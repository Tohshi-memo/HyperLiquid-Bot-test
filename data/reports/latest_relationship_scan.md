# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T13:07:30.827564+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->crypto_alt_24h` score `19.1618` n `59` status `ready` deltaP `43.9972` edge `1.4281` maxDD `-7.968`
- `risk_on_and_context->crypto_alt_24h` score `19.1618` n `59` status `ready` deltaP `43.9972` edge `1.4281` maxDD `-7.968`
- `risk_on_high->unknown_4h` score `8.1216` n `107` status `ready` deltaP `25.4032` edge `0.5691` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1216` n `107` status `ready` deltaP `25.4032` edge `0.5691` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5756` n `159` status `ready` deltaP `22.0998` edge `0.47` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `5.81` n `59` status `ready` deltaP `68.0467` edge `0.0528` maxDD `-0.4489`
- `risk_on_and_context->fx_24h` score `5.81` n `59` status `ready` deltaP `68.0467` edge `0.0528` maxDD `-0.4489`
- `risk_on_high->crypto_major_24h` score `5.5895` n `59` status `ready` deltaP `28.3545` edge `0.7639` maxDD `-15.2397`
- `risk_on_and_context->crypto_major_24h` score `5.5895` n `59` status `ready` deltaP `28.3545` edge `0.7639` maxDD `-15.2397`
- `market_context_high->crypto_major_24h` score `4.4765` n `101` status `ready` deltaP `21.3902` edge `0.4962` maxDD `-17.2607`
- `market_context_high->metal_24h` score `4.4175` n `101` status `ready` deltaP `33.182` edge `0.2297` maxDD `-1.9567`
- `market_context_high->crypto_alt_24h` score `4.1584` n `101` status `ready` deltaP `21.4934` edge `0.8088` maxDD `-27.517`
- `risk_on_high->unknown_1h` score `2.3771` n `107` status `ready` deltaP `6.3658` edge `0.2133` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.3771` n `107` status `ready` deltaP `6.3658` edge `0.2133` maxDD `-1.9453`
- `risk_on_high->metal_24h` score `2.1648` n `59` status `ready` deltaP `34.9105` edge `0.1222` maxDD `-1.8587`
- `risk_on_and_context->metal_24h` score `2.1648` n `59` status `ready` deltaP `34.9105` edge `0.1222` maxDD `-1.8587`
- `market_context_high->unknown_1h` score `2.1544` n `159` status `ready` deltaP `5.7075` edge `0.2045` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.4736` n `61` status `ready` deltaP `3.4701` edge `0.1343` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.1003` n `101` status `ready` deltaP `38.1927` edge `0.0323` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `0.6936` n `44` status `ready` deltaP `8.0808` edge `0.0666` maxDD `-1.1904`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
