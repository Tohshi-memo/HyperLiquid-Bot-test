# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T05:52:26.536933+00:00`
- Price records: `672`
- Market context records: `2113`
- Flow alert records: `7979`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9160`

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

- `market_context_high->crypto_alt_4h` score `12.2173` n `168` status `ready` deltaP `34.5819` edge `0.8812` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.3736` n `168` status `ready` deltaP `40.2149` edge `0.7327` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0552` n `168` status `ready` deltaP `24.5427` edge `0.4159` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.5975` n `168` status `ready` deltaP `23.6063` edge `0.3352` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.7393` n `168` status `ready` deltaP `19.7155` edge `0.1652` maxDD `-1.8022`
- `market_context_high->metal_4h` score `2.7364` n `168` status `ready` deltaP `19.3017` edge `0.2381` maxDD `-4.7664`
- `market_context_high->index_24h` score `2.6586` n `167` status `ready` deltaP `12.1936` edge `0.2631` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.3061` n `168` status `ready` deltaP `15.494` edge `0.1875` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.1851` n `168` status `ready` deltaP `12.3539` edge `0.2111` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.8859` n `167` status `ready` deltaP `23.5056` edge `0.4903` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.8828` n `167` status `ready` deltaP `23.8112` edge `0.5302` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `0.9015` n `167` status `ready` deltaP `20.9259` edge `0.7942` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.8407` n `168` status `ready` deltaP `10.3793` edge `0.0797` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4592` n `168` status `ready` deltaP `8.0446` edge `0.0517` maxDD `-2.3654`
- `market_context_high->index_1h` score `0.0748` n `168` status `ready` deltaP `5.0364` edge `0.0317` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.0203` n `168` status `ready` deltaP `4.9009` edge `0.0376` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0777` n `167` status `ready` deltaP `14.737` edge `0.0311` maxDD `-2.811`
- `market_context_high->metal_24h` score `-0.093` n `167` status `ready` deltaP `11.3845` edge `0.3023` maxDD `-23.2095`
- `market_context_high->fx_1h` score `-0.6155` n `168` status `ready` deltaP `-2.5271` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.136` n `168` status `ready` deltaP `-8.1156` edge `-0.0034` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
