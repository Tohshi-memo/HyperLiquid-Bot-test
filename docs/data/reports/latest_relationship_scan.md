# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T06:37:29.818183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `news_risk_high->unknown_4h` score `15.627` n `48` status `ready` deltaP `26.4228` edge `1.1307` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0584` n `33` status `ready` deltaP `-7.4305` edge `0.7429` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0584` n `33` status `ready` deltaP `-7.4305` edge `0.7429` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.8198` n `51` status `ready` deltaP `20.3769` edge `0.2129` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `3.8038` n `48` status `ready` deltaP `29.878` edge `0.1743` maxDD `-1.5205`
- `news_risk_high->fx_4h` score `2.9604` n `48` status `ready` deltaP `35.315` edge `0.0247` maxDD `-0.0746`
- `news_risk_high->fx_1h` score `1.2086` n `51` status `ready` deltaP `16.696` edge `0.0064` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0524` n `135` status `ready` deltaP `6.1721` edge `0.0914` maxDD `-1.5876`
- `news_risk_high->index_4h` score `1.0396` n `48` status `ready` deltaP `15.3963` edge `0.0226` maxDD `-0.0884`
- `news_risk_high->equity_1h` score `0.875` n `51` status `ready` deltaP `18.7918` edge `0.0234` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7181` n `126` status `ready` deltaP `22.1569` edge `-0.0707` maxDD `-0.3736`
- `news_risk_high->metal_4h` score `0.5269` n `48` status `ready` deltaP `13.6687` edge `-0.0075` maxDD `-0.1775`
- `news_risk_high->index_1h` score `0.2395` n `51` status `ready` deltaP `9.4223` edge `0.0032` maxDD `-0.1583`
- `risk_on_high->fx_1h` score `0.2379` n `33` status `ready` deltaP `6.7139` edge `0.0034` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2379` n `33` status `ready` deltaP `6.7139` edge `0.0034` maxDD `-0.0796`
- `news_risk_high->commodity_1h` score `0.1476` n `51` status `ready` deltaP `8.0897` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1136` n `126` status `ready` deltaP `7.6365` edge `0.0088` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `-0.0765` n `51` status `ready` deltaP `2.9412` edge `-0.0071` maxDD `-0.1184`
- `market_context_high->commodity_24h` score `-0.0878` n `110` status `ready` deltaP `-1.2816` edge `0.091` maxDD `-2.5151`
- `risk_on_high->index_1h` score `-0.1308` n `33` status `ready` deltaP `-0.9164` edge `0.0075` maxDD `-0.1197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
