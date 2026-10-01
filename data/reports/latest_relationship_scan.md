# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T20:07:30.400765+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6818`

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

- `market_context_high->unknown_1h` score `337.7185` n `50` status `ready` deltaP `8.479` edge `28.0916` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.2676` n `50` status `ready` deltaP `6.8598` edge `23.8099` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3356` n `102` status `ready` deltaP `35.7128` edge `1.4775` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.2235` n `50` status `ready` deltaP `33.0417` edge `0.7733` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2691` n `50` status `ready` deltaP `18.9146` edge `0.55` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.5412` n `50` status `ready` deltaP `11.6736` edge `0.5549` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0582` n `50` status `ready` deltaP `16.3415` edge `0.4419` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.7766` n `102` status `ready` deltaP `19.6692` edge `0.5823` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8668` n `50` status `ready` deltaP `19.0417` edge `0.555` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3791` n `115` status `ready` deltaP `27.9733` edge `0.1647` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.144` n `50` status `ready` deltaP `35.128` edge `0.0413` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0167` n `50` status `ready` deltaP `14.4491` edge `0.2001` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9326` n `50` status `ready` deltaP `13.4551` edge `0.221` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.8405` n `102` status `ready` deltaP `20.6495` edge `0.4614` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.2861` n `102` status `ready` deltaP `23.2231` edge `0.0835` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1326` n `102` status `ready` deltaP `24.6324` edge `0.2366` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5274` n `50` status `ready` deltaP `21.2395` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.905` n `50` status `ready` deltaP `14.7917` edge `0.0745` maxDD `-1.2338`
- `news_risk_high->commodity_24h` score `0.6365` n `102` status `ready` deltaP `19.2402` edge `0.0948` maxDD `-7.9353`
- `news_risk_high->equity_1h` score `0.5706` n `115` status `ready` deltaP `7.9966` edge `0.0479` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
