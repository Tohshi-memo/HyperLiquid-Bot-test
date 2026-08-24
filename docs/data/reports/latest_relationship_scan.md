# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T12:52:30.199786+00:00`
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

- `news_risk_high->unknown_24h` score `47.9358` n `51` status `ready` deltaP `16.4931` edge `3.8847` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7887` n `51` status `ready` deltaP `40.237` edge `0.9739` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0693` n `51` status `ready` deltaP `24.1063` edge `0.933` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5864` n `51` status `ready` deltaP `48.9481` edge `0.1544` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7674` n `51` status `ready` deltaP `26.7755` edge `0.2125` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6941` n `51` status `ready` deltaP `16.9337` edge `0.2254` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.1053` n `79` status `ready` deltaP `5.1007` edge `0.1917` maxDD `-1.0208`
- `market_context_high->unknown_4h` score `1.7161` n `135` status `ready` deltaP `19.4004` edge `0.0545` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.2484` n `51` status `ready` deltaP `30.5045` edge `-0.0951` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0055` n `51` status `ready` deltaP `14.4637` edge `0.0271` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9319` n `51` status `ready` deltaP `18.193` edge `0.0346` maxDD `-0.9128`
- `market_context_high->metal_4h` score `0.2551` n `135` status `ready` deltaP `11.8123` edge `-0.0116` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2263` n `51` status `ready` deltaP `8.9732` edge `0.0045` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1476` n `51` status `ready` deltaP `8.0897` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0122` n `135` status `ready` deltaP `10.8771` edge `-0.0266` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1466` n `51` status `ready` deltaP `1.7436` edge `-0.0081` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1511` n `51` status `ready` deltaP `7.3679` edge `-0.0086` maxDD `-0.249`
- `market_context_high->fx_24h` score `-0.1799` n `79` status `ready` deltaP `13.1395` edge `-0.0043` maxDD `-3.1759`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
