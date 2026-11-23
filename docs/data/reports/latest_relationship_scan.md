# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T14:52:33.302140+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4470`

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

- `market_context_high->unknown_1h` score `27671.0819` n `52` status `ready` deltaP `0.4145` edge `2305.9369` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `18839.5085` n `52` status `ready` deltaP `4.0806` edge `1569.9457` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1277.2462` n `31` status `ready` deltaP `3.5783` edge `106.4309` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.5846` n `31` status `ready` deltaP `4.701` edge `91.6897` maxDD `-0.119`
- `news_risk_high->equity_24h` score `44.1813` n `31` status `ready` deltaP `48.6111` edge `3.3577` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.7809` n `31` status `ready` deltaP `48.6111` edge `2.741` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5696` n `31` status `ready` deltaP `48.7847` edge `2.3889` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.1563` n `31` status `ready` deltaP `49.2216` edge `0.7957` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.1218` n `31` status `ready` deltaP `22.1872` edge `0.7826` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.9087` n `31` status `ready` deltaP `32.3466` edge `0.6583` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.9012` n `31` status `ready` deltaP `46.875` edge `0.2626` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1473` n `31` status `ready` deltaP `51.7809` edge `0.1799` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.0877` n `31` status `ready` deltaP `11.5952` edge `0.8449` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2672` n `31` status `ready` deltaP `18.191` edge `0.1697` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2199` n `31` status `ready` deltaP `34.1759` edge `0.0665` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5728` n `31` status `ready` deltaP `30.6452` edge `0.0186` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1585` n `31` status `ready` deltaP `8.813` edge `0.2641` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.0245` n `52` status `ready` deltaP `26.6416` edge `0.0279` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `1.8202` n `31` status `ready` deltaP `7.7651` edge `0.2173` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4753` n `31` status `ready` deltaP `28.6845` edge `0.0258` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
