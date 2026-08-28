# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T10:07:29.509430+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.3245` n `50` status `ready` deltaP `11.6118` edge `4.3663` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.3764` n `50` status `ready` deltaP `39.3276` edge `2.3133` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.859` n `50` status `ready` deltaP `26.0122` edge `0.9081` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4559` n `50` status `ready` deltaP `30.1005` edge `0.3468` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.0577` n `50` status `ready` deltaP `47.5667` edge `0.1086` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9869` n `50` status `ready` deltaP `46.4207` edge `0.0318` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.605` n `133` status `ready` deltaP `5.5968` edge `0.253` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.5667` n `50` status `ready` deltaP `28.9012` edge `0.0363` maxDD `-0.2064`
- `news_risk_high->crypto_major_24h` score `2.4804` n `50` status `ready` deltaP `19.0087` edge `0.1293` maxDD `-2.6128`
- `market_context_high->unknown_4h` score `2.4522` n `144` status `ready` deltaP `18.8178` edge `0.1196` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.3195` n `54` status `ready` deltaP `13.0516` edge `0.1419` maxDD `-0.8495`
- `news_risk_high->equity_4h` score `1.8545` n `50` status `ready` deltaP `24.3232` edge `0.0687` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.5158` n `54` status `ready` deltaP `20.3704` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0356` n `54` status `ready` deltaP `14.6263` edge `0.0193` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9177` n `144` status `ready` deltaP `8.6535` edge `0.0638` maxDD `-1.6015`
- `market_context_high->metal_24h` score `0.8913` n `133` status `ready` deltaP `16.484` edge `0.1038` maxDD `-3.1535`
- `news_risk_high->commodity_1h` score `0.4043` n `54` status `ready` deltaP `12.3087` edge `0.0018` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.256` n `54` status `ready` deltaP `6.0047` edge `0.0039` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.2206` n `50` status `ready` deltaP `10.6646` edge `0.0004` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1346` n `50` status `ready` deltaP `7.3902` edge `0.0016` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
