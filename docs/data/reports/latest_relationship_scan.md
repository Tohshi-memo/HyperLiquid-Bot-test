# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T09:52:24.302908+00:00`
- Price records: `672`
- Market context records: `6907`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `0.1555` n `191` status `ready` deltaP `-5.0314` edge `0.4519` maxDD `-14.2075`
- `market_context_high->fx_1h` score `-0.1778` n `224` status `ready` deltaP `3.4351` edge `0.0028` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3743` n `224` status `ready` deltaP `3.109` edge `0.0245` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4519` n `224` status `ready` deltaP `4.5953` edge `0.0221` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6003` n `224` status `ready` deltaP `-0.5988` edge `-0.0045` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7402` n `224` status `ready` deltaP `15.2222` edge `0.01` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7658` n `224` status `ready` deltaP `-0.7298` edge `-0.0022` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8378` n `224` status `ready` deltaP `-3.8441` edge `-0.005` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3151` n `224` status `ready` deltaP `-1.5789` edge `-0.0091` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5666` n `224` status `ready` deltaP `-2.9619` edge `-0.0207` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7411` n `224` status `ready` deltaP `2.2348` edge `-0.0201` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9045` n `224` status `ready` deltaP `5.1612` edge `-0.0206` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1661` n `224` status `ready` deltaP `2.7766` edge `0.0021` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.3921` n `191` status `ready` deltaP `-0.4383` edge `-0.0096` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.7316` n `224` status `ready` deltaP `2.2104` edge `-0.0066` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8275` n `224` status `ready` deltaP `-0.0871` edge `-0.0292` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0059` n `224` status `ready` deltaP `-7.9704` edge `0.0392` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1498` n `191` status `ready` deltaP `-5.4434` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1279` n `224` status `ready` deltaP `2.5588` edge `-0.1364` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3262` n `191` status `ready` deltaP `-13.2968` edge `-0.1196` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
