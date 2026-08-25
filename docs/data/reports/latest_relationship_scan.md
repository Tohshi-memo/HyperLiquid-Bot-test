# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T00:25:12.844236+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.7572` n `51` status `ready` deltaP `8.6806` edge `3.6719` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0499` n `51` status `ready` deltaP `24.8685` edge `0.9263` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.2431` n `51` status `ready` deltaP `40.237` edge `0.8451` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2384` n `51` status `ready` deltaP `48.9481` edge `0.1254` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.8046` n `51` status `ready` deltaP `27.6901` edge `0.2095` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5765` n `51` status `ready` deltaP `16.6343` edge `0.2176` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3298` n `51` status `ready` deltaP `39.3024` edge `0.0289` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8454` n `130` status `ready` deltaP `19.9062` edge `0.0619` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2685` n `51` status `ready` deltaP `17.2948` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0566` n `51` status `ready` deltaP `19.2409` edge `0.0436` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9511` n `51` status `ready` deltaP `14.1589` edge `0.0246` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2627` n `51` status `ready` deltaP `8.8382` edge `-0.0062` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2107` n `51` status `ready` deltaP `8.5241` edge `0.0055` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.0834` n `130` status `ready` deltaP `10.7153` edge `-0.0186` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0336` n `130` status `ready` deltaP `11.2045` edge `-0.027` maxDD `-1.5916`
- `market_context_high->unknown_24h` score `-0.0899` n `115` status `ready` deltaP `4.3328` edge `-0.0071` maxDD `-0.6752`
- `news_risk_high->metal_1h` score `-0.173` n `51` status `ready` deltaP `1.1448` edge `-0.0075` maxDD `-0.1184`
- `news_risk_high->metal_24h` score `-0.1842` n `51` status `ready` deltaP `22.692` edge `-0.1624` maxDD `-0.0053`
- `news_risk_high->metal_4h` score `-0.3427` n `51` status `ready` deltaP `5.8435` edge `-0.0144` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4162` n `130` status `ready` deltaP `2.8604` edge `0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
