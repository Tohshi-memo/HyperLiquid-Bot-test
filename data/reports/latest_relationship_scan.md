# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T15:22:15.082030+00:00`
- Price records: `672`
- Market context records: `1024`
- Flow alert records: `4858`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `13.8324` n `189` status `ready` deltaP `32.6626` edge `0.9938` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3946` n `189` status `ready` deltaP `11.208` edge `0.4149` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.0028` n `189` status `ready` deltaP `9.3897` edge `0.2415` maxDD `-5.9759`
- `market_context_high->index_24h` score `1.5406` n `189` status `ready` deltaP `8.7041` edge `0.1935` maxDD `-3.1847`
- `market_context_high->fx_1h` score `-0.1148` n `189` status `ready` deltaP `4.5386` edge `0.0006` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5917` n `189` status `ready` deltaP `1.7512` edge `0.0198` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5932` n `189` status `ready` deltaP `3.0542` edge `0.0082` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.624` n `189` status `ready` deltaP `0.339` edge `0.0214` maxDD `-4.3858`
- `market_context_high->fx_4h` score `-0.931` n `189` status `ready` deltaP `2.8294` edge `0.0032` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1668` n `189` status `ready` deltaP `4.8974` edge `-0.0213` maxDD `-10.8756`
- `market_context_high->crypto_alt_1h` score `-1.2422` n `189` status `ready` deltaP `-0.8815` edge `-0.0199` maxDD `-7.3447`
- `market_context_high->index_4h` score `-1.3493` n `189` status `ready` deltaP `0.2847` edge `0.0333` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.3751` n `189` status `ready` deltaP `1.9527` edge `0.0876` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.7561` n `189` status `ready` deltaP `0.6955` edge `-0.0395` maxDD `-8.5553`
- `market_context_high->crypto_alt_4h` score `-2.6876` n `189` status `ready` deltaP `0.7413` edge `0.0489` maxDD `-15.2248`
- `market_context_high->metal_24h` score `-2.8133` n `189` status `ready` deltaP `-7.5266` edge `0.3163` maxDD `-31.3787`
- `market_context_high->crypto_major_4h` score `-2.8302` n `189` status `ready` deltaP `7.4929` edge `0.0848` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2309` n `189` status `ready` deltaP `1.9972` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.4637` n `189` status `ready` deltaP `-3.7626` edge `0.0532` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.031` n `189` status `ready` deltaP `-1.6986` edge `-0.157` maxDD `-21.2115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
