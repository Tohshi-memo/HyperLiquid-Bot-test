# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T13:07:22.031581+00:00`
- Price records: `672`
- Market context records: `2042`
- Flow alert records: `7771`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.971` n `205` status `ready` deltaP `31.4219` edge `0.5911` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3821` n `205` status `ready` deltaP `24.4014` edge `0.6503` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.1715` n `205` status `ready` deltaP `19.7709` edge `0.4574` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9091` n `205` status `ready` deltaP `16.8419` edge `0.2396` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.1307` n `204` status `ready` deltaP `17.4452` edge `0.5933` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6183` n `205` status `ready` deltaP `13.0765` edge `0.1463` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4462` n `205` status `ready` deltaP `12.9713` edge `0.1024` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2785` n `205` status `ready` deltaP `10.2322` edge `0.1497` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.7043` n `204` status `ready` deltaP `16.5801` edge `0.438` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.5453` n `204` status `ready` deltaP `4.9019` edge `0.1356` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2464` n `205` status `ready` deltaP `7.2098` edge `0.0513` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.1297` n `205` status `ready` deltaP `4.345` edge `0.0538` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2702` n `205` status `ready` deltaP `2.8531` edge `0.0175` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5348` n `204` status `ready` deltaP `10.7843` edge `0.0222` maxDD `-2.7598`
- `market_context_high->metal_1h` score `-0.7568` n `205` status `ready` deltaP `4.5567` edge `0.0253` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8266` n `205` status `ready` deltaP `-0.9924` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-1.0443` n `205` status `ready` deltaP `9.321` edge `0.1131` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.4574` n `205` status `ready` deltaP `-4.8914` edge `-0.0007` maxDD `-1.0513`
- `market_context_high->crypto_major_24h` score `-1.5507` n `204` status `ready` deltaP `16.8685` edge `0.6169` maxDD `-62.3533`
- `market_context_high->commodity_1h` score `-1.8886` n `205` status `ready` deltaP `2.1564` edge `-0.0007` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
