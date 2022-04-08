CREATE TABLE "products" (
	"id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	"price" DECIMAL NOT NULL,
	"stock" integer NOT NULL,
	CONSTRAINT "products_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "orders" (
	"id" serial NOT NULL,
	"customer_id" integer NOT NULL,
	CONSTRAINT "orders_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "orders_products" (
	"order_id" integer NOT NULL,
	"product_id" integer NOT NULL,
	"amount" integer NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "customers" (
	"id" serial NOT NULL,
	"firstname" VARCHAR(255) NOT NULL,
	"lastname" VARCHAR(255) NOT NULL,
	CONSTRAINT "customers_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "orders" ADD CONSTRAINT "orders_fk0" FOREIGN KEY ("customer_id") REFERENCES "customers"("id");

ALTER TABLE "orders_products" ADD CONSTRAINT "orders_products_fk0" FOREIGN KEY ("order_id") REFERENCES "orders"("id");
ALTER TABLE "orders_products" ADD CONSTRAINT "orders_products_fk1" FOREIGN KEY ("product_id") REFERENCES "products"("id");





