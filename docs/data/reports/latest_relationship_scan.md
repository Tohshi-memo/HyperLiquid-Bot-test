# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T05:22:28.924889+00:00`
- Price records: `672`
- Market context records: `5739`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.8248` n `218` status `ready` deltaP `14.6614` edge `0.5159` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1534` n `285` status `ready` deltaP `7.6728` edge `0.1255` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2069` n `285` status `ready` deltaP `3.0854` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4471` n `285` status `ready` deltaP `1.6352` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6257` n `285` status `ready` deltaP `0.4376` edge `0.0037` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.7064` n `285` status `ready` deltaP `2.3138` edge `0.0264` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.8002` n `285` status `ready` deltaP `-2.3369` edge `-0.0063` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8992` n `285` status `ready` deltaP `2.4819` edge `0.032` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9851` n `285` status `ready` deltaP `1.1861` edge `0.0304` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.0411` n `218` status `ready` deltaP `12.25` edge `0.0432` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1551` n `285` status `ready` deltaP `1.4752` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.254` n `285` status `ready` deltaP `2.7092` edge `0.0057` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6305` n `285` status `ready` deltaP `-7.5412` edge `-0.0494` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.8156` n `285` status `ready` deltaP `7.4546` edge `0.1462` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.0495` n `218` status `ready` deltaP `-0.5097` edge `0.0269` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7103` n `285` status `ready` deltaP `-2.2111` edge `-0.0269` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.9879` n `285` status `ready` deltaP `5.4872` edge `0.1001` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.0768` n `218` status `ready` deltaP `8.0642` edge `0.0522` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.7545` n `218` status `ready` deltaP `-8.8175` edge `-0.2469` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.7163` n `218` status `ready` deltaP `-12.3105` edge `-0.0803` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
