# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T03:37:18.322840+00:00`
- Price records: `672`
- Market context records: `2004`
- Flow alert records: `7661`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7593`

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

- `market_context_high->crypto_major_4h` score `8.7657` n `215` status `ready` deltaP `30.4453` edge `0.5805` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.1901` n `215` status `ready` deltaP `24.1918` edge `0.6357` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.5749` n `215` status `ready` deltaP `18.7939` edge `0.4142` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.6333` n `215` status `ready` deltaP `15.3892` edge `0.2263` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.7467` n `185` status `ready` deltaP `15.6599` edge `0.5732` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.382` n `215` status `ready` deltaP `11.5771` edge `0.1366` maxDD `-3.2225`
- `market_context_high->metal_24h` score `1.2425` n `185` status `ready` deltaP `15.6368` edge `0.2419` maxDD `-12.7414`
- `market_context_high->crypto_alt_1h` score `1.0998` n `215` status `ready` deltaP `9.3476` edge `0.1407` maxDD `-4.9097`
- `market_context_high->index_4h` score `1.0217` n `215` status `ready` deltaP `9.9759` edge `0.087` maxDD `-1.8022`
- `market_context_high->equity_24h` score `0.8524` n `185` status `ready` deltaP `14.4715` edge `0.4644` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.6665` n `185` status `ready` deltaP `16.2643` edge `0.0293` maxDD `-1.575`
- `market_context_high->index_24h` score `0.0357` n `185` status `ready` deltaP `2.7472` edge `0.1075` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0219` n `215` status `ready` deltaP `5.2521` edge `0.042` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `-0.3447` n `185` status `ready` deltaP `19.3132` edge `0.7011` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.5418` n `215` status `ready` deltaP `0.4032` edge `0.0112` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `-0.7301` n `215` status `ready` deltaP `3.0177` edge `-0.009` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.7813` n `215` status `ready` deltaP `2.1411` edge `0.0043` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8389` n `215` status `ready` deltaP `-1.1308` edge `0.0004` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.6137` n `215` status `ready` deltaP `-6.635` edge `-0.0021` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.6914` n `215` status `ready` deltaP `6.7675` edge `0.0762` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
