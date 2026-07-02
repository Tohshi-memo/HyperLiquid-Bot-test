# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T09:39:22.639660+00:00`
- Price records: `672`
- Market context records: `5442`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->equity_24h` score `4.3431` n `185` status `ready` deltaP `11.8694` edge `0.6364` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `3.7173` n `185` status `ready` deltaP `18.2855` edge `0.6419` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.7008` n `196` status `ready` deltaP `16.6127` edge `0.4269` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.9825` n `196` status `ready` deltaP `13.5764` edge `0.3219` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.8746` n `196` status `ready` deltaP `11.6756` edge `0.3258` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5694` n `197` status `ready` deltaP `8.577` edge `0.0868` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2326` n `185` status `ready` deltaP `10.9975` edge `0.0356` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1518` n `197` status `ready` deltaP `6.7031` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2351` n `197` status `ready` deltaP `1.5099` edge `0.0665` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.3218` n `197` status `ready` deltaP `3.3907` edge `0.0181` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.3236` n `197` status `ready` deltaP `2.532` edge `0.0807` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5498` n `197` status `ready` deltaP `0.4293` edge `0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7347` n `196` status `ready` deltaP `8.1446` edge `0.0454` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0998` n `185` status `ready` deltaP `16.1627` edge `0.0992` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1722` n `196` status `ready` deltaP `0.2894` edge `0.0029` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4924` n `197` status `ready` deltaP `-3.4165` edge `-0.0068` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6774` n `196` status `ready` deltaP `-8.5802` edge `-0.0336` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3401` n `196` status `ready` deltaP `-7.4322` edge `-0.0483` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.9915` n `185` status `ready` deltaP `8.9978` edge `0.2271` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4627` n `185` status `ready` deltaP `-5.7742` edge `-0.1805` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
