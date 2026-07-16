# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T06:52:33.143586+00:00`
- Price records: `672`
- Market context records: `6894`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `0.4792` n `185` status `ready` deltaP `-4.9951` edge `0.4821` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2222` n `224` status `ready` deltaP `2.6866` edge `0.0021` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5746` n `224` status `ready` deltaP `2.0611` edge `0.0148` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.5863` n `224` status `ready` deltaP `-0.4491` edge `-0.0037` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6581` n `224` status `ready` deltaP `3.5474` edge `0.0119` maxDD `-4.2314`
- `market_context_high->index_1h` score `-0.8126` n `224` status `ready` deltaP `-1.4783` edge `-0.0032` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.8548` n `224` status `ready` deltaP `13.3929` edge `0.0075` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8993` n `224` status `ready` deltaP `-4.5926` edge `-0.0079` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3193` n `224` status `ready` deltaP `-1.8838` edge `-0.0076` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7213` n `224` status `ready` deltaP `-3.8601` edge `-0.0276` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.8347` n `224` status `ready` deltaP `1.4863` edge `-0.0271` maxDD `-13.1084`
- `market_context_high->commodity_24h` score `-1.9516` n `185` status `ready` deltaP `1.1981` edge `0.0162` maxDD `-5.2791`
- `market_context_high->index_4h` score `-2.0174` n `224` status `ready` deltaP `3.4844` edge `-0.0239` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.329` n `224` status `ready` deltaP `1.0997` edge `-0.0076` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9942` n `224` status `ready` deltaP `0.686` edge `-0.0301` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-3.0359` n `224` status `ready` deltaP `-1.1542` edge `-0.0488` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1201` n `224` status `ready` deltaP `-9.0375` edge `0.0368` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2626` n `185` status `ready` deltaP `-6.7029` edge `-0.0069` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.4015` n `224` status `ready` deltaP `0.882` edge `-0.1603` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.5466` n `185` status `ready` deltaP `-14.708` edge `-0.1391` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
