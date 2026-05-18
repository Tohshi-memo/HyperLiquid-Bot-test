# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T07:52:16.368297+00:00`
- Price records: `672`
- Market context records: `1097`
- Flow alert records: `5064`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.8117` n `150` status `ready` deltaP `36.5139` edge `1.2039` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.1` n `150` status `ready` deltaP `12.875` edge `0.5459` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.0695` n `150` status `ready` deltaP `15.6527` edge `0.4511` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.193` n `150` status `ready` deltaP `-2.9305` edge `0.619` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.8057` n `150` status `ready` deltaP `15.1319` edge `0.3304` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.0601` n `167` status `ready` deltaP `11.6411` edge `0.1604` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0802` n `167` status `ready` deltaP `9.5726` edge `0.0945` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5337` n `168` status `ready` deltaP `7.9448` edge `0.0232` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3508` n `168` status `ready` deltaP `2.8799` edge `0.0478` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1376` n `168` status `ready` deltaP `8.3155` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0665` n `167` status `ready` deltaP `8.5082` edge `0.1404` maxDD `-8.0874`
- `market_context_high->crypto_major_1h` score `0.0525` n `168` status `ready` deltaP `7.1322` edge `0.0334` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.1585` n `168` status `ready` deltaP `7.2498` edge `-0.0005` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3006` n `168` status `ready` deltaP `2.7944` edge `0.0406` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6789` n `167` status `ready` deltaP `1.7252` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7084` n `168` status `ready` deltaP `-1.3259` edge `-0.0012` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0735` n `167` status `ready` deltaP `4.8708` edge `0.1201` maxDD `-16.2161`
- `market_context_high->metal_4h` score `-2.2025` n `167` status `ready` deltaP `7.7343` edge `-0.0397` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-3.0493` n `167` status `ready` deltaP `9.5315` edge `-0.196` maxDD `-6.7322`
- `market_context_high->commodity_4h` score `-3.1179` n `167` status `ready` deltaP `-10.6306` edge `-0.0121` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
