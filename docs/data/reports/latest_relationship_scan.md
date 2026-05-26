# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T20:52:21.205620+00:00`
- Price records: `672`
- Market context records: `1974`
- Flow alert records: `7576`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7583`

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

- `market_context_high->crypto_alt_4h` score `7.4074` n `234` status `ready` deltaP `22.7173` edge `0.5803` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7998` n `234` status `ready` deltaP `26.1987` edge `0.5166` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4637` n `234` status `ready` deltaP `13.5906` edge `0.3171` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2438` n `234` status `ready` deltaP `14.2107` edge `0.2017` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.5817` n `199` status `ready` deltaP `16.7627` edge `0.5521` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.4376` n `199` status `ready` deltaP `15.2406` edge `0.2608` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.9776` n `234` status `ready` deltaP `9.1023` edge `0.1194` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.8778` n `199` status `ready` deltaP `13.9189` edge `0.4702` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7608` n `234` status `ready` deltaP `7.9457` edge `0.1218` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4177` n `199` status `ready` deltaP `4.1922` edge `0.1297` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1317` n `234` status `ready` deltaP `7.5256` edge `0.0697` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0958` n `234` status `ready` deltaP `4.9491` edge `0.0384` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.173` n `199` status `ready` deltaP `18.4605` edge `0.7211` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1928` n `199` status `ready` deltaP `10.446` edge `0.0192` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6149` n `234` status `ready` deltaP `0.3353` edge `0.0097` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6927` n `234` status `ready` deltaP `-3.7617` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1285` n `234` status `ready` deltaP `-7.8395` edge `-0.0036` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3215` n `234` status `ready` deltaP `2.948` edge `0.0038` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.47` n `234` status `ready` deltaP `0.9584` edge `-0.0337` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.851` n `234` status `ready` deltaP `2.4579` edge `0.0021` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
