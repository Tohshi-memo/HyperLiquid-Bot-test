# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T11:07:23.694072+00:00`
- Price records: `672`
- Market context records: `969`
- Flow alert records: `2714`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.0929` n `150` status `ready` deltaP `34.3403` edge `1.0622` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.5318` n `150` status `ready` deltaP `10.9375` edge `0.7214` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3228` n `150` status `ready` deltaP `0.8264` edge `0.3652` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.6282` n `150` status `ready` deltaP `-0.7708` edge `0.257` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2761` n `206` status `ready` deltaP `2.9213` edge `0.0383` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3516` n `206` status `ready` deltaP `1.7833` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6442` n `206` status `ready` deltaP `1.122` edge `0.0157` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6457` n `194` status `ready` deltaP `2.2143` edge `0.0021` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.726` n `206` status `ready` deltaP `2.9184` edge `0.0054` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0742` n `206` status `ready` deltaP `6.193` edge `-0.0067` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.2304` n `206` status `ready` deltaP `-1.7194` edge `-0.0139` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.4004` n `194` status `ready` deltaP `1.4411` edge `0.0889` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6286` n `194` status `ready` deltaP `-1.2525` edge `0.0249` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8706` n `206` status `ready` deltaP `-2.0682` edge `-0.0301` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.9861` n `206` status `ready` deltaP `0.6541` edge `-0.0259` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4548` n `194` status `ready` deltaP `9.3805` edge `0.1035` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.8871` n `194` status `ready` deltaP `-1.1991` edge `0.08` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.159` n `194` status `ready` deltaP `7.8703` edge `-0.1279` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.1887` n `194` status `ready` deltaP `-1.6674` edge `0.0232` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-3.985` n `150` status `ready` deltaP `5.1875` edge `0.0051` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
