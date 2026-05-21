# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T07:52:17.798581+00:00`
- Price records: `672`
- Market context records: `1403`
- Flow alert records: `5953`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_major_24h` score `12.3648` n `156` status `ready` deltaP `27.4038` edge `0.9609` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4721` n `156` status `ready` deltaP `28.8061` edge `0.9656` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2021` n `156` status `ready` deltaP `10.6838` edge `1.029` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8238` n `156` status `ready` deltaP `19.4978` edge `0.2973` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.225` n `156` status `ready` deltaP `12.6603` edge `0.3337` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0458` n `198` status `ready` deltaP `6.427` edge `0.1273` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0602` n `156` status `ready` deltaP `9.7088` edge `0.0452` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0445` n `204` status `ready` deltaP `4.4999` edge `0.0128` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1171` n `204` status `ready` deltaP `2.8942` edge `0.0268` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2214` n `204` status `ready` deltaP `4.4264` edge `-0.0014` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.7006` n `204` status `ready` deltaP `5.081` edge `-0.0062` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.755` n `204` status `ready` deltaP `0.411` edge `0.0214` maxDD `-3.6309`
- `market_context_high->index_4h` score `-0.7602` n `198` status `ready` deltaP `-0.5774` edge `0.0494` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.8356` n `204` status `ready` deltaP `-1.5381` edge `0.0021` maxDD `-2.252`
- `market_context_high->fx_4h` score `-1.5264` n `198` status `ready` deltaP `-3.2012` edge `-0.0088` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.5376` n `204` status `ready` deltaP `-1.9725` edge `-0.0043` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.5775` n `198` status `ready` deltaP `4.0697` edge `0.1123` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.6273` n `198` status `ready` deltaP `5.6618` edge `0.1586` maxDD `-19.5565`
- `market_context_high->metal_4h` score `-2.2385` n `198` status `ready` deltaP `5.6987` edge `0.0026` maxDD `-10.8373`
- `market_context_high->commodity_4h` score `-4.0145` n `198` status `ready` deltaP `-10.1965` edge `-0.0119` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
