# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T10:52:24.759626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1253.131` n `149` status `ready` deltaP `-2.0216` edge `104.5338` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `31.8654` n `149` status `ready` deltaP `4.8423` edge `2.6384` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5241` n `149` status `ready` deltaP `17.9204` edge `-0.007` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1038` n `149` status `ready` deltaP `6.5205` edge `0.001` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.1133` n `149` status `ready` deltaP `10.2503` edge `0.0441` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1392` n `149` status `ready` deltaP `6.7718` edge `0.0031` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1431` n `149` status `ready` deltaP `7.5785` edge `0.0058` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4668` n `149` status `ready` deltaP `5.333` edge `0.0329` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4907` n `149` status `ready` deltaP `1.1564` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8123` n `149` status `ready` deltaP `7.8368` edge `-0.0023` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8527` n `149` status `ready` deltaP `-5.4204` edge `-0.0049` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.4454` n `149` status `ready` deltaP `4.2121` edge `0.0087` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.548` n `149` status `ready` deltaP `-0.5576` edge `-0.0035` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6998` n `149` status `ready` deltaP `1.2488` edge `0.0101` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1572` n `149` status `ready` deltaP `-10.2462` edge `-0.0326` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.388` n `149` status `ready` deltaP `2.4421` edge `-0.0187` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.6822` n `149` status `ready` deltaP `-2.095` edge `0.0276` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.9737` n `149` status `ready` deltaP `-0.5069` edge `-0.0214` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.4863` n `149` status `ready` deltaP `-4.5445` edge `-0.1497` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9561` n `149` status `ready` deltaP `1.813` edge `-0.212` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
