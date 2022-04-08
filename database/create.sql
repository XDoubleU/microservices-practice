CREATE TABLE "public.Products" (
	"ID" serial NOT NULL,
	"Name" VARCHAR(255) NOT NULL,
	"Price" DECIMAL NOT NULL,
	"Stock" integer NOT NULL,
	CONSTRAINT "Products_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Orders" (
	"ID" serial NOT NULL,
	"Customer_ID" integer NOT NULL,
	CONSTRAINT "Orders_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Orders_Products" (
	"Order_ID" integer NOT NULL,
	"Product_ID" integer NOT NULL,
	"Amount" integer NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Customers" (
	"ID" serial NOT NULL,
	"Firstname" VARCHAR(255) NOT NULL,
	"Lastname" VARCHAR(255) NOT NULL,
	CONSTRAINT "Customers_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "Orders" ADD CONSTRAINT "Orders_fk0" FOREIGN KEY ("Customer_ID") REFERENCES "Customers"("ID");

ALTER TABLE "Orders_Products" ADD CONSTRAINT "Orders_Products_fk0" FOREIGN KEY ("Order_ID") REFERENCES "Orders"("ID");
ALTER TABLE "Orders_Products" ADD CONSTRAINT "Orders_Products_fk1" FOREIGN KEY ("Product_ID") REFERENCES "Products"("ID");





