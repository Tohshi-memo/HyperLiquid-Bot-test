# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T05:07:32.170615+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `44.1622` n `51` status `ready` deltaP `5.3819` edge `3.6443` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9081` n `51` status `ready` deltaP `24.716` edge `0.9155` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.3911` n `51` status `ready` deltaP `40.237` edge `0.7741` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.0896` n `51` status `ready` deltaP `48.9481` edge `0.113` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2827` n `51` status `ready` deltaP `15.8858` edge `0.1981` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.264` n `51` status `ready` deltaP `38.5402` edge `0.0285` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.2359` n `51` status `ready` deltaP `25.8608` edge `0.1743` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9349` n `128` status `ready` deltaP `19.6456` edge `0.0711` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1823` n `51` status `ready` deltaP `16.2469` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8205` n `51` status `ready` deltaP `17.2948` edge `0.0263` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.7255` n `51` status `ready` deltaP `12.3296` edge `0.018` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3273` n `51` status `ready` deltaP `9.5867` edge `-0.0058` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0853` n `51` status `ready` deltaP `6.578` edge `0.0024` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.1048` n `133` status `ready` deltaP `10.2246` edge `-0.032` maxDD `-1.5916`
- `market_context_high->metal_4h` score `-0.1124` n `128` status `ready` deltaP `8.8605` edge `-0.0271` maxDD `-1.3769`
- `news_risk_high->metal_1h` score `-0.1839` n `51` status `ready` deltaP `0.8454` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2981` n `51` status `ready` deltaP `5.996` edge `-0.0117` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4646` n `133` status `ready` deltaP `2.0497` edge `0.0` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5196` n `51` status `ready` deltaP `21.6503` edge `-0.1834` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.031` n `133` status `ready` deltaP `-4.1252` edge `-0.0046` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
