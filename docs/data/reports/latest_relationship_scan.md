# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T01:07:27.907118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.3017` n `47` status `ready` deltaP `11.0142` edge `5.9588` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.7807` n `46` status `ready` deltaP `22.9091` edge `2.8446` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.7985` n `46` status `ready` deltaP `20.305` edge `1.6079` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `19.8254` n `46` status `ready` deltaP `17.8819` edge `1.5329` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.1669` n `98` status `ready` deltaP `-1.3145` edge `1.4585` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.9929` n `46` status `ready` deltaP `29.3328` edge `0.3959` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9093` n `103` status `ready` deltaP `14.5365` edge `0.412` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `4.8655` n `98` status `ready` deltaP `-3.5467` edge `0.9172` maxDD `-32.7147`
- `news_risk_high->crypto_major_4h` score `4.5838` n `103` status `ready` deltaP `17.4328` edge `0.3235` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.6289` n `103` status `ready` deltaP `13.9062` edge `0.1754` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4722` n `47` status `ready` deltaP `29.1483` edge `0.0271` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4037` n `98` status `ready` deltaP `23.7741` edge `0.1597` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0481` n `103` status `ready` deltaP `15.8523` edge `0.1085` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.9297` n `46` status `ready` deltaP `23.3092` edge `0.0288` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6234` n `103` status `ready` deltaP `23.6814` edge `0.041` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3951` n `47` status `ready` deltaP `11.1994` edge `0.0834` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1319` n `98` status `ready` deltaP `27.9797` edge `0.1217` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.793` n `47` status `ready` deltaP `12.8137` edge `0.0085` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.7153` n `98` status `ready` deltaP `18.6508` edge `0.0701` maxDD `-3.8855`
- `news_risk_high->metal_1h` score `0.6781` n `103` status `ready` deltaP `15.6517` edge `0.0115` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
