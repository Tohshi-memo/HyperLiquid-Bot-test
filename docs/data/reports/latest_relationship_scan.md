# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T23:52:31.125995+00:00`
- Price records: `672`
- Market context records: `5717`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.6122` n `269` status `ready` deltaP `10.1964` edge `0.2035` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0028` n `219` status `ready` deltaP `17.0496` edge `0.5228` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.321` n `269` status `ready` deltaP `7.6237` edge `0.1472` maxDD `-8.3685`
- `market_context_high->equity_4h` score `0.2237` n `269` status `ready` deltaP `7.5007` edge `0.1325` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1841` n `281` status `ready` deltaP `3.4937` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4497` n `281` status `ready` deltaP `1.5844` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4818` n `281` status `ready` deltaP `2.9317` edge `0.0359` maxDD `-3.9811`
- `market_context_high->index_1h` score `-0.605` n `281` status `ready` deltaP `0.8359` edge `0.0037` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6125` n `281` status `ready` deltaP `3.2929` edge `0.0277` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.7026` n `281` status `ready` deltaP `1.1918` edge `0.0309` maxDD `-4.1249`
- `market_context_high->commodity_1h` score `-0.7301` n `281` status `ready` deltaP `-1.2285` edge `-0.0047` maxDD `-3.7906`
- `market_context_high->fx_24h` score `-1.1446` n `219` status `ready` deltaP `10.4856` edge `0.0417` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1928` n `269` status `ready` deltaP `0.7503` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2858` n `269` status `ready` deltaP `2.1115` edge `0.0056` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6126` n `269` status `ready` deltaP `-7.1233` edge `-0.0499` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8643` n `219` status `ready` deltaP `2.6018` edge `0.0299` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8761` n `269` status `ready` deltaP `-4.0133` edge `-0.0287` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4606` n `219` status `ready` deltaP `6.8065` edge `0.0286` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6546` n `219` status `ready` deltaP `-5.8671` edge `-0.2381` maxDD `-31.9985`
- `market_context_high->commodity_24h` score `-11.5699` n `219` status `ready` deltaP `-9.5225` edge `-0.0675` maxDD `-44.9872`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
