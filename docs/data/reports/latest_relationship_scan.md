# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T17:37:29.630247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4030`

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

- `news_risk_high->crypto_alt_4h` score `-0.007` n `146` status `ready` deltaP `7.7619` edge `0.211` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5767` n `146` status `ready` deltaP `2.0322` edge `0.0353` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6171` n `146` status `ready` deltaP `-1.0253` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8568` n `146` status `ready` deltaP `1.6467` edge `-0.0024` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.42` n `146` status `ready` deltaP `-6.7447` edge `-0.0149` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4236` n `146` status `ready` deltaP `-7.0122` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8324` n `146` status `ready` deltaP `0.5367` edge `-0.0084` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1214` n `146` status `ready` deltaP `-7.5794` edge `0.0104` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.1374` n `146` status `ready` deltaP `-4.2044` edge `0.0382` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4445` n `146` status `ready` deltaP `-18.6638` edge `-0.0181` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6212` n `146` status `ready` deltaP `-6.636` edge `-0.0242` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-3.3456` n `146` status `ready` deltaP `3.9579` edge `0.053` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.3664` n `146` status `ready` deltaP `-7.7065` edge `-0.0566` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.3784` n `146` status `ready` deltaP `-10.036` edge `0.0208` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8331` n `146` status `ready` deltaP `-5.4711` edge `-0.0458` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1877` n `146` status `ready` deltaP `-11.9446` edge `-0.1174` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.0414` n `146` status `ready` deltaP `14.8221` edge `0.4415` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9375` n `146` status `ready` deltaP `0.2318` edge `-0.0769` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.4031` n `146` status `ready` deltaP `11.8809` edge `0.4209` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.2105` n `146` status `ready` deltaP `-20.6807` edge `-0.0536` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
