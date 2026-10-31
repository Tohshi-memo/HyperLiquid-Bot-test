# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T13:22:22.542403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2401.3941` n `110` status `ready` deltaP `-7.642` edge `200.2101` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `90.3683` n `99` status `ready` deltaP `-5.7567` edge `7.5977` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `63.4426` n `110` status `ready` deltaP `1.1059` edge `5.2928` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.221` n `47` status `ready` deltaP `45.5711` edge `1.1364` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.8942` n `110` status `ready` deltaP `27.0991` edge `1.0029` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.699` n `110` status `ready` deltaP `42.3895` edge `0.1273` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.687` n `98` status `ready` deltaP `17.4185` edge `0.4131` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.6834` n `110` status `ready` deltaP `21.2361` edge `0.0412` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.0928` n `110` status `ready` deltaP `6.5105` edge `0.187` maxDD `-4.48`
- `news_risk_high->crypto_alt_1h` score `0.6816` n `99` status `ready` deltaP `6.791` edge `0.0986` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5701` n `110` status `ready` deltaP `12.8552` edge `0.0164` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.5159` n `110` status `ready` deltaP `6.0533` edge `0.0902` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3913` n `110` status `ready` deltaP `9.1018` edge `0.0747` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.1945` n `110` status `ready` deltaP `6.5351` edge `-0.0006` maxDD `-0.1407`
- `market_context_high->metal_24h` score `0.1187` n `110` status `ready` deltaP `13.5322` edge `0.1897` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `-0.0101` n `110` status `ready` deltaP `10.3325` edge `0.0517` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.0814` n `110` status `ready` deltaP `4.9861` edge `-0.0006` maxDD `-0.1537`
- `market_context_high->crypto_major_4h` score `-0.1978` n `110` status `ready` deltaP `15.8897` edge `0.1516` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.3963` n `110` status `ready` deltaP `3.1982` edge `0.0015` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4778` n `110` status `ready` deltaP `-0.343` edge `0.0139` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
