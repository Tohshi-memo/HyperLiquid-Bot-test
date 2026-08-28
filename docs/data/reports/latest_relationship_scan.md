# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T14:22:28.539513+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.6881` n `50` status `ready` deltaP `11.6118` edge `4.3966` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.5313` n `50` status `ready` deltaP `42.2738` edge `2.3899` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.005` n `56` status `ready` deltaP `22.365` edge `0.7822` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4451` n `50` status `ready` deltaP `30.1005` edge `0.3459` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.5016` n `50` status `ready` deltaP `44.6205` edge `0.0819` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9213` n `56` status `ready` deltaP `45.601` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.8496` n `50` status `ready` deltaP `20.5685` edge `0.233` maxDD `-2.6128`
- `market_context_high->metal_24h` score `2.7738` n `127` status `ready` deltaP `25.3607` edge `0.164` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4289` n `50` status `ready` deltaP `27.688` edge `0.0329` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4107` n `127` status `ready` deltaP `18.1187` edge `0.1208` maxDD `-0.5894`
- `market_context_high->unknown_24h` score `2.2979` n `127` status `ready` deltaP `5.3126` edge `0.2293` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.2719` n `56` status `ready` deltaP `13.1737` edge `0.1372` maxDD `-0.8558`
- `news_risk_high->fx_1h` score `1.4815` n `56` status `ready` deltaP `19.9423` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1063` n `56` status `ready` deltaP `15.601` edge `0.0187` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.8898` n `127` status `ready` deltaP `7.465` edge `0.0694` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7764` n `56` status `ready` deltaP `19.4469` edge `0.0462` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5851` n `56` status `ready` deltaP `13.2405` edge `0.0136` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4999` n `56` status `ready` deltaP `13.8473` edge `0.0038` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3423` n `56` status `ready` deltaP `6.8435` edge `0.0055` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.094` n `56` status `ready` deltaP `7.0993` edge `0.0004` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
