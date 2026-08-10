# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T04:52:31.805866+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10952`

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

- `market_context_high->commodity_4h` score `1.3816` n `166` status `ready` deltaP `15.5745` edge `0.0786` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.9056` n `139` status `ready` deltaP `19.6855` edge `0.025` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7681` n `172` status `ready` deltaP `10.2458` edge `0.03` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.052` n `166` status `ready` deltaP `7.6569` edge `0.0073` maxDD `-0.8679`
- `market_context_high->fx_1h` score `-0.1385` n `172` status `ready` deltaP `4.6338` edge `-0.0004` maxDD `-0.8595`
- `market_context_high->index_1h` score `-0.5298` n `172` status `ready` deltaP `-2.4474` edge `-0.0039` maxDD `-0.8168`
- `market_context_high->index_24h` score `-0.6018` n `139` status `ready` deltaP `2.3243` edge `0.0875` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.7553` n `166` status `ready` deltaP `-1.4381` edge `-0.009` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8568` n `172` status `ready` deltaP `-5.4066` edge `-0.0102` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.22` n `172` status `ready` deltaP `-1.6258` edge `-0.0038` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.4704` n `139` status `ready` deltaP `-3.8507` edge `0.0313` maxDD `-2.9193`
- `market_context_high->crypto_alt_1h` score `-1.5247` n `172` status `ready` deltaP `-8.4981` edge `-0.0367` maxDD `-5.5029`
- `market_context_high->equity_24h` score `-1.7141` n `139` status `ready` deltaP `-2.2382` edge `0.1864` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-2.0367` n `166` status `ready` deltaP `-7.3685` edge `-0.0356` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-2.9096` n `166` status `ready` deltaP `-8.8488` edge `-0.1053` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5367` n `172` status `ready` deltaP `-9.6365` edge `-0.0571` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9448` n `166` status `ready` deltaP `-11.5486` edge `-0.153` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3543` n `139` status `ready` deltaP `-11.2423` edge `-0.1436` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.9185` n `139` status `ready` deltaP `-3.2324` edge `-0.1389` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5469` n `172` status `ready` deltaP `-4.6512` edge `-0.5522` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
