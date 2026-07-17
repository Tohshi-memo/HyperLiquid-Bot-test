# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T09:37:29.547906+00:00`
- Price records: `672`
- Market context records: `7015`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2685` n `228` status `ready` deltaP `1.9461` edge `0.0011` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.4029` n `215` status `ready` deltaP `-5.8269` edge `0.4422` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.5399` n `228` status `ready` deltaP `1.7019` edge `0.0301` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6446` n `228` status `ready` deltaP `-1.0295` edge `0.001` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6554` n `228` status `ready` deltaP `0.8535` edge `0.0014` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-1.0287` n `228` status `ready` deltaP `10.2723` edge `0.006` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.045` n `228` status `ready` deltaP `3.3381` edge `0.0259` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2457` n `228` status `ready` deltaP `-2.3637` edge `-0.0159` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2744` n `228` status `ready` deltaP `-1.7991` edge `-0.0041` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.7112` n `228` status `ready` deltaP `-4.7256` edge `-0.0389` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7703` n `228` status `ready` deltaP `7.9857` edge `-0.0103` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8153` n `228` status `ready` deltaP `3.9132` edge `-0.0034` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8713` n `228` status `ready` deltaP `7.0818` edge `0.0112` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.459` n `228` status `ready` deltaP `-5.9799` edge `0.07` maxDD `-10.1375`
- `market_context_high->crypto_alt_4h` score `-2.6962` n `228` status `ready` deltaP `1.7517` edge `0.0212` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.0511` n `215` status `ready` deltaP `-4.5212` edge `-0.0849` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.2038` n `215` status `ready` deltaP `-5.8204` edge `-0.0156` maxDD `-5.0065`
- `market_context_high->crypto_major_4h` score `-4.8674` n `228` status `ready` deltaP `1.5805` edge `0.0123` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.3747` n `228` status `ready` deltaP `5.0278` edge `-0.0597` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3852` n `215` status `ready` deltaP `-9.5995` edge `-0.0545` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
