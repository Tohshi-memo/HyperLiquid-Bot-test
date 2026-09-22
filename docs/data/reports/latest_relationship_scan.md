# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T21:07:27.196292+00:00`
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

- `market_context_high->unknown_4h` score `45.5322` n `46` status `ready` deltaP `7.0122` edge `3.7476` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5446` n `46` status `ready` deltaP `13.0133` edge `2.3909` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2013` n `46` status `ready` deltaP `12.1453` edge `1.2792` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.7306` n `46` status `ready` deltaP `10.9375` edge `1.0713` maxDD `0.0`
- `market_context_high->index_24h` score `5.5143` n `46` status `ready` deltaP `19.6105` edge `0.3375` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.1348` n `96` status `ready` deltaP `38.3681` edge `0.29` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.851` n `96` status `ready` deltaP `-9.7222` edge `1.1549` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9087` n `96` status `ready` deltaP `14.3293` edge `0.2046` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.7739` n `96` status `ready` deltaP `10.8232` edge `0.2588` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.1311` n `96` status `ready` deltaP `11.9823` edge `0.1331` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8462` n `46` status `ready` deltaP `22.097` edge `0.0199` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.517` n `96` status `ready` deltaP `13.629` edge `0.0749` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2538` n `96` status `ready` deltaP `19.1819` edge `0.0402` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.8882` n `46` status `ready` deltaP `21.2259` edge `-0.0441` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.8397` n `96` status `ready` deltaP `-8.8542` edge `0.6171` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.695` n `46` status `ready` deltaP `6.3135` edge `0.0401` maxDD `-0.2751`
- `news_risk_high->fx_24h` score `0.638` n `96` status `ready` deltaP `21.0069` edge `0.1007` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6329` n `96` status `ready` deltaP `15.1759` edge `0.0109` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.4083` n `96` status `ready` deltaP `18.0556` edge `0.0164` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
