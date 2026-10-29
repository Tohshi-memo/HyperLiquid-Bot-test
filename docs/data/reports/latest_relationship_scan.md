# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T11:52:25.716054+00:00`
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

- `market_context_high->unknown_24h` score `1256.3878` n `149` status `ready` deltaP `-2.0216` edge `104.8052` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `31.6272` n `149` status `ready` deltaP `4.385` edge `2.6216` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5121` n `149` status `ready` deltaP `17.9204` edge `-0.008` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1038` n `149` status `ready` deltaP `6.5205` edge `0.001` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.0975` n `149` status `ready` deltaP `10.4027` edge `0.0444` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1338` n `149` status `ready` deltaP `7.7282` edge `0.006` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1392` n `149` status `ready` deltaP `6.7718` edge `0.0031` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.4631` n `149` status `ready` deltaP `1.4558` edge `0.0101` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.5432` n `149` status `ready` deltaP `4.7342` edge `0.0271` maxDD `-6.9306`
- `market_context_high->metal_4h` score `-0.8107` n `149` status `ready` deltaP `7.8368` edge `-0.0021` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.827` n `149` status `ready` deltaP `-4.9713` edge `-0.0046` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.4792` n `149` status `ready` deltaP `3.8649` edge `0.0082` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5573` n `149` status `ready` deltaP `-0.7073` edge `-0.0037` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.7364` n `149` status `ready` deltaP `0.9494` edge `0.0074` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.2167` n `149` status `ready` deltaP `-10.8559` edge `-0.0335` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5008` n `149` status `ready` deltaP `1.8324` edge `-0.0291` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.6334` n `149` status `ready` deltaP `-1.9213` edge `0.0327` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.9653` n `149` status `ready` deltaP `-0.5069` edge `-0.0207` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.6093` n `149` status `ready` deltaP `-5.1542` edge `-0.1614` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9717` n `149` status `ready` deltaP `1.813` edge `-0.2133` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
