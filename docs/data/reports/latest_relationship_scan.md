# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T17:22:29.393558+00:00`
- Price records: `672`
- Market context records: `5579`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11413`

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

- `market_context_high->equity_24h` score `4.1971` n `174` status `ready` deltaP `15.0084` edge `0.7576` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1994` n `194` status `ready` deltaP `11.3402` edge `0.2536` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.8673` n `174` status `ready` deltaP `17.6186` edge `0.0522` maxDD `-1.457`
- `market_context_high->crypto_major_24h` score `0.7374` n `174` status `ready` deltaP `13.4519` edge `0.4258` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `0.6177` n `194` status `ready` deltaP `6.8032` edge `0.1702` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5756` n `194` status `ready` deltaP `5.5695` edge `0.1747` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.2056` n `206` status `ready` deltaP `3.6161` edge `0.0081` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2777` n `206` status `ready` deltaP `5.8122` edge `0.0388` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.3364` n `194` status `ready` deltaP `5.4533` edge `0.009` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.5064` n `206` status `ready` deltaP `0.5581` edge `0.0009` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5181` n `206` status `ready` deltaP `0.0` edge `0.0011` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6087` n `206` status `ready` deltaP `0.8895` edge `0.0395` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7662` n `206` status `ready` deltaP `2.5042` edge `0.044` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.2089` n `206` status `ready` deltaP `-2.3545` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5201` n `194` status `ready` deltaP `2.7376` edge `0.016` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.0531` n `174` status `ready` deltaP `12.8652` edge `0.0497` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0672` n `194` status `ready` deltaP `-13.9757` edge `-0.0617` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.3568` n `194` status `ready` deltaP `-6.5564` edge `-0.0518` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9174` n `174` status `ready` deltaP `-8.1537` edge `-0.2246` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.2984` n `174` status `ready` deltaP `3.4124` edge `0.0721` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
