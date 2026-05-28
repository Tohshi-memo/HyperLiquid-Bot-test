# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T04:36:00.984865+00:00`
- Price records: `672`
- Market context records: `2108`
- Flow alert records: `7963`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `11.269` n `173` status `ready` deltaP `32.2078` edge `0.8305` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.8395` n `173` status `ready` deltaP `38.5027` edge `0.6996` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.8932` n `173` status `ready` deltaP `24.0774` edge `0.4055` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.3026` n `173` status `ready` deltaP `22.9346` edge `0.3151` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5869` n `173` status `ready` deltaP `19.1298` edge `0.1564` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.4755` n `172` status `ready` deltaP `11.99` edge `0.2492` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.3365` n `173` status `ready` deltaP `16.1287` edge `0.1858` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.1413` n `173` status `ready` deltaP `12.7064` edge `0.2051` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.0664` n `172` status `ready` deltaP `23.4509` edge `0.5479` maxDD `-35.8966`
- `market_context_high->metal_4h` score `1.9277` n `173` status `ready` deltaP `17.4265` edge `0.2089` maxDD `-6.8217`
- `market_context_high->equity_24h` score `1.7239` n `172` status `ready` deltaP `23.2498` edge `0.4785` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8739` n `173` status `ready` deltaP `10.7646` edge `0.0799` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.5108` n `172` status `ready` deltaP `21.1576` edge `0.7601` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.1495` n `173` status `ready` deltaP `5.924` edge `0.032` maxDD `-1.3898`
- `market_context_high->metal_1h` score `-0.0104` n `173` status `ready` deltaP `7.138` edge `0.0422` maxDD `-4.252`
- `market_context_high->fx_24h` score `-0.0751` n `172` status `ready` deltaP `14.8467` edge `0.0307` maxDD `-2.811`
- `market_context_high->unknown_1h` score `-0.1298` n `173` status `ready` deltaP `4.7013` edge `0.0298` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.5676` n `172` status `ready` deltaP `10.5475` edge `0.2725` maxDD `-23.2095`
- `market_context_high->fx_1h` score `-0.5792` n `173` status `ready` deltaP `-1.8734` edge `0.001` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.091` n `173` status `ready` deltaP `-7.2951` edge `-0.0031` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
