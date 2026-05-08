# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T11:52:18.689876+00:00`
- Price records: `643`
- Market context records: `752`
- Flow alert records: `2122`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.112` n `146` status `ready` deltaP `31.2689` edge `0.9176` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6501` n `146` status `ready` deltaP `7.5418` edge `0.5087` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.4285` n `146` status `ready` deltaP `2.6729` edge `0.2174` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.1689` n `146` status `ready` deltaP `1.1252` edge `0.2389` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.2444` n `169` status `ready` deltaP `3.581` edge `0.0026` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4362` n `158` status `ready` deltaP `6.194` edge `0.0095` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6177` n `169` status `ready` deltaP `1.1956` edge `0.038` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9431` n `169` status `ready` deltaP `0.4743` edge `0.0036` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0068` n `169` status `ready` deltaP `6.5894` edge `-0.0007` maxDD `-11.4508`
- `market_context_high->equity_1h` score `-1.1372` n `169` status `ready` deltaP `-1.8497` edge `-0.0014` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3267` n `169` status `ready` deltaP `5.3421` edge `-0.0147` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5997` n `169` status `ready` deltaP `-4.7754` edge `-0.0243` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.6054` n `158` status `ready` deltaP `17.2976` edge `0.1215` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7498` n `158` status `ready` deltaP `1.7779` edge `-0.0054` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0172` n `169` status `ready` deltaP `-3.9883` edge `-0.0361` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.1749` n `158` status `ready` deltaP `2.465` edge `0.0593` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5718` n `158` status `ready` deltaP `-1.1114` edge `0.0083` maxDD `-10.5498`
- `market_context_high->unknown_4h` score `-3.72` n `158` status `ready` deltaP `5.0724` edge `-0.156` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.7387` n `158` status `ready` deltaP `-5.7999` edge `0.0772` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-5.453` n `146` status `ready` deltaP `-16.3526` edge `-0.0729` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
