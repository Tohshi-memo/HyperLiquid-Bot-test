# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T18:52:35.443026+00:00`
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

- `market_context_high->unknown_4h` score `46.2594` n `46` status `ready` deltaP `7.0122` edge `3.8082` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5679` n `46` status `ready` deltaP `12.8397` edge `2.394` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2932` n `46` status `ready` deltaP `12.3189` edge `1.2857` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.3402` n `46` status `ready` deltaP `12.1528` edge `1.114` maxDD `0.0`
- `market_context_high->index_24h` score `5.5788` n `46` status `ready` deltaP `20.1314` edge `0.3394` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.3978` n `96` status `ready` deltaP `39.9306` edge `0.3015` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8744` n `96` status `ready` deltaP `-9.8958` edge `1.158` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `3.1176` n `96` status `ready` deltaP `12.1951` edge `0.2783` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `3.1021` n `96` status `ready` deltaP `15.3963` edge `0.2136` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.3061` n `96` status `ready` deltaP `13.0302` edge `0.1407` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.868` n `46` status `ready` deltaP `22.2494` edge `0.0207` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6285` n `96` status `ready` deltaP `14.3775` edge `0.0792` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.4493` n `96` status `ready` deltaP `-7.6389` edge `0.6598` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.1832` n `96` status `ready` deltaP `18.4197` edge `0.0394` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.1296` n `46` status `ready` deltaP `22.7884` edge `-0.0344` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.731` n `46` status `ready` deltaP `6.6129` edge `0.0411` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6389` n `96` status `ready` deltaP `15.1759` edge `0.0114` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6052` n `46` status `ready` deltaP `9.9063` edge `0.0097` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.5652` n `96` status `ready` deltaP `19.6181` edge `0.0261` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.5123` n `96` status `ready` deltaP `19.4444` edge `0.095` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
