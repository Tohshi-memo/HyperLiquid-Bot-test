# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T18:22:17.641054+00:00`
- Price records: `672`
- Market context records: `1655`
- Flow alert records: `6674`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.7198` n `169` status `ready` deltaP `28.5877` edge `0.862` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.2117` n `189` status `ready` deltaP `22.0193` edge `0.4706` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7875` n `169` status `ready` deltaP `20.5841` edge `0.3162` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.4347` n `189` status `ready` deltaP `18.0112` edge `0.3537` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.8032` n `189` status `ready` deltaP `12.2273` edge `0.1782` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7152` n `169` status `ready` deltaP `19.6013` edge `0.5021` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.7507` n `169` status `ready` deltaP `25.4008` edge `0.7518` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.5843` n `169` status `ready` deltaP `26.055` edge `1.0559` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.4662` n `200` status `ready` deltaP `6.1078` edge `0.1005` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2796` n `200` status `ready` deltaP `1.515` edge `0.0349` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.406` n `189` status `ready` deltaP `0.8915` edge `0.0509` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.4625` n `200` status `ready` deltaP `2.2036` edge `0.0534` maxDD `-5.5244`
- `market_context_high->fx_24h` score `-0.4822` n `169` status `ready` deltaP `6.214` edge `0.0233` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5007` n `200` status `ready` deltaP `-1.0838` edge `0.0062` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.5326` n `200` status `ready` deltaP `-0.2934` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.8018` n `200` status `ready` deltaP `3.8533` edge `0.0051` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8781` n `200` status `ready` deltaP `1.1527` edge `-0.0071` maxDD `-6.7191`
- `market_context_high->metal_4h` score `-1.3591` n `189` status `ready` deltaP `8.299` edge `0.1006` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.9933` n `189` status `ready` deltaP `-8.9875` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.6603` n `189` status `ready` deltaP `10.8285` edge `-0.1501` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
