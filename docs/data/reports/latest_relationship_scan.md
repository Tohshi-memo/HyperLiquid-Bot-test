# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T11:07:32.316594+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9175`

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

- `market_context_high->unknown_4h` score `32.4901` n `58` status `ready` deltaP `1.23` edge `2.7143` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `21.5401` n `101` status `ready` deltaP `9.1859` edge `2.4196` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `15.9589` n `101` status `ready` deltaP `9.5709` edge `1.7542` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.6393` n `101` status `ready` deltaP `16.9373` edge `0.3113` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.3235` n `101` status `ready` deltaP `19.9861` edge `0.2695` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4764` n `101` status `ready` deltaP `15.1835` edge `0.1517` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8686` n `101` status `ready` deltaP `17.1296` edge `0.0938` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2604` n `101` status `ready` deltaP `23.8913` edge `0.1329` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7647` n `58` status `ready` deltaP `5.7093` edge `0.051` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6573` n `58` status `ready` deltaP `9.9783` edge `0.0138` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5861` n `101` status `ready` deltaP `14.4483` edge `0.0127` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3977` n `58` status `ready` deltaP `9.3744` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3914` n `101` status `ready` deltaP `10.6224` edge `0.0254` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.3082` n `58` status `ready` deltaP `5.9984` edge `0.0165` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2981` n `101` status `ready` deltaP `14.8122` edge `0.0315` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2569` n `58` status `ready` deltaP `13.7142` edge `0.0052` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1513` n `101` status `ready` deltaP `3.741` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3101` n `101` status `ready` deltaP `1.3221` edge `0.0059` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3815` n `58` status `ready` deltaP `2.4285` edge `-0.0027` maxDD `-0.6588`
- `market_context_high->crypto_major_1h` score `-0.4164` n `58` status `ready` deltaP `-2.6894` edge `0.0551` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
