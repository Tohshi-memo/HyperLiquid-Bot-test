# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T18:18:31.813682+00:00`
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

- `news_risk_high->unknown_24h` score `44.4702` n `51` status `ready` deltaP `5.9028` edge `3.6665` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5582` n `53` status `ready` deltaP `24.2176` edge `0.895` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.9322` n `51` status `ready` deltaP `31.0356` edge `0.5472` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1425` n `51` status `ready` deltaP `41.3092` edge `0.085` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1873` n `53` status `ready` deltaP `16.3117` edge `0.1924` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0392` n `53` status `ready` deltaP `36.0303` edge `0.0265` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.5996` n `133` status `ready` deltaP `22.3592` edge `0.1084` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6877` n `53` status `ready` deltaP `19.889` edge `0.0851` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.2004` n `53` status `ready` deltaP `16.5179` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5026` n `53` status `ready` deltaP `14.2724` edge `0.0057` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.396` n `53` status `ready` deltaP `10.5271` edge `-0.0059` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2438` n `53` status `ready` deltaP `8.0333` edge `0.0065` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1698` n `133` status `ready` deltaP `11.8713` edge `-0.0201` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `-0.0047` n `51` status `ready` deltaP `25.2961` edge `-0.1648` maxDD `-0.0053`
- `news_risk_high->index_1h` score `-0.0402` n `53` status `ready` deltaP `4.4487` edge `0.0005` maxDD `-0.1583`
- `news_risk_high->crypto_alt_24h` score `-0.0467` n `51` status `ready` deltaP `22.3958` edge `-0.1532` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4109` n `133` status `ready` deltaP `3.0976` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.4546` n `53` status `ready` deltaP `-0.6129` edge `-0.0112` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.567` n `53` status `ready` deltaP `4.5099` edge `-0.0242` maxDD `-0.249`
- `market_context_high->metal_4h` score `-1.0674` n `133` status `ready` deltaP `3.5027` edge `-0.0486` maxDD `-2.4293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
