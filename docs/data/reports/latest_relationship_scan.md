# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T19:37:28.067539+00:00`
- Price records: `672`
- Market context records: `5279`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `25.4041` n `153` status `ready` deltaP `28.3803` edge `1.9368` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.532` n `153` status `ready` deltaP `25.7353` edge `0.8711` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.3312` n `173` status `ready` deltaP `16.6071` edge `0.4143` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.874` n `173` status `ready` deltaP `15.3876` edge `0.4495` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.7394` n `153` status `ready` deltaP `19.9653` edge `0.7414` maxDD `-40.0306`
- `market_context_high->equity_4h` score `0.9194` n `173` status `ready` deltaP `9.5825` edge `0.1766` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7018` n `173` status `ready` deltaP `14.175` edge `0.0662` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5721` n `153` status `ready` deltaP `13.3068` edge `0.0485` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5254` n `181` status `ready` deltaP `5.1808` edge `0.1054` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3108` n `181` status `ready` deltaP `6.0219` edge `0.1103` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2334` n `153` status `ready` deltaP `20.8231` edge `0.0546` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0857` n `181` status `ready` deltaP `6.9847` edge `0.0571` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.016` n `181` status `ready` deltaP `6.0757` edge `0.0112` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2903` n `173` status `ready` deltaP `7.1875` edge `0.0266` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.324` n `181` status `ready` deltaP `3.1776` edge `0.011` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3615` n `181` status `ready` deltaP `0.3904` edge `0.0` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7329` n `173` status `ready` deltaP `1.0583` edge `0.0019` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3735` n `181` status `ready` deltaP `-2.4862` edge `-0.0061` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6532` n `173` status `ready` deltaP `-2.8364` edge `0.0073` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.5245` n `181` status `ready` deltaP `6.3859` edge `-0.1888` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
