# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T06:07:26.088148+00:00`
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

- `news_risk_high->unknown_24h` score `50.8731` n `51` status `ready` deltaP `17.0139` edge `4.126` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3671` n `51` status `ready` deltaP `40.237` edge `1.0221` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9061` n `51` status `ready` deltaP `23.1916` edge `0.9255` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.794` n `51` status `ready` deltaP `48.9481` edge `0.1717` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.6229` n `51` status `ready` deltaP `26.3182` edge `0.2035` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5442` n `51` status `ready` deltaP `16.0355` edge `0.2189` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2516` n `51` status `ready` deltaP `38.2353` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.3158` n `145` status `ready` deltaP `22.3938` edge `0.0617` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.8478` n `51` status `ready` deltaP `35.192` edge `-0.0764` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9483` n `51` status `ready` deltaP `18.3427` edge `0.0357` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9241` n `51` status `ready` deltaP `13.7015` edge `0.0254` maxDD `-0.1788`
- `news_risk_high->crypto_alt_24h` score `0.8929` n `51` status `ready` deltaP `24.8264` edge `-0.0911` maxDD `0.0`
- `news_risk_high->index_1h` score `0.259` n `51` status `ready` deltaP `9.572` edge `0.0047` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1775` n `51` status `ready` deltaP `8.3891` edge `-0.0103` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1029` n `51` status `ready` deltaP `2.3424` edge `-0.0065` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1243` n `51` status `ready` deltaP `7.6728` edge `-0.0084` maxDD `-0.249`
- `market_context_high->unknown_1h` score `-0.2564` n `153` status `ready` deltaP `9.4996` edge `-0.0398` maxDD `-1.5916`
- `market_context_high->metal_4h` score `-0.269` n `145` status `ready` deltaP `5.8337` edge `-0.019` maxDD `-1.3507`
- `market_context_high->metal_1h` score `-0.4206` n `153` status `ready` deltaP `-1.5792` edge `-0.0057` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
