# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T00:52:27.472034+00:00`
- Price records: `672`
- Market context records: `6142`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.3698` n `30` status `ready` deltaP `40.7291` edge `0.6907` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7493` n `30` status `ready` deltaP `68.5764` edge `0.1886` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3323` n `32` status `ready` deltaP `45.1982` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4554` n `32` status `ready` deltaP `29.491` edge `0.0219` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4646` n `195` status `ready` deltaP `0.8046` edge `0.2175` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1903` n `32` status `ready` deltaP `12.9304` edge `0.1131` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6112` n `32` status `ready` deltaP `8.1774` edge `0.07` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3466` n `195` status `ready` deltaP `3.75` edge `0.0956` maxDD `-2.671`
- `news_risk_high->crypto_major_24h` score `-0.0742` n `30` status `ready` deltaP `11.0764` edge `-0.0054` maxDD `-4.2368`
- `news_risk_high->index_24h` score `-0.2064` n `30` status `ready` deltaP `7.5` edge `0.0107` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2341` n `195` status `ready` deltaP `2.1833` edge `0.0` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3629` n `195` status `ready` deltaP `-2.6118` edge `0.2404` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `-0.5959` n `30` status `ready` deltaP `14.0973` edge `-0.1231` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6101` n `195` status `ready` deltaP `3.6945` edge `0.0159` maxDD `-3.4996`
- `market_context_high->metal_24h` score `-0.7197` n `195` status `ready` deltaP `16.5572` edge `0.0542` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.7739` n `195` status `ready` deltaP `-2.2885` edge `-0.0046` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7855` n `32` status `ready` deltaP `-3.2934` edge `-0.029` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8428` n `195` status `ready` deltaP `2.0912` edge `-0.0043` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8453` n `195` status `ready` deltaP `-1.1577` edge `0.0109` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9647` n `195` status `ready` deltaP `3.1614` edge `0.0305` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
