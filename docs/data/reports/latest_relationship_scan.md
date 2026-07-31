# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T12:22:36.621154+00:00`
- Price records: `672`
- Market context records: `8514`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6277.1901` n `52` status `ready` deltaP `44.7383` edge `522.843` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.595` n `64` status `ready` deltaP `21.1128` edge `0.3852` maxDD `-3.4427`
- `market_context_high->equity_4h` score `4.7953` n `30` status `ready` deltaP `36.3211` edge `0.1669` maxDD `-0.4211`
- `news_risk_high->index_4h` score `1.9855` n `64` status `ready` deltaP `16.5015` edge `0.0745` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7446` n `64` status `ready` deltaP `15.9525` edge `0.0867` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5919` n `30` status `ready` deltaP `15.1626` edge `0.1597` maxDD `-3.2023`
- `market_context_high->crypto_major_4h` score `1.5816` n `30` status `ready` deltaP `11.3516` edge `0.1862` maxDD `-2.395`
- `market_context_high->index_4h` score `1.0493` n `30` status `ready` deltaP `13.2723` edge `0.0177` maxDD `-0.1659`
- `news_risk_high->crypto_major_4h` score `0.8666` n `64` status `ready` deltaP `5.8308` edge `0.1498` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7983` n `64` status `ready` deltaP `14.3293` edge `0.146` maxDD `-5.8012`
- `market_context_high->metal_4h` score `0.709` n `30` status `ready` deltaP `20.2643` edge `-0.0023` maxDD `-1.0186`
- `news_risk_high->crypto_alt_1h` score `0.5864` n `64` status `ready` deltaP `9.4592` edge `0.0648` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3485` n `64` status `ready` deltaP `6.7646` edge `0.0508` maxDD `-2.0972`
- `market_context_high->commodity_1h` score `0.2342` n `42` status `ready` deltaP `11.3202` edge `0.0171` maxDD `-2.0038`
- `news_risk_high->fx_1h` score `0.0932` n `64` status `ready` deltaP `5.436` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0566` n `64` status `ready` deltaP `4.5191` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.005` n `64` status `ready` deltaP `11.1662` edge `0.0209` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0453` n `64` status `ready` deltaP `1.4101` edge `0.0324` maxDD `-0.8085`
- `market_context_high->equity_1h` score `-0.0843` n `42` status `ready` deltaP `-0.3421` edge `0.0244` maxDD `-0.9985`
- `news_risk_high->metal_1h` score `-0.1143` n `64` status `ready` deltaP `3.4057` edge `0.0081` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
