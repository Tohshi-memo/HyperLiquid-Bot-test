# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T22:52:25.054646+00:00`
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

- `news_risk_high->unknown_24h` score `48.7961` n `50` status `ready` deltaP `11.5717` edge `3.9892` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.2887` n `50` status `ready` deltaP `36.5872` edge `0.9076` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.4491` n `50` status `ready` deltaP `26.3171` edge `0.8719` maxDD `-0.1274`
- `news_risk_high->equity_24h` score `7.26` n `50` status `ready` deltaP `31.8411` edge `0.4865` maxDD `-4.8351`
- `news_risk_high->index_24h` score `3.8674` n `50` status `ready` deltaP `38.6045` edge `0.0801` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.6074` n `50` status `ready` deltaP `42.4573` edge `0.0266` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3038` n `137` status `ready` deltaP `25.0178` edge `0.1492` maxDD `-0.5871`
- `news_risk_high->unknown_1h` score `2.7469` n `50` status `ready` deltaP `15.7784` edge `0.1593` maxDD `-0.8463`
- `news_risk_high->metal_24h` score `2.5222` n `50` status `ready` deltaP `34.7876` edge `-0.0175` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.41` n `50` status `ready` deltaP `19.4451` edge `0.0646` maxDD `-2.1389`
- `market_context_high->unknown_1h` score `1.3803` n `137` status `ready` deltaP `13.1507` edge `0.0723` maxDD `-1.5954`
- `news_risk_high->fx_1h` score `1.3599` n `50` status `ready` deltaP `18.5569` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2812` n `50` status `ready` deltaP `17.2635` edge `0.0196` maxDD `-0.2338`
- `news_risk_high->commodity_1h` score `0.5074` n `50` status `ready` deltaP `14.1497` edge `0.002` maxDD `-0.5024`
- `market_context_high->unknown_24h` score `0.3116` n `133` status `ready` deltaP `5.5567` edge `0.062` maxDD `-3.1794`
- `news_risk_high->index_1h` score `0.103` n `50` status `ready` deltaP `6.9102` edge `0.0011` maxDD `-0.0505`
- `news_risk_high->index_4h` score `0.0952` n `50` status `ready` deltaP `6.4756` edge `0.0045` maxDD `-0.1788`
- `news_risk_high->metal_1h` score `0.0789` n `50` status `ready` deltaP `5.1018` edge `-0.0013` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0465` n `50` status `ready` deltaP `8.2256` edge `-0.0056` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3951` n `137` status `ready` deltaP `3.4912` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
