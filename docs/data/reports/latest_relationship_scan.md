# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T06:52:27.517883+00:00`
- Price records: `672`
- Market context records: `7113`
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

- `market_context_high->fx_4h` score `0.3846` n `146` status `ready` deltaP `15.7659` edge `0.0142` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1098` n `146` status `ready` deltaP `4.2367` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.124` n `146` status `ready` deltaP `-0.4307` edge `0.0484` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.5435` n `146` status `ready` deltaP `-0.1538` edge `-0.0067` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5718` n `146` status `ready` deltaP `3.5744` edge `0.0381` maxDD `-7.1523`
- `market_context_high->crypto_alt_1h` score `-0.5736` n `146` status `ready` deltaP `1.0705` edge `0.0315` maxDD `-4.5815`
- `market_context_high->commodity_1h` score `-0.8405` n `146` status `ready` deltaP `-3.9783` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.4009` n `146` status `ready` deltaP `-4.8843` edge `-0.0435` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5076` n `146` status `ready` deltaP `-6.4905` edge `-0.0058` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5495` n `146` status `ready` deltaP `-6.8326` edge `0.0071` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.141` n `146` status `ready` deltaP `2.2639` edge `-0.0473` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0573` n `146` status `ready` deltaP `3.8841` edge `0.0106` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.6848` n `146` status `ready` deltaP `-9.5082` edge `-0.1128` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.1232` n `146` status `ready` deltaP `-3.6439` edge `-0.0494` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4114` n `146` status `ready` deltaP `-8.8018` edge `-0.0121` maxDD `-5.414`
- `market_context_high->fx_24h` score `-4.6229` n `146` status `ready` deltaP `-12.0196` edge `-0.0224` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.7422` n `146` status `ready` deltaP `0.1587` edge `-0.0177` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.3138` n `146` status `ready` deltaP `-26.9358` edge `-0.0819` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.756` n `146` status `ready` deltaP `-2.8045` edge `-0.2406` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7094` n `146` status `ready` deltaP `-26.6766` edge `-0.1576` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
