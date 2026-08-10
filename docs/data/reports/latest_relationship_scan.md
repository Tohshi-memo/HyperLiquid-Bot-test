# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T14:22:42.712114+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `0.9208` n `169` status `ready` deltaP `12.2988` edge `0.0662` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7395` n `136` status `ready` deltaP `18.7634` edge `0.0173` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7221` n `171` status `ready` deltaP `9.7008` edge `0.0298` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.2732` n `136` status `ready` deltaP `2.9029` edge `0.3168` maxDD `-21.0709`
- `market_context_high->fx_4h` score `0.0282` n `169` status `ready` deltaP `8.0143` edge `0.0089` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0897` n `171` status `ready` deltaP `4.9287` edge `0.0008` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.4312` n `136` status `ready` deltaP `2.866` edge `0.0981` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7164` n `171` status `ready` deltaP `-1.574` edge `-0.0015` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7783` n `171` status `ready` deltaP `-4.0769` edge `-0.009` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-0.9049` n `136` status `ready` deltaP `0.172` edge `0.0516` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1657` n `171` status `ready` deltaP `-1.279` edge `-0.0021` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2157` n `169` status `ready` deltaP `-1.8843` edge `-0.0105` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.6173` n `171` status `ready` deltaP `-9.5598` edge `-0.0415` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9328` n `169` status `ready` deltaP `-6.0002` edge `-0.0314` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2612` n `169` status `ready` deltaP `-11.4059` edge `-0.1304` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6753` n `171` status `ready` deltaP `-10.8887` edge `-0.0603` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-4.0083` n `136` status `ready` deltaP `-0.8104` edge `-0.0792` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.0092` n `169` status `ready` deltaP `-12.6073` edge `-0.1542` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.2743` n `136` status `ready` deltaP `-11.9075` edge `-0.1325` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-8.6665` n `136` status `ready` deltaP `-5.3752` edge `-0.2037` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
