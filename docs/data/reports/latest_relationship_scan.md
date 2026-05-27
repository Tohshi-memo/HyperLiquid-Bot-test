# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T23:52:19.698345+00:00`
- Price records: `672`
- Market context records: `2088`
- Flow alert records: `7905`
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

- `market_context_high->crypto_major_4h` score `10.3622` n `192` status `ready` deltaP `36.4964` edge `0.6732` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `10.2861` n `192` status `ready` deltaP `30.5768` edge `0.7678` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.1782` n `192` status `ready` deltaP `24.6443` edge `0.5088` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.4744` n `191` status `ready` deltaP `21.841` edge `0.7593` maxDD `-35.8966`
- `market_context_high->equity_4h` score `4.0675` n `192` status `ready` deltaP `21.8115` edge `0.303` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.4575` n `192` status `ready` deltaP `18.2927` edge `0.1512` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.2355` n `192` status `ready` deltaP `15.9306` edge `0.1787` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.9576` n `191` status `ready` deltaP `10.9005` edge `0.2133` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.8852` n `192` status `ready` deltaP `12.5655` edge `0.1847` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7824` n `191` status `ready` deltaP `21.9868` edge `0.4918` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.6663` n `192` status `ready` deltaP `9.9239` edge `0.0682` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5821` n `192` status `ready` deltaP `5.7105` edge `0.0824` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.1897` n `191` status `ready` deltaP `21.1634` edge `0.7333` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.0153` n `192` status `ready` deltaP `5.0275` edge `0.0268` maxDD `-1.3898`
- `market_context_high->metal_4h` score `-0.1025` n `192` status `ready` deltaP `13.5543` edge `0.1556` maxDD `-11.3602`
- `market_context_high->fx_24h` score `-0.1278` n `191` status `ready` deltaP `14.7982` edge `0.03` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.3715` n `192` status `ready` deltaP `5.8071` edge `0.0324` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8059` n `192` status `ready` deltaP `-0.8982` edge `0.0016` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3412` n `192` status `ready` deltaP `-3.7094` edge `0.0011` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.3581` n `191` status `ready` deltaP `10.897` edge `0.2043` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
