# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T22:52:24.016810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8280`

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

- `market_context_high->unknown_24h` score `1244.2035` n `148` status `ready` deltaP `-2.135` edge `103.7906` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.1068` n `149` status `ready` deltaP `4.385` edge `1.7449` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.0404` n `148` status `ready` deltaP `21.2838` edge `0.0136` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2332` n `149` status `ready` deltaP `8.0175` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0651` n `149` status `ready` deltaP `7.534` edge `0.0042` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.091` n `149` status `ready` deltaP `8.4767` edge `0.0065` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3457` n `149` status `ready` deltaP `7.8112` edge `0.041` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3616` n `149` status `ready` deltaP `6.5306` edge `0.0384` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6476` n `149` status `ready` deltaP `-0.4903` edge `0.0077` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7243` n `149` status `ready` deltaP `-3.3246` edge `-0.0024` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.7493` n `148` status `ready` deltaP `10.8437` edge `0.0225` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8674` n `149` status `ready` deltaP `7.227` edge `-0.0053` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3851` n `149` status `ready` deltaP `1.2388` edge `0.0054` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5736` n `149` status `ready` deltaP `2.7458` edge `0.0163` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1016` n `149` status `ready` deltaP `-9.9413` edge `-0.03` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4534` n `149` status `ready` deltaP `3.5092` edge `-0.0342` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5613` n `148` status `ready` deltaP `-0.2393` edge `0.0068` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.6935` n `148` status `ready` deltaP `-2.1021` edge `0.0262` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.2417` n `148` status `ready` deltaP `3.8335` edge `-0.0826` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.4853` n `149` status `ready` deltaP `-4.2396` edge `-0.1516` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
