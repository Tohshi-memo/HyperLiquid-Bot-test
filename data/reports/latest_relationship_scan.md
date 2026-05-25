# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T18:37:17.049917+00:00`
- Price records: `672`
- Market context records: `1868`
- Flow alert records: `7278`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `6.5479` n `199` status `ready` deltaP `21.2893` edge `0.5182` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.243` n `199` status `ready` deltaP `25.7331` edge `0.4733` maxDD `-4.9684`
- `market_context_high->metal_24h` score `4.4652` n `178` status `ready` deltaP `20.8197` edge `0.4759` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1899` n `199` status `ready` deltaP `17.3482` edge `0.4359` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.3505` n `178` status `ready` deltaP `13.0072` edge `0.232` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.1756` n `199` status `ready` deltaP `13.9723` edge `0.1976` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.9708` n `178` status `ready` deltaP `12.4766` edge `0.6131` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4125` n `199` status `ready` deltaP `9.9407` edge `0.077` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.3895` n `178` status `ready` deltaP `10.68` edge `0.4511` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.2676` n `199` status `ready` deltaP `5.1478` edge `0.0866` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2575` n `178` status `ready` deltaP `19.2065` edge `0.752` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1787` n `178` status `ready` deltaP `14.0391` edge `0.0262` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.0249` n `199` status `ready` deltaP `4.5595` edge `0.0789` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.3361` n `199` status `ready` deltaP `3.3401` edge `0.0291` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5889` n `199` status `ready` deltaP `5.8323` edge `0.0192` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5936` n `199` status `ready` deltaP `2.6886` edge `0.0278` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.6732` n `199` status `ready` deltaP `12.238` edge `0.1315` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6924` n `199` status `ready` deltaP `-3.8012` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.8075` n `199` status `ready` deltaP `-1.503` edge `0.0059` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9915` n `199` status `ready` deltaP `-5.0389` edge `-0.0047` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
