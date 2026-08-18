# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T18:07:55.388520+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `market_context_high->crypto_major_24h` score `2.6481` n `91` status `ready` deltaP `10.0294` edge `0.2746` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6983` n `91` status `ready` deltaP `19.4636` edge `0.2713` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1944` n `96` status `ready` deltaP `9.9115` edge `0.0636` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7703` n `96` status `ready` deltaP `14.126` edge `0.0276` maxDD `-1.273`
- `market_context_high->equity_4h` score `0.6529` n `96` status `ready` deltaP `4.5985` edge `0.1126` maxDD `-2.4411`
- `market_context_high->index_1h` score `0.6456` n `96` status `ready` deltaP `12.6185` edge `0.0084` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.4622` n `96` status `ready` deltaP `7.9522` edge `0.0876` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4387` n `96` status `ready` deltaP `9.2066` edge `-0.0021` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `-0.0156` n `96` status `ready` deltaP `8.3841` edge `0.0698` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0321` n `96` status `ready` deltaP `4.0232` edge `0.0092` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.1558` n `91` status `ready` deltaP `12.914` edge `-0.0777` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.202` n `96` status `ready` deltaP `3.6839` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.4035` n `96` status `ready` deltaP `3.4807` edge `0.0101` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4751` n `96` status `ready` deltaP `1.4783` edge `0.0094` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.5365` n `96` status `ready` deltaP `1.0924` edge `0.0135` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.545` n `96` status `ready` deltaP `0.736` edge `0.0097` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8471` n `96` status `ready` deltaP `-6.9923` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2709` n `91` status `ready` deltaP `-6.6277` edge `0.0301` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.4272` n `91` status `ready` deltaP `-28.602` edge `-0.0283` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
