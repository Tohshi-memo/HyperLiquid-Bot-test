# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T16:07:19.626753+00:00`
- Price records: `672`
- Market context records: `2054`
- Flow alert records: `7808`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.4108` n `205` status `ready` deltaP `33.0793` edge `0.6167` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.7016` n `205` status `ready` deltaP `25.3049` edge `0.6709` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.3267` n `205` status `ready` deltaP `20.0609` edge `0.4684` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.6249` n `205` status `ready` deltaP `17.6876` edge `0.7162` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.2978` n `205` status `ready` deltaP `18.4756` edge `0.2611` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.8576` n `205` status `ready` deltaP `14.6037` edge `0.1258` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.6424` n `206` status `ready` deltaP `13.1068` edge `0.1481` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2114` n `206` status `ready` deltaP `9.9631` edge `0.1459` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.1542` n `205` status `ready` deltaP `18.3939` edge `0.4634` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.0288` n `205` status `ready` deltaP `6.8959` edge `0.1626` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4045` n `206` status `ready` deltaP `8.2714` edge `0.0574` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2484` n `206` status `ready` deltaP `4.6596` edge `0.0616` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1139` n `206` status `ready` deltaP `3.9068` edge `0.0235` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.3958` n `205` status `ready` deltaP `12.3335` edge `0.0241` maxDD `-2.811`
- `market_context_high->crypto_major_24h` score `-0.568` n `205` status `ready` deltaP `18.6075` edge `0.6872` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-0.7249` n `205` status `ready` deltaP `10.8537` edge `0.1295` maxDD `-11.9812`
- `market_context_high->fx_1h` score `-0.7783` n `206` status `ready` deltaP `-0.4491` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8231` n `206` status `ready` deltaP `3.9969` edge `0.0235` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.432` n `205` status `ready` deltaP `-4.6037` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9247` n `206` status `ready` deltaP `1.9417` edge `-0.0039` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
