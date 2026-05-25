# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T17:52:14.795444+00:00`
- Price records: `672`
- Market context records: `1864`
- Flow alert records: `7268`
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

- `market_context_high->crypto_alt_4h` score `6.4927` n `199` status `ready` deltaP `21.2893` edge `0.5136` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.1164` n `199` status `ready` deltaP `25.2758` edge `0.4658` maxDD `-4.9684`
- `market_context_high->metal_24h` score `4.7192` n `178` status `ready` deltaP `21.3405` edge `0.4936` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1114` n `199` status `ready` deltaP `16.8909` edge `0.4324` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.3992` n `178` status `ready` deltaP `13.1808` edge `0.2349` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.142` n `199` status `ready` deltaP `13.9723` edge `0.1948` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.0044` n `178` status `ready` deltaP `12.4766` edge `0.6159` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.3969` n `199` status `ready` deltaP `9.9407` edge `0.0757` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.3703` n `178` status `ready` deltaP `10.68` edge `0.4495` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.2952` n `199` status `ready` deltaP `5.2975` edge `0.0879` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2383` n `178` status `ready` deltaP `19.2065` edge `0.7504` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1648` n `178` status `ready` deltaP `13.8655` edge `0.0262` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.0201` n `199` status `ready` deltaP `4.4098` edge `0.0803` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.275` n `199` status `ready` deltaP `3.7892` edge `0.0312` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5967` n `199` status `ready` deltaP `5.6826` edge `0.0192` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5972` n `199` status `ready` deltaP `2.8383` edge `0.0265` maxDD `-3.6151`
- `market_context_high->fx_1h` score `-0.6667` n `199` status `ready` deltaP `-3.3521` edge `0.0001` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.6852` n `199` status `ready` deltaP `12.238` edge `0.1305` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.7955` n `199` status `ready` deltaP `-1.503` edge `0.0069` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9899` n `199` status `ready` deltaP `-5.0389` edge `-0.0045` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
