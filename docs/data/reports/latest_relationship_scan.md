# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T19:37:43.779501+00:00`
- Price records: `672`
- Market context records: `2896`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `10.4303` n `142` status `ready` deltaP `9.8201` edge `1.1954` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.6625` n `142` status `ready` deltaP `11.5121` edge `0.5955` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.1463` n `142` status `ready` deltaP `10.4142` edge `0.4059` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1608` n `142` status `ready` deltaP `9.891` edge `0.2122` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.74` n `142` status `ready` deltaP `15.5516` edge `0.3507` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4814` n `142` status `ready` deltaP `13.3009` edge `0.0572` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.2786` n `142` status `ready` deltaP `5.4234` edge `0.0924` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0843` n `142` status `ready` deltaP `3.5992` edge `0.0146` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1137` n `142` status `ready` deltaP `4.8587` edge `0.0961` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.2558` n `142` status `ready` deltaP `4.4805` edge `0.0219` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.5991` n `142` status `ready` deltaP `-0.5819` edge `0.0024` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6461` n `142` status `ready` deltaP `4.9465` edge `0.0602` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.6701` n `142` status `ready` deltaP `-1.2524` edge `0.0358` maxDD `-2.6634`
- `market_context_high->metal_1h` score `-0.712` n `142` status `ready` deltaP `-0.9151` edge `-0.0006` maxDD `-3.0996`
- `market_context_high->crypto_alt_4h` score `-0.7287` n `142` status `ready` deltaP `14.0329` edge `0.2798` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.737` n `142` status `ready` deltaP `5.1236` edge `0.0583` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1072` n `142` status `ready` deltaP `3.8195` edge `0.0246` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.1821` n `142` status `ready` deltaP `-3.9054` edge `0.0054` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3375` n `142` status `ready` deltaP `-1.8852` edge `-0.0117` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
