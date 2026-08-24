# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T14:52:34.401664+00:00`
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

- `news_risk_high->unknown_24h` score `47.1786` n `51` status `ready` deltaP `15.2778` edge `3.8297` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7251` n `51` status `ready` deltaP `40.237` edge `0.9686` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9373` n `51` status `ready` deltaP `24.1063` edge `0.922` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5456` n `51` status `ready` deltaP `48.9481` edge `0.151` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.7753` n `78` status `ready` deltaP `8.8675` edge `0.3681` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.0822` n `51` status `ready` deltaP `27.995` edge `0.2306` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6305` n `51` status `ready` deltaP `16.784` edge `0.2211` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7328` n `130` status `ready` deltaP `19.144` edge `0.0576` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2194` n `51` status `ready` deltaP `16.696` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0771` n `51` status `ready` deltaP `15.0735` edge `0.029` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0652` n `51` status `ready` deltaP `19.0912` edge `0.0457` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `1.0389` n `51` status `ready` deltaP `29.1156` edge `-0.1033` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2948` n `51` status `ready` deltaP `10.0211` edge `0.0063` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.2325` n `130` status `ready` deltaP `11.9348` edge `-0.0143` maxDD `-1.3378`
- `news_risk_high->commodity_1h` score `0.1416` n `51` status `ready` deltaP `7.94` edge `-0.0103` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0876` n `130` status `ready` deltaP `11.3542` edge `-0.0235` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1325` n `51` status `ready` deltaP `1.8933` edge `-0.0073` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1935` n `51` status `ready` deltaP `7.063` edge `-0.0101` maxDD `-0.249`
- `market_context_high->fx_24h` score `-0.3304` n `78` status `ready` deltaP `13.9022` edge `-0.0067` maxDD `-3.6003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
