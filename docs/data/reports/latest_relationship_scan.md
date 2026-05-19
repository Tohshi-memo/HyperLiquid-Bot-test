# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T16:07:20.359844+00:00`
- Price records: `672`
- Market context records: `1235`
- Flow alert records: `5461`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8788`

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

- `market_context_high->crypto_major_24h` score `18.7964` n `128` status `ready` deltaP `44.184` edge `1.385` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.9337` n `128` status `ready` deltaP `4.154` edge `0.7551` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.7437` n `128` status `ready` deltaP `22.6562` edge `0.6959` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.6159` n `128` status `ready` deltaP `-0.1736` edge `0.7192` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.4211` n `128` status `ready` deltaP `-6.0764` edge `0.5571` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.5419` n `128` status `ready` deltaP `22.0486` edge `0.2568` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.5036` n `128` status `ready` deltaP `17.5495` edge `0.2413` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.1213` n `128` status `ready` deltaP `22.2222` edge `0.4847` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.5935` n `128` status `ready` deltaP `13.7385` edge `0.1095` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.3431` n `128` status `ready` deltaP `0.8681` edge `0.3791` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.7332` n `128` status `ready` deltaP `10.1984` edge `0.0248` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6362` n `128` status `ready` deltaP `5.4593` edge `0.0535` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.4796` n `128` status `ready` deltaP `6.8577` edge `0.0407` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1514` n `128` status `ready` deltaP `10.2685` edge `0.0052` maxDD `-2.2164`
- `market_context_high->metal_4h` score `-0.0487` n `128` status `ready` deltaP `14.6914` edge `0.0411` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.0641` n `128` status `ready` deltaP `6.0489` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0746` n `128` status `ready` deltaP `6.3072` edge `0.1405` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3211` n `128` status `ready` deltaP `0.6456` edge `0.0388` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4494` n `128` status `ready` deltaP `1.9274` edge `0.0061` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.772` n `128` status `ready` deltaP `7.4885` edge `0.1476` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
