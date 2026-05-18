# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T20:52:22.464795+00:00`
- Price records: `672`
- Market context records: `1153`
- Flow alert records: `5223`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.1145` n `149` status `ready` deltaP `44.1904` edge `1.4948` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.7645` n `149` status `ready` deltaP `20.556` edge `0.8783` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.8776` n `149` status `ready` deltaP `20.0352` edge `0.6159` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.1911` n `149` status `ready` deltaP `18.6463` edge `0.4474` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.6968` n `149` status `ready` deltaP `-2.0321` edge `0.655` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5399` n `165` status `ready` deltaP `12.4177` edge `0.1952` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2063` n `165` status `ready` deltaP `9.5436` edge `0.1052` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5378` n `165` status `ready` deltaP `8.0566` edge `0.0228` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4657` n `165` status `ready` deltaP `3.8214` edge `0.0511` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.2756` n `165` status `ready` deltaP `9.3977` edge `0.1648` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1725` n `165` status `ready` deltaP `7.8969` edge `0.0383` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0944` n `165` status `ready` deltaP `7.926` edge `0.0006` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.227` n `165` status `ready` deltaP `3.3987` edge `0.0427` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.2345` n `165` status `ready` deltaP `6.9144` edge `-0.0046` maxDD `-2.2164`
- `market_context_high->fx_4h` score `-0.8846` n `165` status `ready` deltaP `-1.7045` edge `-0.0024` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.9192` n `165` status `ready` deltaP `6.4569` edge `0.1356` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-1.1541` n `165` status `ready` deltaP `-1.9788` edge `-0.0022` maxDD `-3.7959`
- `market_context_high->unknown_24h` score `-2.2396` n `149` status `ready` deltaP `4.43` edge `0.0568` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-2.4251` n `165` status `ready` deltaP `7.0519` edge `-0.0537` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.7852` n `165` status `ready` deltaP `8.4682` edge `-0.1669` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
