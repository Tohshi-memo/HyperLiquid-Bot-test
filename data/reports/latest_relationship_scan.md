# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T05:37:35.232174+00:00`
- Price records: `672`
- Market context records: `5741`
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

- `market_context_high->equity_24h` score `0.8233` n `218` status `ready` deltaP `14.6614` edge `0.5157` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1558` n `285` status `ready` deltaP `7.6728` edge `0.1257` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1983` n `285` status `ready` deltaP `3.2351` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4385` n `285` status `ready` deltaP `1.7849` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6343` n `285` status `ready` deltaP `0.2879` edge `0.0036` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.7064` n `285` status `ready` deltaP `2.3138` edge `0.0264` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7995` n `285` status `ready` deltaP `-2.3369` edge `-0.0062` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8944` n `285` status `ready` deltaP `2.4819` edge `0.0324` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9839` n `285` status `ready` deltaP `1.1861` edge `0.0305` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.0313` n `218` status `ready` deltaP `12.4236` edge `0.0433` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1559` n `285` status `ready` deltaP `1.4752` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.246` n `285` status `ready` deltaP `2.8616` edge `0.0057` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6218` n `285` status `ready` deltaP `-7.3888` edge `-0.0493` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.7819` n `285` status `ready` deltaP `7.607` edge `0.148` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.0503` n `218` status `ready` deltaP `-0.5097` edge `0.0268` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7103` n `285` status `ready` deltaP `-2.2111` edge `-0.0269` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.9589` n `285` status `ready` deltaP `5.6397` edge `0.1015` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.0564` n `218` status `ready` deltaP `8.0642` edge `0.0539` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.7713` n `218` status `ready` deltaP `-8.9911` edge `-0.2479` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.7409` n `218` status `ready` deltaP `-12.4841` edge `-0.0812` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
