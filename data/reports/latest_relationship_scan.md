# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T20:22:15.807254+00:00`
- Price records: `672`
- Market context records: `1876`
- Flow alert records: `7300`
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

- `market_context_high->crypto_alt_4h` score `6.7643` n `199` status `ready` deltaP `21.5942` edge `0.5342` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.5491` n `199` status `ready` deltaP `26.8001` edge `0.4917` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3229` n `199` status `ready` deltaP `18.1104` edge `0.4419` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.8231` n `178` status `ready` deltaP `19.6044` edge `0.4305` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3502` n `199` status `ready` deltaP `14.4296` edge `0.2091` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.2285` n `178` status `ready` deltaP `12.4864` edge `0.2253` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.9852` n `178` status `ready` deltaP `12.4766` edge `0.6143` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4665` n `199` status `ready` deltaP `9.9407` edge `0.0815` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4367` n `199` status `ready` deltaP `6.046` edge `0.0947` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.4135` n `178` status `ready` deltaP `10.68` edge `0.4531` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.3012` n `178` status `ready` deltaP `19.0329` edge `0.7568` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.2903` n `178` status `ready` deltaP `15.2544` edge `0.0274` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.1322` n `199` status `ready` deltaP `5.1583` edge `0.088` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2534` n `199` status `ready` deltaP `3.6395` edge `0.034` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5372` n `199` status `ready` deltaP `3.1377` edge `0.0295` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5523` n `199` status `ready` deltaP `6.1317` edge `0.0219` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5674` n `199` status `ready` deltaP `12.3905` edge `0.1393` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6924` n `199` status `ready` deltaP `-3.8012` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7536` n `199` status `ready` deltaP `-1.2036` edge `0.0084` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.0002` n `199` status `ready` deltaP `-5.1913` edge `-0.0048` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
