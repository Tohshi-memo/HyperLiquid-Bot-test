# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T20:37:31.153485+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10648`

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

- `news_risk_high->crypto_major_24h` score `24.1513` n `98` status `ready` deltaP `12.0961` edge `2.6178` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.4106` n `98` status `ready` deltaP `15.2671` edge `2.0872` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `10.6768` n `44` status `ready` deltaP `-0.4158` edge `0.9075` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.768` n `101` status `ready` deltaP `21.2056` edge `0.3769` maxDD `-7.675`
- `market_context_high->commodity_4h` score `3.8672` n `44` status `ready` deltaP `36.0587` edge `0.0952` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `3.7873` n `101` status `ready` deltaP `20.4434` edge `0.3051` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9045` n `101` status `ready` deltaP `16.8302` edge `0.1764` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2031` n `101` status `ready` deltaP `18.7763` edge `0.1107` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.3876` n `44` status `ready` deltaP `20.122` edge `0.0079` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.0292` n `98` status `ready` deltaP `22.775` edge `0.1107` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8817` n `55` status `ready` deltaP `12.9314` edge `0.0052` maxDD `-0.1012`
- `market_context_high->commodity_1h` score `0.6672` n `55` status `ready` deltaP `11.9897` edge `0.0331` maxDD `-0.1998`
- `news_risk_high->metal_1h` score `0.6305` n `101` status `ready` deltaP `14.598` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.613` n `101` status `ready` deltaP `17.0988` edge `0.0425` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.4882` n `98` status `ready` deltaP `16.3974` edge `0.0723` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.2316` n `101` status `ready` deltaP `5.364` edge `0.0241` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.1883` n `101` status `ready` deltaP `8.4883` edge `0.0227` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.1144` n `98` status `ready` deltaP `14.9837` edge `-0.0008` maxDD `-2.4203`
- `market_context_high->metal_1h` score `0.0959` n `55` status `ready` deltaP `5.6151` edge `0.0054` maxDD `-0.4538`
- `news_risk_high->fx_1h` score `-0.2915` n `101` status `ready` deltaP `2.0943` edge `0.0061` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
