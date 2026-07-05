# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T09:07:26.850480+00:00`
- Price records: `672`
- Market context records: `5756`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8664`

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

- `market_context_high->equity_24h` score `0.7915` n `224` status `ready` deltaP `15.0546` edge `0.509` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1471` n `285` status `ready` deltaP `7.3679` edge `0.127` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.195` n `293` status `ready` deltaP `3.2842` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4414` n `293` status `ready` deltaP `1.7453` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6072` n `293` status `ready` deltaP `3.3737` edge `0.0276` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6499` n `293` status `ready` deltaP `-0.0271` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7405` n `293` status `ready` deltaP `3.7752` edge `0.0366` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.7583` n `293` status `ready` deltaP `-1.6196` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.8423` n `293` status `ready` deltaP `2.2363` edge `0.0353` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9363` n `224` status `ready` deltaP `14.2361` edge `0.0434` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1544` n `285` status `ready` deltaP `1.4752` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2199` n `285` status `ready` deltaP `3.3189` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6123` n `285` status `ready` deltaP `-7.2363` edge `-0.0491` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6635` n `285` status `ready` deltaP `8.2168` edge `0.1538` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9705` n `224` status `ready` deltaP `0.6944` edge `0.029` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7297` n `285` status `ready` deltaP `-2.3636` edge `-0.0275` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.7994` n `285` status `ready` deltaP `6.5543` edge `0.1087` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.491` n `224` status `ready` deltaP `7.3413` edge `0.0225` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8562` n `224` status `ready` deltaP `-10.1439` edge `-0.2511` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.8578` n `224` status `ready` deltaP `-13.1944` edge `-0.0862` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
