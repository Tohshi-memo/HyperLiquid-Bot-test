# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T05:22:25.190844+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `51.2307` n `51` status `ready` deltaP `17.0139` edge `4.1558` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3851` n `51` status `ready` deltaP `40.237` edge `1.0236` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9219` n `51` status `ready` deltaP `23.3441` edge `0.9258` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8096` n `51` status `ready` deltaP `48.9481` edge `0.173` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.5119` n `51` status `ready` deltaP `15.7361` edge `0.2182` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.5119` n `51` status `ready` deltaP `25.8608` edge `0.1973` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.237` n `51` status `ready` deltaP `38.0829` edge `0.0293` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.3114` n `145` status `ready` deltaP `21.8566` edge `0.0606` maxDD `-0.0956`
- `news_risk_high->metal_24h` score `1.9122` n `51` status `ready` deltaP `35.7128` edge `-0.0745` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `1.3006` n `51` status `ready` deltaP `25.3472` edge `-0.0606` maxDD `0.0`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9085` n `51` status `ready` deltaP `17.8936` edge `0.0336` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8791` n `51` status `ready` deltaP `13.2442` edge `0.0247` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2325` n `51` status `ready` deltaP `9.1229` edge `0.0043` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2039` n `51` status `ready` deltaP `8.6885` edge `-0.0101` maxDD `-0.4666`
- `news_risk_high->metal_4h` score `-0.0805` n `51` status `ready` deltaP `8.1301` edge `-0.0078` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1029` n `51` status `ready` deltaP `2.3424` edge `-0.0065` maxDD `-0.1184`
- `market_context_high->fx_24h` score `-0.2096` n `92` status `ready` deltaP `7.4728` edge `0.0054` maxDD `-1.5673`
- `market_context_high->unknown_1h` score `-0.2767` n `156` status `ready` deltaP `9.6653` edge `-0.0426` maxDD `-1.5916`
- `market_context_high->metal_4h` score `-0.3884` n `145` status `ready` deltaP `4.222` edge `-0.0211` maxDD `-1.5478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
