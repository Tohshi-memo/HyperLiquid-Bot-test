# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T05:22:27.400936+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2790`

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

- `market_context_high->unknown_1h` score `11992.0232` n `108` status `ready` deltaP `1.1367` edge `999.3475` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7452.2073` n `108` status `ready` deltaP `-0.0903` edge `621.0463` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `14.2116` n `101` status `ready` deltaP `31.4786` edge `1.3615` maxDD `-26.6313`
- `market_context_high->crypto_alt_24h` score `7.9213` n `101` status `ready` deltaP `17.4247` edge `1.103` maxDD `-40.3912`
- `market_context_high->crypto_major_4h` score `1.4428` n `108` status `ready` deltaP `4.3981` edge `0.3728` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2505` n `108` status `ready` deltaP `5.9225` edge `0.2723` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.8367` n `108` status `ready` deltaP `20.0034` edge `0.0708` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0391` n `108` status `ready` deltaP `6.1377` edge `0.0223` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2304` n `108` status `ready` deltaP `3.8645` edge `0.0059` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3178` n `108` status `ready` deltaP `4.5465` edge `0.0686` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.734` n `108` status `ready` deltaP `-1.7853` edge `0.04` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0811` n `108` status `ready` deltaP `6.792` edge `0.0425` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6217` n `108` status `ready` deltaP `-11.5491` edge `-0.0022` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8296` n `108` status `ready` deltaP `-2.2245` edge `-0.0033` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3762` n `108` status `ready` deltaP `-14.7979` edge `-0.0044` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4091` n `108` status `ready` deltaP `-9.6696` edge `-0.0281` maxDD `-3.9892`
- `market_context_high->metal_24h` score `-4.6471` n `101` status `ready` deltaP `14.824` edge `0.0854` maxDD `-35.719`
- `market_context_high->fx_24h` score `-6.5045` n `101` status `ready` deltaP `-16.5205` edge `-0.0046` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0968` n `108` status `ready` deltaP `-28.9577` edge `-0.1124` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3103` n `108` status `ready` deltaP `-6.8992` edge `-0.0477` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
