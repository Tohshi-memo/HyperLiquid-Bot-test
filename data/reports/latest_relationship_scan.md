# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T06:25:26.540674+00:00`
- Price records: `672`
- Market context records: `7111`
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

- `market_context_high->fx_4h` score `0.3635` n `147` status `ready` deltaP `15.3746` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1292` n `147` status `ready` deltaP `3.878` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1685` n `147` status `ready` deltaP `-0.7475` edge `0.0468` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.365` n `147` status `ready` deltaP `1.2516` edge `0.0313` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5631` n `147` status `ready` deltaP `3.7415` edge `0.0381` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.5673` n `147` status `ready` deltaP `-0.611` edge `-0.0067` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8202` n `147` status `ready` deltaP `-3.6335` edge `-0.0193` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3997` n `147` status `ready` deltaP `-4.877` edge `-0.0434` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5293` n `147` status `ready` deltaP `-6.7467` edge `-0.0059` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5671` n `147` status `ready` deltaP `-7.0516` edge `0.0063` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.1354` n `147` status `ready` deltaP `2.328` edge `-0.047` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0585` n `147` status `ready` deltaP `3.9054` edge `0.0103` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.6208` n `147` status `ready` deltaP `-9.2333` edge `-0.1093` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0824` n `147` status `ready` deltaP `-3.2386` edge `-0.0487` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.4004` n `147` status `ready` deltaP `-8.66` edge `-0.012` maxDD `-5.4243`
- `market_context_high->fx_24h` score `-4.6159` n `147` status `ready` deltaP `-11.9472` edge `-0.0223` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.7443` n `147` status `ready` deltaP `0.2219` edge `-0.0183` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.2747` n `147` status `ready` deltaP `-26.6865` edge `-0.0803` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7116` n `147` status `ready` deltaP `-2.6993` edge `-0.2376` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7229` n `147` status `ready` deltaP `-26.3853` edge `-0.1553` maxDD `-42.3232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
