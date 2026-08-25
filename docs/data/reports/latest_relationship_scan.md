# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T02:06:26.244076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.5148` n `51` status `ready` deltaP `7.4653` edge `3.6598` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0319` n `51` status `ready` deltaP `24.8685` edge `0.9248` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.9635` n `51` status `ready` deltaP `40.237` edge `0.8218` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.1856` n `51` status `ready` deltaP `48.9481` edge `0.121` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.5722` n `51` status `ready` deltaP `27.0804` edge `0.1942` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5393` n `51` status `ready` deltaP `16.9337` edge `0.2125` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2908` n `51` status `ready` deltaP `38.8451` edge `0.0287` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8274` n `130` status `ready` deltaP `19.9062` edge `0.0604` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.205` n `51` status `ready` deltaP `16.5463` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9194` n `51` status `ready` deltaP `18.3427` edge `0.032` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9065` n `51` status `ready` deltaP `14.0064` edge `0.0219` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2734` n `51` status `ready` deltaP `8.9879` edge `-0.0063` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1593` n `51` status `ready` deltaP `7.7756` edge `0.0039` maxDD `-0.1583`
- `market_context_high->metal_4h` score `-0.0354` n `130` status `ready` deltaP `9.8007` edge `-0.0224` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.0641` n `133` status `ready` deltaP `11.2725` edge `-0.0356` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1956` n `51` status `ready` deltaP `0.8454` edge `-0.0084` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.4045` n `133` status `ready` deltaP `3.101` edge `0.0007` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.4212` n `51` status `ready` deltaP `21.6503` edge `-0.1752` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.4614` n `51` status `ready` deltaP `4.9289` edge `-0.0182` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.918` n `133` status `ready` deltaP `-3.9755` edge `-0.0123` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
