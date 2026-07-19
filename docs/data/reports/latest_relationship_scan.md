# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T19:37:26.435128+00:00`
- Price records: `672`
- Market context records: `7283`
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

- `market_context_high->fx_1h` score `-0.2249` n `132` status `ready` deltaP `2.8801` edge `0.0009` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.8175` n `132` status `ready` deltaP `-1.8327` edge `0.0113` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.8422` n `130` status `ready` deltaP `5.8057` edge `0.0133` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.948` n `132` status `ready` deltaP `1.3655` edge `0.0104` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-1.0661` n `125` status `ready` deltaP `-1.8435` edge `-0.0016` maxDD `-2.1564`
- `market_context_high->commodity_1h` score `-1.0662` n `132` status `ready` deltaP `-1.795` edge `-0.0148` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-1.2022` n `132` status `ready` deltaP `0.2722` edge `-0.0936` maxDD `-1.3212`
- `market_context_high->unknown_4h` score `-1.217` n `130` status `ready` deltaP `7.2818` edge `0.0859` maxDD `-6.2026`
- `market_context_high->commodity_4h` score `-1.3441` n `130` status `ready` deltaP `0.1999` edge `-0.0165` maxDD `-2.4139`
- `market_context_high->index_1h` score `-1.4433` n `132` status `ready` deltaP `-6.4223` edge `-0.0102` maxDD `-2.3805`
- `market_context_high->metal_1h` score `-2.2463` n `132` status `ready` deltaP `-9.5945` edge `-0.0074` maxDD `-1.9332`
- `market_context_high->metal_4h` score `-2.6319` n `130` status `ready` deltaP `-11.4704` edge `-0.0154` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.7307` n `125` status `ready` deltaP `-4.2435` edge `-0.1195` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-4.5319` n `130` status `ready` deltaP `-1.7613` edge `-0.0387` maxDD `-19.5109`
- `market_context_high->equity_1h` score `-4.69` n `132` status `ready` deltaP `-10.0601` edge `-0.0711` maxDD `-15.5469`
- `market_context_high->crypto_major_4h` score `-5.3491` n `130` status `ready` deltaP `-1.8645` edge `-0.0439` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.4775` n `130` status `ready` deltaP `-16.0574` edge `-0.0657` maxDD `-12.3635`
- `market_context_high->unknown_24h` score `-6.0867` n `126` status `ready` deltaP `-12.0784` edge `-0.0587` maxDD `-17.44`
- `market_context_high->metal_24h` score `-12.141` n `126` status `ready` deltaP `-31.0516` edge `-0.1455` maxDD `-26.0725`
- `market_context_high->index_24h` score `-14.5587` n `125` status `ready` deltaP `-29.6` edge `-0.1839` maxDD `-39.5596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
