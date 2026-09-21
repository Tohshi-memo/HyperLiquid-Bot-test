# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T13:37:28.306769+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9102`

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

- `market_context_high->unknown_4h` score `31.7785` n `58` status `ready` deltaP `1.23` edge `2.655` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.0423` n `101` status `ready` deltaP `7.6234` edge `2.3052` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `14.1335` n `101` status `ready` deltaP `8.0084` edge `1.6125` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.3821` n `101` status `ready` deltaP `16.6324` edge `0.2919` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1099` n `101` status `ready` deltaP `19.9861` edge `0.2517` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.3996` n `101` status `ready` deltaP `14.8841` edge `0.1473` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7966` n `101` status `ready` deltaP `16.6805` edge `0.0908` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.3568` n `101` status `ready` deltaP `24.0649` edge `0.1441` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7839` n `58` status `ready` deltaP `5.7093` edge `0.0526` maxDD `-0.36`
- `market_context_high->index_1h` score `0.619` n `58` status `ready` deltaP `9.5292` edge `0.0136` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4423` n `101` status `ready` deltaP `12.9513` edge `0.0107` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4097` n `58` status `ready` deltaP `9.5241` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3135` n `101` status `ready` deltaP `9.7078` edge `0.025` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2799` n `101` status `ready` deltaP `14.6598` edge `0.031` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2553` n `58` status `ready` deltaP `13.5618` edge `0.006` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.1644` n `58` status `ready` deltaP `4.5014` edge `0.0145` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1393` n `101` status `ready` deltaP `3.8907` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2909` n `101` status `ready` deltaP `1.3221` edge `0.0075` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4322` n `58` status `ready` deltaP `1.5139` edge `-0.0031` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4819` n `101` status `ready` deltaP `8.7355` edge `-0.0356` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
