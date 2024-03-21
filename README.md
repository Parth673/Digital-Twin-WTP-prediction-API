
# Digital Twin of Wind Turbine Power prediction API

The following API is use to predict the power output of wind turbine. It uses PINN (Physics Informed Neural Network) Deep Learning Model that is use to predict the power output of wind turbine. This API is used in **Pratibimb Digital Twin of Wind Turbine**. 

- **Turbine Name:** Senvion MM82 (Senvion MM82 kW)
- **Type:** Onshore

## Input and Ouput of API

You can sen a list or single value in dictioany or JSON format.
After hitting API you will get a JSON/dictionary of list or single value of power generated forcast.

**Input:** **v** 
WindSpeed(m/s), **β** Blade pitch (rad), **T** Torque(Nm)

**Ouput:** 
**P** Power (kW)


Run

```bash
  python app.py
```


## Credits


Link: https://github.com/alfonsogijon/windturbines_pinns


Please adhere to this `alfonsogijon`.
