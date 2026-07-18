# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T06:37:24.952072+00:00`
- Price records: `672`
- Market context records: `7112`
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
- `market_context_high->unknown_1h` score `-0.1252` n `146` status `ready` deltaP `-0.4307` edge `0.0483` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.5513` n `146` status `ready` deltaP `-0.3035` edge `-0.0067` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.571` n `146` status `ready` deltaP `3.5744` edge `0.0382` maxDD `-7.1523`
- `market_context_high->crypto_alt_1h` score `-0.5736` n `146` status `ready` deltaP `1.0705` edge `0.0315` maxDD `-4.5815`
- `market_context_high->commodity_1h` score `-0.8405` n `146` status `ready` deltaP `-3.9783` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.4103` n `146` status `ready` deltaP `-5.0367` edge `-0.0437` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5076` n `146` status `ready` deltaP `-6.4905` edge `-0.0058` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5502` n `146` status `ready` deltaP `-6.8326` edge `0.007` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1512` n `146` status `ready` deltaP `2.1142` edge `-0.0476` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0675` n `146` status `ready` deltaP `3.7316` edge `0.0103` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.6764` n `146` status `ready` deltaP `-9.5082` edge `-0.1121` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.1232` n `146` status `ready` deltaP `-3.6439` edge `-0.0494` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.3993` n `146` status `ready` deltaP `-8.6494` edge `-0.0121` maxDD `-5.414`
- `market_context_high->fx_24h` score `-4.6078` n `146` status `ready` deltaP `-11.8459` edge `-0.0223` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.7652` n `146` status `ready` deltaP `0.0063` edge `-0.0186` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.2927` n `146` status `ready` deltaP `-26.7622` edge `-0.0813` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7742` n `146` status `ready` deltaP `-2.9569` edge `-0.2411` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.6883` n `146` status `ready` deltaP `-26.503` edge `-0.157` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
