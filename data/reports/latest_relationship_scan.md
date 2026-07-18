# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T07:07:26.605140+00:00`
- Price records: `672`
- Market context records: `7114`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11664`

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

- `market_context_high->fx_4h` score `0.3767` n `146` status `ready` deltaP `15.6135` edge `0.0142` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1096` n `146` status `ready` deltaP `-0.281` edge `0.0486` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1183` n `146` status `ready` deltaP `4.087` edge `0.0027` maxDD `-0.276`
- `market_context_high->index_1h` score `-0.5349` n `146` status `ready` deltaP `-0.0041` edge `-0.0066` maxDD `-2.2895`
- `market_context_high->crypto_alt_1h` score `-0.5592` n `146` status `ready` deltaP `1.2202` edge `0.0317` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.571` n `146` status `ready` deltaP `3.5744` edge `0.0382` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8405` n `146` status `ready` deltaP `-3.9783` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.4009` n `146` status `ready` deltaP `-4.8843` edge `-0.0435` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5076` n `146` status `ready` deltaP `-6.4905` edge `-0.0058` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5487` n `146` status `ready` deltaP `-6.8326` edge `0.0072` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1309` n `146` status `ready` deltaP `2.4136` edge `-0.047` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0447` n `146` status `ready` deltaP `4.0365` edge `0.0112` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.6944` n `146` status `ready` deltaP `-9.5082` edge `-0.1136` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.1098` n `146` status `ready` deltaP `-3.4914` edge `-0.0493` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4236` n `146` status `ready` deltaP `-8.9542` edge `-0.0121` maxDD `-5.414`
- `market_context_high->fx_24h` score `-4.638` n `146` status `ready` deltaP `-12.1932` edge `-0.0225` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.7192` n `146` status `ready` deltaP `0.3111` edge `-0.0168` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.3337` n `146` status `ready` deltaP `-27.1095` edge `-0.0824` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7366` n `146` status `ready` deltaP `-2.652` edge `-0.24` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7305` n `146` status `ready` deltaP `-26.8502` edge `-0.1582` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
