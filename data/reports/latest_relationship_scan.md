# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T15:22:32.234330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11022`

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

- `news_risk_high->unknown_4h` score `395.296` n `78` status `ready` deltaP `-20.931` edge `33.1702` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7156` n `78` status `ready` deltaP `46.2073` edge `1.5407` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.5512` n `78` status `ready` deltaP `34.8691` edge `1.3772` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.9221` n `78` status `ready` deltaP `38.0475` edge `1.0012` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6684` n `78` status `ready` deltaP `61.7655` edge `0.3282` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1128` n `107` status `ready` deltaP `39.4097` edge `0.33` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.34` n `47` status `ready` deltaP `39.4097` edge `0.2656` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.34` n `47` status `ready` deltaP `39.4097` edge `0.2656` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.2847` n `78` status `ready` deltaP `37.4466` edge `0.3195` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.8255` n `47` status `ready` deltaP `53.9487` edge `0.0467` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8255` n `47` status `ready` deltaP `53.9487` edge `0.0467` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4038` n `107` status `ready` deltaP `50.4689` edge `0.0521` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9205` n `52` status `ready` deltaP `25.8325` edge `0.0228` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9205` n `52` status `ready` deltaP `25.8325` edge `0.0228` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7208` n `137` status `ready` deltaP `21.2424` edge `0.0436` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7394` n `137` status `ready` deltaP `12.5126` edge `0.0159` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6532` n `78` status `ready` deltaP `15.8966` edge `0.0406` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.224` n `52` status `ready` deltaP `6.8978` edge `0.0079` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.224` n `52` status `ready` deltaP `6.8978` edge `0.0079` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2194` n `137` status `ready` deltaP `10.1589` edge `0.008` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
