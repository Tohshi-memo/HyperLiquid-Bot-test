# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T17:22:15.411220+00:00`
- Price records: `672`
- Market context records: `1650`
- Flow alert records: `6661`
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

- `market_context_high->metal_24h` score `9.3944` n `169` status `ready` deltaP `27.8957` edge `0.8395` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.0295` n `186` status `ready` deltaP `21.6011` edge `0.4582` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.683` n `169` status `ready` deltaP `19.8921` edge `0.3121` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.3112` n `186` status `ready` deltaP `17.5333` edge `0.3466` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.7133` n `186` status `ready` deltaP `11.7494` edge `0.1739` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5542` n `169` status `ready` deltaP `18.9093` edge `0.4933` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.3845` n `169` status `ready` deltaP `24.7087` edge `0.7259` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.3577` n `196` status `ready` deltaP `5.4412` edge `0.0959` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.1965` n `169` status `ready` deltaP `25.3629` edge `1.0282` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.3099` n `196` status `ready` deltaP `1.0388` edge `0.0342` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.443` n `186` status `ready` deltaP `0.2258` edge `0.0506` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4951` n `196` status `ready` deltaP `0.4277` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.5062` n `169` status `ready` deltaP `6.214` edge `0.0213` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5097` n `196` status `ready` deltaP `-1.2403` edge `0.0061` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.5176` n `196` status `ready` deltaP `1.6253` edge `0.0502` maxDD `-5.5244`
- `market_context_high->metal_1h` score `-0.8545` n `196` status `ready` deltaP `2.9451` edge `0.0044` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8567` n `196` status `ready` deltaP `1.5031` edge `-0.0067` maxDD `-6.7191`
- `market_context_high->metal_4h` score `-1.4447` n `186` status `ready` deltaP `7.5736` edge `0.0983` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0636` n `186` status `ready` deltaP `-9.8664` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.1057` n `186` status `ready` deltaP `10.6962` edge `-0.103` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
