# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T08:52:18.832570+00:00`
- Price records: `672`
- Market context records: `1204`
- Flow alert records: `5372`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.547` n `133` status `ready` deltaP `44.216` edge `1.364` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.4` n `133` status `ready` deltaP `22.05` edge `0.6713` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.9606` n `133` status `ready` deltaP `3.5359` edge `0.5948` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.4028` n `133` status `ready` deltaP `-3.7477` edge `0.5586` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.6439` n `133` status `ready` deltaP `-3.5675` edge `0.5877` maxDD `-15.8204`
- `market_context_high->equity_4h` score `2.7808` n `133` status `ready` deltaP `14.484` edge `0.2015` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1712` n `133` status `ready` deltaP `17.4251` edge `0.1734` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.7482` n `133` status `ready` deltaP `17.6574` edge `0.3391` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9162` n `133` status `ready` deltaP `10.2983` edge `0.076` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.4888` n `133` status `ready` deltaP `8.7497` edge `0.0532` maxDD `-2.3306`
- `market_context_high->index_1h` score `0.4877` n `133` status `ready` deltaP `8.4046` edge `0.0163` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3619` n `133` status `ready` deltaP `3.9034` edge `0.0419` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.143` n `133` status `ready` deltaP `6.117` edge `0.133` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1485` n `133` status `ready` deltaP `4.9041` edge `0.0005` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1631` n `133` status `ready` deltaP `8.8267` edge `-0.0114` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3695` n `133` status `ready` deltaP `3.3902` edge `0.0066` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3744` n `133` status `ready` deltaP `0.7024` edge `0.0316` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.7861` n `133` status `ready` deltaP `-2.3288` edge `0.0115` maxDD `-2.252`
- `market_context_high->unknown_24h` score `-0.8529` n `133` status `ready` deltaP `1.1239` edge `0.1944` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-0.9314` n `133` status `ready` deltaP `8.8174` edge `-0.0351` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
