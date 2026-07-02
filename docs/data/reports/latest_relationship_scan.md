# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T08:37:30.332378+00:00`
- Price records: `672`
- Market context records: `5437`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->equity_24h` score `4.5207` n `185` status `ready` deltaP `11.8694` edge `0.6512` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `4.0861` n `185` status `ready` deltaP `18.9799` edge `0.668` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7766` n `196` status `ready` deltaP `16.7652` edge `0.4322` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9566` n `196` status `ready` deltaP `11.9805` edge `0.3306` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.9088` n `196` status `ready` deltaP `13.1191` edge `0.3188` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.585` n `197` status `ready` deltaP `8.577` edge `0.0881` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1769` n `197` status `ready` deltaP `7.0025` edge `0.0174` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1698` n `185` status `ready` deltaP `10.3031` edge `0.035` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1536` n `197` status `ready` deltaP `2.1087` edge `0.0693` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2265` n `197` status `ready` deltaP `3.1308` edge `0.0848` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2894` n `197` status `ready` deltaP `3.6901` edge `0.0188` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5366` n `197` status `ready` deltaP `0.579` edge `0.0003` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7991` n `196` status `ready` deltaP `7.5348` edge `0.0441` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0686` n `185` status `ready` deltaP `16.1627` edge `0.1018` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1758` n `196` status `ready` deltaP `0.2894` edge `0.0026` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.5367` n `197` status `ready` deltaP `-3.8656` edge `-0.0075` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6922` n `196` status `ready` deltaP `-8.5802` edge `-0.0355` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4057` n `196` status `ready` deltaP `-8.0419` edge `-0.0497` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.6096` n `185` status `ready` deltaP `9.6922` edge `0.2543` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4253` n `185` status `ready` deltaP `-5.7742` edge `-0.1757` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
