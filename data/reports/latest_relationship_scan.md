# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T15:22:29.405709+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2584.3152` n `139` status `ready` deltaP `1.2153` edge `215.3515` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6273` n `139` status `ready` deltaP `32.4141` edge `1.5647` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.2563` n `139` status `ready` deltaP `34.7896` edge `0.8784` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.2693` n `139` status `ready` deltaP `24.8938` edge `0.9666` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2395` n `139` status `ready` deltaP `39.0325` edge `0.1626` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8038` n `139` status `ready` deltaP `31.586` edge `0.2919` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7204` n `142` status `ready` deltaP `27.9801` edge `0.2011` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0957` n `142` status `ready` deltaP `8.7857` edge `0.2987` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7729` n `142` status `ready` deltaP `6.9706` edge `0.109` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5847` n `142` status `ready` deltaP `7.4028` edge `0.0655` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4538` n `142` status `ready` deltaP `8.4507` edge `0.0105` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0515` n `142` status `ready` deltaP `8.9875` edge `0.0297` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.358` n `142` status `ready` deltaP `2.4395` edge `0.0661` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5648` n `142` status `ready` deltaP `0.565` edge `0.0121` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.2945` n `142` status `ready` deltaP `9.2838` edge `-0.0065` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3335` n `142` status `ready` deltaP `-7.8495` edge `0.0308` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7402` n `142` status `ready` deltaP `-4.6827` edge `0.0796` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8325` n `142` status `ready` deltaP `-9.1444` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9219` n `142` status `ready` deltaP `-10.2028` edge `-0.0109` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3536` n `142` status `ready` deltaP `-9.6122` edge `0.0042` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
