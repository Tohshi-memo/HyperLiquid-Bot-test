# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T12:07:22.019542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `43.6139` n `51` status `ready` deltaP `2.0833` edge `3.6206` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5086` n `52` status `ready` deltaP `23.8977` edge `0.8881` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.477` n `51` status `ready` deltaP `35.3758` edge `0.647` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.5185` n `51` status `ready` deltaP `44.4342` edge `0.0955` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0806` n `53` status `ready` deltaP `16.162` edge `0.1845` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0177` n `52` status `ready` deltaP `35.7763` edge `0.0264` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.3264` n `52` status `ready` deltaP `22.5024` edge `0.1209` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0161` n `133` status `ready` deltaP `20.2251` edge `0.074` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1393` n `53` status `ready` deltaP `15.7694` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.6507` n `53` status `ready` deltaP `15.3203` edge `0.0177` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4232` n `52` status `ready` deltaP `9.6154` edge `0.0109` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3361` n `53` status `ready` deltaP `9.9283` edge `-0.0069` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.063` n `133` status `ready` deltaP `11.7216` edge `-0.028` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0176` n `53` status `ready` deltaP `4.7481` edge `0.0014` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2806` n `52` status `ready` deltaP `6.4845` edge `-0.0135` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.318` n `53` status `ready` deltaP `0.5847` edge `-0.0078` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4506` n `133` status `ready` deltaP `2.3491` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6984` n `51` status `ready` deltaP `21.6503` edge `-0.1983` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7209` n `133` status `ready` deltaP `6.0941` edge `-0.037` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.17` n `133` status `ready` deltaP `-5.6222` edge `-0.0062` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
