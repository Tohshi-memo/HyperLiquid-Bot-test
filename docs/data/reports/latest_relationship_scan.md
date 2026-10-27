# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T07:52:24.775840+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9517`

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

- `market_context_high->unknown_4h` score `84.2847` n `136` status `ready` deltaP `4.4925` edge `7.0147` maxDD `-0.6743`
- `market_context_high->unknown_1h` score `25.6895` n `136` status `ready` deltaP `1.202` edge `2.1817` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.539` n `120` status `ready` deltaP `25.0939` edge `0.034` maxDD `-2.1766`
- `market_context_high->fx_1h` score `0.4967` n `136` status `ready` deltaP `11.0558` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4595` n `136` status `ready` deltaP `13.1904` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1191` n `136` status `ready` deltaP `11.7207` edge `0.0118` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.2225` n `120` status `ready` deltaP `17.344` edge `0.1084` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.2823` n `136` status `ready` deltaP `2.316` edge `0.0111` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.5112` n `136` status `ready` deltaP `5.1999` edge `0.0281` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5266` n `136` status `ready` deltaP `0.3258` edge `-0.0014` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.5271` n `120` status `ready` deltaP `10.2527` edge `0.0213` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5928` n `136` status `ready` deltaP `4.887` edge `0.0399` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.7148` n `136` status `ready` deltaP `9.783` edge `0.002` maxDD `-4.7087`
- `market_context_high->equity_1h` score `-1.3395` n `136` status `ready` deltaP `2.8839` edge `0.0049` maxDD `-9.6688`
- `market_context_high->crypto_alt_1h` score `-2.0523` n `136` status `ready` deltaP `-1.5014` edge `-0.0097` maxDD `-12.8063`
- `market_context_high->equity_24h` score `-2.1584` n `120` status `ready` deltaP `3.6742` edge `-0.0039` maxDD `-15.7851`
- `market_context_high->index_4h` score `-2.5558` n `136` status `ready` deltaP `-3.4434` edge `-0.023` maxDD `-5.6952`
- `market_context_high->crypto_major_4h` score `-3.6653` n `136` status `ready` deltaP `3.4254` edge `-0.0608` maxDD `-27.2224`
- `market_context_high->crypto_major_24h` score `-4.6655` n `120` status `ready` deltaP `-0.4997` edge `-0.1091` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.8381` n `136` status `ready` deltaP `3.5599` edge `-0.1102` maxDD `-35.704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
