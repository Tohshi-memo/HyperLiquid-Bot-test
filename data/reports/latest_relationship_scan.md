# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T12:07:33.851733+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9100`

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

- `market_context_high->unknown_4h` score `31.7329` n `58` status `ready` deltaP `1.23` edge `2.6512` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.9133` n `101` status `ready` deltaP `8.4914` edge `2.372` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `15.1917` n `101` status `ready` deltaP `8.8765` edge `1.6949` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4155` n `101` status `ready` deltaP `16.48` edge `0.2957` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1145` n `101` status `ready` deltaP `19.8337` edge `0.2531` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4032` n `101` status `ready` deltaP `14.8841` edge `0.1476` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7822` n `101` status `ready` deltaP `16.6805` edge `0.0896` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2924` n `101` status `ready` deltaP `23.8913` edge `0.137` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7324` n `58` status `ready` deltaP `5.5596` edge `0.0493` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6154` n `58` status `ready` deltaP `9.5292` edge `0.0133` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5262` n `101` status `ready` deltaP `13.8495` edge `0.0117` maxDD `-0.8144`
- `news_risk_high->fx_4h` score `0.3914` n `101` status `ready` deltaP `10.6224` edge `0.0254` maxDD `-0.421`
- `market_context_high->fx_1h` score `0.3846` n `58` status `ready` deltaP `9.2247` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.2787` n `101` status `ready` deltaP `14.6598` edge `0.0309` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2483` n `58` status `ready` deltaP `5.3996` edge `0.0155` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.2459` n `58` status `ready` deltaP `13.5618` edge `0.0048` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1645` n `101` status `ready` deltaP `3.5913` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3425` n `101` status `ready` deltaP `1.1724` edge `0.0042` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3815` n `58` status `ready` deltaP `2.4285` edge `-0.0027` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4659` n `101` status `ready` deltaP `8.9091` edge `-0.0347` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
