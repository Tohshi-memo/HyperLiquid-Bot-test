# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T06:07:18.059951+00:00`
- Price records: `672`
- Market context records: `2114`
- Flow alert records: `7982`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9140`

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

- `market_context_high->crypto_alt_4h` score `12.3695` n `167` status `ready` deltaP `35.0737` edge `0.8906` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.4536` n `167` status `ready` deltaP `40.2996` edge `0.7388` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1106` n `167` status `ready` deltaP `24.5454` edge `0.4205` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.6896` n `167` status `ready` deltaP `24.0981` edge `0.3396` maxDD `-5.0894`
- `market_context_high->metal_4h` score `2.8107` n `167` status `ready` deltaP `19.6902` edge `0.2417` maxDD `-4.7664`
- `market_context_high->index_4h` score `2.8012` n `167` status `ready` deltaP `20.1895` edge `0.1672` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.6891` n `166` status `ready` deltaP `12.2295` edge `0.2654` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.2942` n `167` status `ready` deltaP `15.4191` edge `0.187` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.18` n `167` status `ready` deltaP `12.2754` edge `0.2112` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.8969` n `166` status `ready` deltaP `23.5524` edge `0.4909` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.8379` n `166` status `ready` deltaP `23.8796` edge `0.526` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `0.9775` n `166` status `ready` deltaP `20.8717` edge `0.8009` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.8055` n `167` status `ready` deltaP `10.1797` edge `0.0781` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4671` n `167` status `ready` deltaP `8.2335` edge `0.0511` maxDD `-2.3654`
- `market_context_high->unknown_1h` score `0.0488` n `167` status `ready` deltaP `5.2395` edge `0.0411` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.0444` n `167` status `ready` deltaP `4.7904` edge `0.0308` maxDD `-1.3898`
- `market_context_high->metal_24h` score `-0.0718` n `166` status `ready` deltaP `11.2978` edge `0.3056` maxDD `-23.2095`
- `market_context_high->fx_24h` score `-0.0776` n `166` status `ready` deltaP `14.708` edge `0.0313` maxDD `-2.811`
- `market_context_high->fx_1h` score `-0.6079` n `167` status `ready` deltaP `-2.3952` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.1452` n `167` status `ready` deltaP `-8.291` edge `-0.0034` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
