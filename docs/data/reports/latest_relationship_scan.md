# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T14:22:28.279859+00:00`
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

- `market_context_high->unknown_1h` score `26532.2006` n `54` status `ready` deltaP `-0.9315` edge `2211.0391` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `18005.6555` n `54` status `ready` deltaP `4.2231` edge `1500.457` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1286.6662` n `31` status `ready` deltaP `3.728` edge `107.2149` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.9734` n `31` status `ready` deltaP `4.701` edge `91.7221` maxDD `-0.119`
- `news_risk_high->equity_24h` score `44.5139` n `31` status `ready` deltaP `48.9583` edge `3.3831` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9369` n `31` status `ready` deltaP `48.6111` edge `2.754` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6848` n `31` status `ready` deltaP `48.7847` edge `2.3985` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.2285` n `31` status `ready` deltaP `49.5688` edge `0.7994` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.2298` n `31` status `ready` deltaP `22.1872` edge `0.7916` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.1215` n `31` status `ready` deltaP `32.6515` edge `0.674` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.9578` n `31` status `ready` deltaP `47.2222` edge `0.265` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1787` n `31` status `ready` deltaP `52.1282` edge `0.1802` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1758` n `31` status `ready` deltaP `11.5952` edge `0.8562` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.488` n `31` status `ready` deltaP `18.4904` edge `0.1861` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2635` n `31` status `ready` deltaP `34.4808` edge `0.0681` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6183` n `31` status `ready` deltaP `30.9446` edge `0.0204` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2716` n `31` status `ready` deltaP `8.9627` edge `0.2776` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9177` n `31` status `ready` deltaP `7.9148` edge `0.2288` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.6731` n `54` status `ready` deltaP `24.0063` edge `0.0251` maxDD `-0.3242`
- `news_risk_high->metal_1h` score `1.5103` n `31` status `ready` deltaP `28.9839` edge `0.0283` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
