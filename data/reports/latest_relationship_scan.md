# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T09:22:57.045638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9426`

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

- `market_context_high->unknown_4h` score `87.3363` n `135` status `ready` deltaP `5.0045` edge `7.2599` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.6251` n `135` status `ready` deltaP `1.8175` edge `1.3389` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.8039` n `125` status `ready` deltaP `26.2073` edge `0.0444` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4847` n `135` status `ready` deltaP `10.906` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.1106` n `135` status `ready` deltaP `11.5436` edge `0.0119` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3393` n `135` status `ready` deltaP `1.8286` edge `0.0096` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4918` n `135` status `ready` deltaP `5.4369` edge `0.029` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5484` n `135` status `ready` deltaP `-0.0632` edge `-0.0016` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.6414` n `135` status `ready` deltaP `10.1479` edge `0.0042` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.644` n `125` status `ready` deltaP `8.2593` edge `0.0196` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.6474` n `125` status `ready` deltaP `15.5106` edge `0.0952` maxDD `-6.204`
- `market_context_high->commodity_4h` score `-0.6783` n `135` status `ready` deltaP `4.4026` edge `0.036` maxDD `-1.0837`
- `market_context_high->equity_1h` score `-1.3404` n `135` status `ready` deltaP `2.4894` edge `0.0028` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.8478` n `125` status `ready` deltaP `5.5542` edge `0.0225` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9748` n `135` status `ready` deltaP `-1.3407` edge `-0.0079` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.4692` n `135` status `ready` deltaP `-3.1166` edge `-0.0228` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.6317` n `135` status `ready` deltaP `3.9646` edge `-0.0601` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.5567` n `125` status `ready` deltaP `-0.4464` edge `-0.0955` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7084` n `135` status `ready` deltaP `3.9194` edge `-0.1064` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
