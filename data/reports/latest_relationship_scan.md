# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T03:37:29.903692+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9754`

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

- `market_context_high->unknown_4h` score `46.046` n `46` status `ready` deltaP `7.1646` edge `3.7894` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6031` n `46` status `ready` deltaP `13.5341` edge `2.3923` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6405` n `46` status `ready` deltaP `12.1453` edge `1.3158` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.8244` n `46` status `ready` deltaP `10.5903` edge `0.9981` maxDD `0.0`
- `market_context_high->index_24h` score `5.6488` n `46` status `ready` deltaP `20.8258` edge `0.3406` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9095` n `96` status `ready` deltaP `-9.2014` edge `1.1563` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.5054` n `96` status `ready` deltaP `34.8958` edge `0.2607` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.808` n `97` status `ready` deltaP `13.7604` edge `0.2` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.2238` n `97` status `ready` deltaP `8.8823` edge `0.2259` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.0771` n `46` status `ready` deltaP `24.3836` edge `0.0239` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.9237` n `103` status `ready` deltaP `11.2115` edge `0.1346` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4965` n `103` status `ready` deltaP `13.4571` edge `0.0785` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3997` n `97` status `ready` deltaP `20.661` edge `0.0425` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.8867` n `96` status `ready` deltaP `23.9583` edge `0.1129` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8125` n `46` status `ready` deltaP `6.9123` edge `0.0459` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6938` n `46` status `ready` deltaP `10.8045` edge `0.0111` maxDD `-0.0249`
- `market_context_high->equity_4h` score `0.6051` n `46` status `ready` deltaP `4.6329` edge `0.0502` maxDD `-0.4529`
- `news_risk_high->metal_1h` score `0.4697` n `103` status `ready` deltaP `13.4062` edge `0.0091` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.4275` n `97` status `ready` deltaP `13.6928` edge `0.0401` maxDD `-1.9941`
- `market_context_high->metal_24h` score `0.413` n `46` status `ready` deltaP `17.5801` edge `-0.0594` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
