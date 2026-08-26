# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T23:07:27.090721+00:00`
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

- `news_risk_high->unknown_24h` score `48.8309` n `50` status `ready` deltaP `11.5717` edge `3.9921` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.3583` n `50` status `ready` deltaP `36.5872` edge `0.9134` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4261` n `50` status `ready` deltaP `26.1646` edge `0.871` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `7.197` n `50` status `ready` deltaP `31.6684` edge `0.4824` maxDD `-4.8351`
- `news_risk_high->index_24h` score `3.8451` n `50` status `ready` deltaP `38.4318` edge `0.0794` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.622` n `50` status `ready` deltaP `42.6098` edge `0.0268` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2808` n `137` status `ready` deltaP `24.8653` edge `0.1483` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7314` n `50` status `ready` deltaP `15.6287` edge `0.159` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.5432` n `50` status `ready` deltaP `34.9603` edge `-0.0169` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.3836` n `50` status `ready` deltaP `19.4451` edge `0.0624` maxDD `-2.1389`
- `news_risk_high->fx_1h` score `1.3731` n `50` status `ready` deltaP `18.7066` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3648` n `137` status `ready` deltaP `13.001` edge `0.072` maxDD `-1.5954`
- `news_risk_high->equity_1h` score `1.2812` n `50` status `ready` deltaP `17.2635` edge `0.0196` maxDD `-0.2338`
- `news_risk_high->commodity_1h` score `0.5082` n `50` status `ready` deltaP `14.1497` edge `0.0021` maxDD `-0.5024`
- `market_context_high->unknown_24h` score `0.3464` n `133` status `ready` deltaP `5.5567` edge `0.0649` maxDD `-3.1794`
- `news_risk_high->index_1h` score `0.103` n `50` status `ready` deltaP `6.9102` edge `0.0011` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0916` n `50` status `ready` deltaP `6.4756` edge `0.0042` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0703` n `50` status `ready` deltaP `4.9521` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0647` n `50` status `ready` deltaP `8.0732` edge `-0.0061` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3866` n `137` status `ready` deltaP `3.6409` edge `-0.0006` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
