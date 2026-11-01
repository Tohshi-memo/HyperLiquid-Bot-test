# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T02:52:26.498878+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6255`

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

- `market_context_high->unknown_24h` score `4958.6767` n `71` status `ready` deltaP `-3.7828` edge `413.2732` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `217.6883` n `71` status `ready` deltaP `0.7321` edge `18.1491` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.466` n `108` status `ready` deltaP `-5.0454` edge `6.8511` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.6821` n `92` status `ready` deltaP `35.0921` edge `1.1069` maxDD `-6.3871`
- `market_context_high->equity_24h` score `14.0415` n `71` status `ready` deltaP `27.2716` edge `1.1713` maxDD `-9.3054`
- `market_context_high->index_24h` score `5.6336` n `71` status `ready` deltaP `48.6282` edge `0.1631` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.4716` n `108` status `ready` deltaP `20.7317` edge `0.4564` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.8506` n `71` status `ready` deltaP `28.3429` edge `0.082` maxDD `-0.3387`
- `market_context_high->metal_4h` score `1.2772` n `71` status `ready` deltaP `15.7828` edge `0.0437` maxDD `-0.7323`
- `market_context_high->commodity_24h` score `0.9119` n `71` status `ready` deltaP `27.9831` edge `0.1189` maxDD `-9.7506`
- `news_risk_high->crypto_alt_1h` score `0.872` n `108` status `ready` deltaP `9.0264` edge `0.1079` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.8075` n `71` status `ready` deltaP `11.2507` edge `0.0213` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.6644` n `71` status `ready` deltaP `15.5098` edge `0.0002` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.4666` n `71` status `ready` deltaP `-4.4723` edge `0.2074` maxDD `-4.0876`
- `market_context_high->fx_4h` score `0.4068` n `71` status `ready` deltaP `10.6364` edge `0.0021` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.3044` n `71` status `ready` deltaP `1.1533` edge `0.1189` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.2027` n `71` status `ready` deltaP `1.7521` edge `0.0651` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3306` n `71` status `ready` deltaP `0.7316` edge `0.019` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.519` n `71` status `ready` deltaP `-1.8133` edge `0.0014` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-0.5666` n `71` status `ready` deltaP `13.4167` edge `0.068` maxDD `-12.7399`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
