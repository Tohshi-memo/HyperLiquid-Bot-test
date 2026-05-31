# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T17:07:19.348962+00:00`
- Price records: `672`
- Market context records: `2477`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `market_context_high->unknown_24h` score `5.2653` n `121` status `ready` deltaP `20.3398` edge `0.336` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.1593` n `136` status `ready` deltaP `21.0455` edge `0.4742` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9191` n `136` status `ready` deltaP `18.3285` edge `0.3854` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.9903` n `121` status `ready` deltaP `11.2546` edge `0.5694` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.5939` n `136` status `ready` deltaP `10.1507` edge `0.1672` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.5386` n `140` status `ready` deltaP `7.7545` edge `0.1126` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.3812` n `140` status `ready` deltaP `6.0607` edge `0.1101` maxDD `-6.1656`
- `market_context_high->index_24h` score `-0.018` n `121` status `ready` deltaP `3.6716` edge `0.0721` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1985` n `136` status `ready` deltaP `5.6402` edge `0.0211` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2321` n `121` status `ready` deltaP `18.0685` edge `0.0129` maxDD `-6.8828`
- `market_context_high->crypto_alt_24h` score `-0.2591` n `121` status `ready` deltaP `0.934` edge `0.6563` maxDD `-43.6595`
- `market_context_high->fx_1h` score `-0.3604` n `140` status `ready` deltaP `0.4149` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.3753` n `140` status `ready` deltaP `1.9932` edge `0.0274` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.4909` n `140` status `ready` deltaP `0.9324` edge `0.0068` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.6253` n `140` status `ready` deltaP `1.5098` edge `-0.0024` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6461` n `136` status `ready` deltaP `-0.7891` edge `0.0084` maxDD `-0.8774`
- `market_context_high->index_1h` score `-0.6807` n `140` status `ready` deltaP `-1.3687` edge `0.0018` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.8572` n `121` status `ready` deltaP `3.6631` edge `0.0042` maxDD `-2.7484`
- `market_context_high->equity_1h` score `-0.9012` n `140` status `ready` deltaP `-0.6971` edge `0.0134` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.938` n `136` status `ready` deltaP `3.2819` edge `0.0387` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
