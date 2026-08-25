# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T06:37:44.706313+00:00`
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

- `news_risk_high->unknown_24h` score `43.9768` n `51` status `ready` deltaP `4.3403` edge `3.6358` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8577` n `51` status `ready` deltaP `24.716` edge `0.9113` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.8578` n `51` status `ready` deltaP `39.1953` edge `0.7366` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.9693` n `51` status `ready` deltaP `48.2537` edge `0.1076` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3078` n `51` status `ready` deltaP `16.1852` edge `0.1982` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2238` n `51` status `ready` deltaP `38.0829` edge `0.0282` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.9407` n `51` status `ready` deltaP `24.9462` edge `0.1558` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.8635` n `133` status `ready` deltaP `19.158` edge `0.0684` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1571` n `51` status `ready` deltaP `15.9475` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7909` n `51` status `ready` deltaP `16.9954` edge `0.0245` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.6188` n `51` status `ready` deltaP `11.415` edge `0.0152` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3753` n `51` status `ready` deltaP `10.0358` edge `-0.0048` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0596` n `51` status `ready` deltaP `6.1289` edge `0.0021` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.0796` n `133` status `ready` deltaP `10.524` edge `-0.0319` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1995` n `51` status `ready` deltaP `0.546` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2995` n `51` status `ready` deltaP `5.8435` edge `-0.0108` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.481` n `133` status `ready` deltaP `1.7503` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5832` n `51` status `ready` deltaP `21.6503` edge `-0.1887` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.6873` n `133` status `ready` deltaP `6.0941` edge `-0.0342` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.0706` n `133` status `ready` deltaP `-4.5743` edge `-0.0049` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
