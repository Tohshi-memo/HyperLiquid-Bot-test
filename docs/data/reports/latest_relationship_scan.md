# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T19:52:47.173880+00:00`
- Price records: `672`
- Market context records: `7284`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.2109` n `131` status `ready` deltaP `3.1348` edge `0.001` maxDD `-0.5817`
- `market_context_high->fx_4h` score `-0.8256` n `129` status `ready` deltaP `6.0344` edge `0.0139` maxDD `-1.4649`
- `market_context_high->crypto_alt_1h` score `-0.844` n `131` status `ready` deltaP `-2.2375` edge `0.0106` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9346` n `131` status `ready` deltaP `1.609` edge `0.0105` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-1.0242` n `125` status `ready` deltaP `-1.2174` edge `-0.0004` maxDD `-2.1564`
- `market_context_high->commodity_1h` score `-1.0903` n `131` status `ready` deltaP `-2.0207` edge `-0.0153` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-1.1802` n `131` status `ready` deltaP `0.6365` edge `-0.0932` maxDD `-1.3212`
- `market_context_high->unknown_4h` score `-1.2406` n `129` status `ready` deltaP `7.0169` edge `0.0857` maxDD `-6.2026`
- `market_context_high->commodity_4h` score `-1.2939` n `129` status `ready` deltaP `0.6471` edge `-0.0153` maxDD `-2.4139`
- `market_context_high->index_1h` score `-1.4853` n `131` status `ready` deltaP `-6.9023` edge `-0.0105` maxDD `-2.3805`
- `market_context_high->metal_1h` score `-2.2852` n `131` status `ready` deltaP `-10.0802` edge `-0.0074` maxDD `-1.9332`
- `market_context_high->metal_4h` score `-2.6187` n `129` status `ready` deltaP `-11.3963` edge `-0.0142` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.8324` n `125` status `ready` deltaP `-4.8696` edge `-0.1238` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-4.3176` n `129` status `ready` deltaP `-1.4452` edge `-0.0335` maxDD `-18.6668`
- `market_context_high->equity_1h` score `-4.7464` n `131` status `ready` deltaP `-10.569` edge `-0.0724` maxDD `-15.5469`
- `market_context_high->crypto_major_4h` score `-5.2545` n `129` status `ready` deltaP `-1.5067` edge `-0.0384` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.4488` n `129` status `ready` deltaP `-15.8666` edge `-0.0657` maxDD `-12.2741`
- `market_context_high->unknown_24h` score `-6.0269` n `126` status `ready` deltaP `-12.0784` edge `-0.0571` maxDD `-17.1696`
- `market_context_high->metal_24h` score `-11.9669` n `126` status `ready` deltaP `-30.4315` edge `-0.142` maxDD `-25.5224`
- `market_context_high->index_24h` score `-14.3822` n `125` status `ready` deltaP `-29.6` edge `-0.1803` maxDD `-39.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
