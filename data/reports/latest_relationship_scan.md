# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T20:22:28.804389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11568`

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

- `risk_on_high->unknown_4h` score `7.8538` n `107` status `ready` deltaP `23.7264` edge `0.558` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8538` n `107` status `ready` deltaP `23.7264` edge `0.558` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3065` n `159` status `ready` deltaP `20.423` edge `0.4588` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.3287` n `107` status `ready` deltaP `6.2161` edge `0.2103` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.3287` n `107` status `ready` deltaP `6.2161` edge `0.2103` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.1049` n `159` status `ready` deltaP `5.5578` edge `0.2014` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `2.0178` n `87` status `ready` deltaP `14.1223` edge `0.1728` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `2.0178` n `87` status `ready` deltaP `14.1223` edge `0.1728` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.4231` n `61` status `ready` deltaP `3.3204` edge `0.1311` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.0915` n `87` status `ready` deltaP `43.0795` edge `0.0249` maxDD `-3.1066`
- `risk_on_and_context->fx_24h` score `1.0915` n `87` status `ready` deltaP `43.0795` edge `0.0249` maxDD `-3.1066`
- `risk_on_high->crypto_alt_24h` score `1.023` n `87` status `ready` deltaP `15.0862` edge `0.7003` maxDD `-42.2447`
- `risk_on_and_context->crypto_alt_24h` score `1.023` n `87` status `ready` deltaP `15.0862` edge `0.7003` maxDD `-42.2447`
- `market_context_high->fx_24h` score `0.2954` n `130` status `ready` deltaP `29.0919` edge `0.0195` maxDD `-3.773`
- `news_risk_high->commodity_4h` score `0.2186` n `61` status `ready` deltaP `6.8823` edge `0.0238` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2043` n `159` status `ready` deltaP `9.6298` edge `0.0178` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1463` n `61` status `ready` deltaP `10.6533` edge `0.0005` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.0177` n `107` status `ready` deltaP `5.9209` edge `0.015` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0177` n `107` status `ready` deltaP `5.9209` edge `0.015` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `-0.032` n `159` status `ready` deltaP `6.3565` edge `0.0447` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
