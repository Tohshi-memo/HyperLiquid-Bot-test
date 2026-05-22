# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T13:07:22.664647+00:00`
- Price records: `672`
- Market context records: `1529`
- Flow alert records: `6313`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8792`

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

- `market_context_high->metal_24h` score `13.462` n `169` status `ready` deltaP `23.533` edge `1.065` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7251` n `169` status `ready` deltaP `28.9541` edge `0.9857` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4608` n `169` status `ready` deltaP `28.3233` edge `0.7961` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8682` n `169` status `ready` deltaP `20.1882` edge `0.2964` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6337` n `169` status `ready` deltaP `13.4492` edge `0.3625` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8967` n `169` status `ready` deltaP `18.3349` edge `0.0574` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1243` n `194` status `ready` deltaP `3.6617` edge `0.0954` maxDD `-5.0894`
- `market_context_high->fx_1h` score `-0.5751` n `199` status `ready` deltaP `-1.096` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6224` n `199` status `ready` deltaP `-0.5296` edge `0.0261` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.6665` n `194` status `ready` deltaP `10.4114` edge `0.1771` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.7184` n `194` status `ready` deltaP `5.9828` edge `0.1389` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.7266` n `199` status `ready` deltaP `-0.3475` edge `0.0013` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7454` n `199` status `ready` deltaP `5.1478` edge `0.0037` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7572` n `199` status `ready` deltaP `-0.1241` edge `0.0009` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.9087` n `199` status `ready` deltaP `-1.7813` edge `0.017` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1273` n `199` status `ready` deltaP `-2.0905` edge `0.0051` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3729` n `194` status `ready` deltaP `9.852` edge `0.0891` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.5066` n `194` status `ready` deltaP `-5.6025` edge `0.0207` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.9052` n `194` status `ready` deltaP `-8.0509` edge `-0.0122` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-4.6085` n `169` status `ready` deltaP `-0.6708` edge `-0.1066` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
