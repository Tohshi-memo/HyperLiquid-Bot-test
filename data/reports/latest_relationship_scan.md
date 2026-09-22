# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T18:07:35.352113+00:00`
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

- `market_context_high->unknown_4h` score `46.545` n `46` status `ready` deltaP `7.0122` edge `3.832` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.7181` n `46` status `ready` deltaP `13.1869` edge `2.4042` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2848` n `46` status `ready` deltaP `12.3189` edge `1.285` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.6267` n `46` status `ready` deltaP `12.6736` edge `1.1344` maxDD `0.0`
- `market_context_high->index_24h` score `5.5776` n `46` status `ready` deltaP `20.1314` edge `0.3393` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.1747` n `98` status `ready` deltaP `38.7472` edge `0.2908` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `3.9803` n `98` status `ready` deltaP `-10.0163` edge `1.0843` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `2.7838` n `98` status `ready` deltaP `11.8622` edge `0.2527` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `2.7442` n `98` status `ready` deltaP `15.0634` edge `0.186` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.2082` n `98` status `ready` deltaP `12.691` edge `0.1348` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.868` n `46` status `ready` deltaP `22.2494` edge `0.0207` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.4861` n `98` status `ready` deltaP `14.0383` edge `0.0696` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2355` n `98` status `ready` deltaP `19.1637` edge `0.0388` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.1965` n `46` status `ready` deltaP `23.3092` edge `-0.0323` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7525` n `46` status `ready` deltaP `6.7626` edge `0.0419` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5515` n `98` status `ready` deltaP `14.2857` edge `0.0109` maxDD `-0.8144`
- `market_context_high->equity_4h` score `0.5277` n `46` status `ready` deltaP `5.0902` edge `0.0407` maxDD `-0.4529`
- `news_risk_high->metal_24h` score `0.4939` n `98` status `ready` deltaP `18.6508` edge `0.0234` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.4535` n `98` status `ready` deltaP `18.7783` edge `0.0919` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
