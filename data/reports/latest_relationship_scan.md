# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T21:22:34.583325+00:00`
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

- `market_context_high->unknown_4h` score `45.5214` n `46` status `ready` deltaP `7.0122` edge `3.7467` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.553` n `46` status `ready` deltaP `13.0133` edge `2.3916` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2013` n `46` status `ready` deltaP `12.1453` edge `1.2792` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.6886` n `46` status `ready` deltaP `10.9375` edge `1.0678` maxDD `0.0`
- `market_context_high->index_24h` score `5.5119` n `46` status `ready` deltaP `19.6105` edge `0.3373` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.1053` n `96` status `ready` deltaP `38.1944` edge `0.2887` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8594` n `96` status `ready` deltaP `-9.7222` edge `1.1556` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9281` n `96` status `ready` deltaP `14.4817` edge `0.2052` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.7509` n `96` status `ready` deltaP `10.6707` edge `0.2579` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.1023` n `96` status `ready` deltaP `11.8326` edge `0.1317` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8462` n `46` status `ready` deltaP `22.097` edge `0.0199` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5086` n `96` status `ready` deltaP `13.629` edge `0.0742` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2684` n `96` status `ready` deltaP `19.3344` edge `0.0404` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.8636` n `46` status `ready` deltaP `21.0523` edge `-0.045` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.7977` n `96` status `ready` deltaP `-8.8542` edge `0.6136` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.6818` n `46` status `ready` deltaP `6.1638` edge `0.04` maxDD `-0.2751`
- `news_risk_high->fx_24h` score `0.6525` n `96` status `ready` deltaP `21.1806` edge `0.1014` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.646` n `96` status `ready` deltaP `15.3256` edge `0.011` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.3923` n `96` status `ready` deltaP `17.882` edge `0.0155` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
