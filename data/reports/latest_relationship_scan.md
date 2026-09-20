# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T15:37:28.761176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9386`

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

- `news_risk_high->crypto_major_24h` score `22.6255` n `98` status `ready` deltaP `8.6239` edge `2.5138` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2309` n `98` status `ready` deltaP `14.7463` edge `2.0757` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `11.344` n `52` status `ready` deltaP `0.6332` edge `0.9561` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9765` n `101` status `ready` deltaP `23.1873` edge `0.4644` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5212` n `101` status `ready` deltaP `21.9678` edge `0.3561` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3793` n `52` status `ready` deltaP `37.0895` edge `0.131` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `4.207` n `41` status `ready` deltaP `24.9154` edge `0.237` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `3.0485` n `101` status `ready` deltaP `16.6805` edge `0.1894` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2475` n `101` status `ready` deltaP `18.4769` edge `0.1164` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.0608` n `52` status `ready` deltaP `27.0521` edge `0.0129` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.8281` n `41` status `ready` deltaP `19.9568` edge `0.0235` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.5158` n `52` status `ready` deltaP `17.135` edge `0.0396` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0721` n `98` status `ready` deltaP `22.775` edge `0.1162` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8831` n `52` status `ready` deltaP `12.667` edge `0.0066` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.7152` n `101` status `ready` deltaP `18.1659` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6293` n `101` status `ready` deltaP `14.598` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.6149` n `98` status `ready` deltaP `16.571` edge `0.0817` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3458` n `52` status `ready` deltaP `8.8669` edge `0.0076` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2297` n `98` status `ready` deltaP `15.5046` edge `0.0105` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2245` n `101` status `ready` deltaP `5.2143` edge `0.0245` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
