# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T05:07:19.625388+00:00`
- Price records: `520`
- Market context records: `615`
- Flow alert records: `1740`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.1824` n `146` status `ready` deltaP `7.5698` edge `0.3862` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.7621` n `146` status `ready` deltaP `13.7148` edge `0.3388` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.062` n `146` status `ready` deltaP `9.4192` edge `0.0164` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3221` n `146` status `ready` deltaP `1.9665` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.647` n `146` status `ready` deltaP `1.0702` edge `0.0364` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6849` n `146` status `ready` deltaP `0.0214` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0655` n `146` status `ready` deltaP `-3.3981` edge `-0.0058` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1044` n `146` status `ready` deltaP `6.0503` edge `-0.0009` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2626` n `146` status `ready` deltaP `-2.127` edge `-0.01` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5104` n `146` status `ready` deltaP `5.2511` edge `0.0961` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6563` n `146` status `ready` deltaP `5.9068` edge `-0.0051` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2116` n `146` status `ready` deltaP `14.7749` edge `0.0878` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.285` n `146` status `ready` deltaP `-0.5315` edge `-0.0346` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.7218` n `146` status `ready` deltaP `-7.606` edge `0.0234` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2014` n `146` status `ready` deltaP `-3.1315` edge `-0.0307` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2649` n `146` status `ready` deltaP `-4.237` edge `-0.0479` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6918` n `146` status `ready` deltaP `-6.3534` edge `0.0848` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2715` n `146` status `ready` deltaP `-2.6615` edge `-0.0127` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6883` n `146` status `ready` deltaP `2.3891` edge `-0.2188` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7122` n `146` status `ready` deltaP `-11.0861` edge `-0.0583` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
