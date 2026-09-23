# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T04:37:35.025162+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9818`

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

- `market_context_high->unknown_4h` score `46.3776` n `46` status `ready` deltaP `7.4695` edge `3.815` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4903` n `46` status `ready` deltaP `13.5341` edge `2.3829` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6717` n `46` status `ready` deltaP `12.1453` edge `1.3184` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.6528` n `46` status `ready` deltaP `10.5903` edge `0.9838` maxDD `0.0`
- `market_context_high->index_24h` score `5.6536` n `46` status `ready` deltaP `20.8258` edge `0.341` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7967` n `96` status `ready` deltaP `-9.2014` edge `1.1469` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4874` n `96` status `ready` deltaP `34.8958` edge `0.2592` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6308` n `97` status `ready` deltaP `13.1506` edge `0.1893` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1197` n `46` status `ready` deltaP `24.8409` edge `0.0244` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.0646` n `97` status `ready` deltaP `8.2726` edge `0.2167` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8649` n `103` status `ready` deltaP `10.9121` edge `0.1317` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4077` n `103` status `ready` deltaP `13.008` edge `0.0741` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3997` n `97` status `ready` deltaP `20.661` edge `0.0425` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9345` n `96` status `ready` deltaP `24.6528` edge `0.1144` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7562` n `46` status `ready` deltaP `6.4632` edge `0.0442` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.6767` n `46` status `ready` deltaP `5.2426` edge `0.0521` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6543` n `46` status `ready` deltaP `10.3554` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->metal_4h` score `0.4395` n `97` status `ready` deltaP `13.6928` edge `0.0411` maxDD `-1.9941`
- `news_risk_high->metal_1h` score `0.4289` n `103` status `ready` deltaP `12.9571` edge `0.0087` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.3262` n `46` status `ready` deltaP `16.8856` edge `-0.062` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
