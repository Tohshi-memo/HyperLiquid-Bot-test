# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T17:52:44.012994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10692`

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

- `news_risk_high->unknown_4h` score `394.9836` n `78` status `ready` deltaP `-22.1505` edge `33.1523` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.9463` n `78` status `ready` deltaP `46.9017` edge `1.5553` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.2041` n `78` status `ready` deltaP `34.1747` edge `1.3529` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.3034` n `78` status `ready` deltaP `39.7836` edge `1.0214` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7075` n `78` status `ready` deltaP `61.9391` edge `0.3303` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.7387` n `115` status `ready` deltaP `37.6736` edge `0.3104` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3701` n `78` status `ready` deltaP `37.7938` edge `0.3243` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0571` n `51` status `ready` deltaP `37.6736` edge `0.2536` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0571` n `51` status `ready` deltaP `37.6736` edge `0.2536` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.6784` n `51` status `ready` deltaP `52.3795` edge `0.0449` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.6784` n `51` status `ready` deltaP `52.3795` edge `0.0449` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.2805` n `115` status `ready` deltaP `49.1229` edge `0.0508` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9919` n `52` status `ready` deltaP `26.2899` edge `0.0257` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9919` n `52` status `ready` deltaP `26.2899` edge `0.0257` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7922` n `137` status `ready` deltaP `21.6998` edge `0.0465` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7766` n `137` status `ready` deltaP `12.812` edge `0.017` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6446` n `78` status `ready` deltaP `15.8966` edge `0.0395` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2612` n `52` status `ready` deltaP `7.1972` edge `0.009` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2612` n `52` status `ready` deltaP `7.1972` edge `0.009` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2194` n `137` status `ready` deltaP `10.1589` edge `0.008` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
