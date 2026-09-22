# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T20:37:28.885001+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `45.6342` n `46` status `ready` deltaP `7.0122` edge `3.7561` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5091` n `46` status `ready` deltaP `12.8397` edge `2.3891` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2097` n `46` status `ready` deltaP `12.1453` edge `1.2799` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.8333` n `46` status `ready` deltaP `11.1111` edge `1.0787` maxDD `0.0`
- `market_context_high->index_24h` score `5.5179` n `46` status `ready` deltaP `19.6105` edge `0.3378` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.1926` n `96` status `ready` deltaP `38.7153` edge `0.2925` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8156` n `96` status `ready` deltaP `-9.8958` edge `1.1531` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9439` n `96` status `ready` deltaP `14.6341` edge `0.2055` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.8415` n `96` status `ready` deltaP `11.128` edge `0.2624` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.1875` n `96` status `ready` deltaP `12.2817` edge `0.1358` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8596` n `46` status `ready` deltaP `22.2494` edge `0.02` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5434` n `96` status `ready` deltaP `13.7787` edge `0.0761` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2246` n `96` status `ready` deltaP `18.8771` edge `0.0398` maxDD `-0.421`
- `news_risk_high->crypto_alt_24h` score `0.9423` n `96` status `ready` deltaP `-8.6806` edge `0.6245` maxDD `-32.7147`
- `market_context_high->metal_24h` score `0.94` n `46` status `ready` deltaP `21.5731` edge `-0.0421` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7106` n `46` status `ready` deltaP `6.4632` edge `0.0404` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->fx_24h` score `0.6098` n `96` status `ready` deltaP `20.6597` edge `0.0994` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6077` n `96` status `ready` deltaP `14.8765` edge `0.0108` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.442` n `96` status `ready` deltaP `18.4028` edge `0.0184` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
