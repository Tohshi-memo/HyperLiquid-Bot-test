# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T23:37:24.990398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `48.8981` n `50` status `ready` deltaP `11.5717` edge `3.9977` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.4819` n `50` status `ready` deltaP `36.5872` edge `0.9237` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4069` n `50` status `ready` deltaP `26.1646` edge `0.8694` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `7.0614` n `50` status `ready` deltaP `31.323` edge `0.4734` maxDD `-4.8351`
- `news_risk_high->index_24h` score `3.7983` n `50` status `ready` deltaP `38.0864` edge `0.0778` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.65` n `50` status `ready` deltaP `42.9146` edge `0.0271` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2616` n `137` status `ready` deltaP `24.8653` edge `0.1467` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7014` n `50` status `ready` deltaP `15.3293` edge `0.1585` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.5865` n `50` status `ready` deltaP `35.3057` edge `-0.0156` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.3731` n `50` status `ready` deltaP `18.7066` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3348` n `137` status `ready` deltaP `12.7016` edge `0.0715` maxDD `-1.5954`
- `news_risk_high->equity_4h` score `1.3248` n `50` status `ready` deltaP `19.4451` edge `0.0575` maxDD `-2.1389`
- `news_risk_high->equity_1h` score `1.2836` n `50` status `ready` deltaP `17.2635` edge `0.0198` maxDD `-0.2338`
- `news_risk_high->commodity_1h` score `0.509` n `50` status `ready` deltaP `14.1497` edge `0.0022` maxDD `-0.5024`
- `market_context_high->unknown_24h` score `0.4136` n `133` status `ready` deltaP `5.5567` edge `0.0705` maxDD `-3.1794`
- `news_risk_high->index_1h` score `0.1038` n `50` status `ready` deltaP `6.9102` edge `0.0012` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0844` n `50` status `ready` deltaP `6.4756` edge `0.0036` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.061` n `50` status `ready` deltaP `4.8024` edge `-0.0016` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1011` n `50` status `ready` deltaP `7.7683` edge `-0.0071` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3866` n `137` status `ready` deltaP `3.6409` edge `-0.0006` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
