# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T23:52:26.409756+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10807`

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

- `risk_on_high->unknown_4h` score `20.7877` n `133` status `ready` deltaP `-3.3055` edge `1.9549` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.7877` n `133` status `ready` deltaP `-3.3055` edge `1.9549` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.2285` n `228` status `ready` deltaP `1.5191` edge `0.9224` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `5.9817` n `37` status `ready` deltaP `24.8311` edge `0.3599` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9019` n `37` status `ready` deltaP `20.1389` edge `0.1909` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3045` n `37` status `ready` deltaP `16.4181` edge `0.2072` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.8363` n `153` status `ready` deltaP `15.1042` edge `0.4895` maxDD `-16.9737`
- `news_risk_high->metal_4h` score `2.3503` n `37` status `ready` deltaP `23.8464` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.5895` n `37` status `ready` deltaP `13.0847` edge `0.0843` maxDD `-0.7924`
- `risk_on_high->crypto_major_24h` score `1.5421` n `78` status `ready` deltaP `11.7922` edge `0.8517` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.5421` n `78` status `ready` deltaP `11.7922` edge `0.8517` maxDD `-47.9416`
- `news_risk_high->commodity_4h` score `1.5356` n `37` status `ready` deltaP `7.313` edge `0.0993` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1954` n `37` status `ready` deltaP `6.4655` edge `0.0748` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1754` n `37` status `ready` deltaP `14.7233` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `1.0155` n `37` status `ready` deltaP `20.9975` edge `0.0462` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8937` n `37` status `ready` deltaP `8.8769` edge `0.0418` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.1256` n `37` status `ready` deltaP `3.3496` edge `0.021` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `-0.0519` n `37` status `ready` deltaP `5.276` edge `0.0028` maxDD `-0.9036`
- `news_risk_high->crypto_major_24h` score `-0.0724` n `37` status `ready` deltaP `14.8414` edge `0.1694` maxDD `-18.2098`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
