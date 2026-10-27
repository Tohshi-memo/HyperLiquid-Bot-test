# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T19:07:30.218887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8700`

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

- `market_context_high->unknown_4h` score `78.1074` n `136` status `ready` deltaP `4.618` edge `6.4934` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9783` n `135` status `ready` deltaP `27.1875` edge `0.0524` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4056` n `148` status `ready` deltaP `9.9773` edge `0.0031` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4018` n `136` status `ready` deltaP `12.4551` edge `0.0103` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0748` n `148` status `ready` deltaP `8.6219` edge `0.0076` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3182` n `148` status `ready` deltaP `8.1` edge `0.0335` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3383` n `136` status `ready` deltaP `6.8687` edge `0.0479` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.483` n `135` status `ready` deltaP `11.0417` edge `0.0217` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5794` n `148` status `ready` deltaP `0.0769` edge `0.0096` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6412` n `148` status `ready` deltaP `-1.5779` edge `-0.0034` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8849` n `136` status `ready` deltaP `7.1915` edge `-0.0073` maxDD `-4.6603`
- `market_context_high->unknown_1h` score `-1.0291` n `148` status `ready` deltaP `0.8497` edge `-0.0425` maxDD `-1.5807`
- `market_context_high->metal_24h` score `-1.0598` n `135` status `ready` deltaP `15.0579` edge `0.0891` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4273` n `148` status `ready` deltaP `1.7923` edge `-0.0037` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6586` n `148` status `ready` deltaP `2.6096` edge `0.0063` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.6686` n `135` status `ready` deltaP `8.0671` edge `0.1036` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.9817` n `136` status `ready` deltaP `-7.7386` edge `-0.0347` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7681` n `135` status `ready` deltaP `0.544` edge `-0.001` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8581` n `136` status `ready` deltaP `2.9412` edge `-0.0823` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5478` n `136` status `ready` deltaP `-0.5829` edge `-0.184` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
