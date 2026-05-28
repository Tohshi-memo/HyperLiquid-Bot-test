# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T15:22:18.253154+00:00`
- Price records: `672`
- Market context records: `2153`
- Flow alert records: `8095`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6366` n `148` status `ready` deltaP `38.118` edge `0.9759` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.934` n `148` status `ready` deltaP `41.999` edge `0.7675` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.3157` n `148` status `ready` deltaP `24.8888` edge `0.4353` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.7056` n `148` status `ready` deltaP `25.9023` edge `0.3289` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.1369` n `37` status `ready` deltaP `30.3601` edge `0.3951` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.6319` n `148` status `ready` deltaP `14.1` edge `0.3315` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.4809` n `148` status `ready` deltaP `18.5386` edge `0.2142` maxDD `-1.817`
- `market_context_high->index_4h` score `3.3077` n `148` status `ready` deltaP `24.2254` edge `0.1825` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.2572` n `148` status `ready` deltaP `16.6653` edge `0.2467` maxDD `-4.9097`
- `market_context_high->metal_4h` score `2.9746` n `148` status `ready` deltaP `21.1395` edge `0.2457` maxDD `-4.7664`
- `market_context_high->equity_24h` score `2.9434` n `148` status `ready` deltaP `25.8493` edge `0.5628` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.8362` n `148` status `ready` deltaP `27.2991` edge `0.5864` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4878` n `37` status `ready` deltaP `31.456` edge `0.016` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1888` n `148` status `ready` deltaP `20.8193` edge `1.0004` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.0439` n `37` status `ready` deltaP `14.7537` edge `0.1078` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0219` n `43` status `ready` deltaP `18.8692` edge `0.0063` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8217` n `148` status `ready` deltaP `10.382` edge `0.0781` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.8079` n `43` status `ready` deltaP `10.7645` edge `0.0998` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.6475` n `148` status `ready` deltaP `9.5323` edge `0.0574` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
