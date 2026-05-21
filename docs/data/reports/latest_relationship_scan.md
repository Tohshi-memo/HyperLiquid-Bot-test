# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T15:52:25.084949+00:00`
- Price records: `672`
- Market context records: `1437`
- Flow alert records: `6050`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `12.2285` n `154` status `ready` deltaP `28.7811` edge `1.0288` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1059` n `154` status `ready` deltaP `13.5507` edge `1.0852` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6348` n `154` status `ready` deltaP `27.3539` edge `0.9004` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.0929` n `154` status `ready` deltaP `19.3813` edge `0.3205` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3903` n `154` status `ready` deltaP `12.5271` edge `0.4317` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2172` n `210` status `ready` deltaP `6.3342` edge `0.1422` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1694` n `154` status `ready` deltaP `10.0537` edge `0.052` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1371` n `222` status `ready` deltaP `2.1443` edge `0.0343` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2023` n `222` status `ready` deltaP `3.0372` edge `0.0094` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.5865` n `222` status `ready` deltaP `-0.1483` edge `0.0136` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.6669` n `222` status `ready` deltaP `1.814` edge `0.0347` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.7199` n `210` status `ready` deltaP `-0.6737` edge `0.0534` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.7282` n `222` status `ready` deltaP `0.7566` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.8804` n `222` status `ready` deltaP `4.2173` edge `-0.0074` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.0353` n `210` status `ready` deltaP `8.8168` edge `0.1869` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0586` n `210` status `ready` deltaP `-4.3438` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.2535` n `210` status `ready` deltaP `4.9695` edge `0.1333` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.6335` n `222` status `ready` deltaP `-0.8901` edge `0.0055` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7049` n `210` status `ready` deltaP `5.4472` edge `0.0143` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0541` n `210` status `ready` deltaP `-9.8664` edge `-0.0174` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
