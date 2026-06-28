# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T13:37:28.176805+00:00`
- Price records: `672`
- Market context records: `5045`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10234`

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

- `market_context_high->unknown_1h` score `11.818` n `101` status `ready` deltaP `3.6491` edge `1.0106` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9331` n `93` status `ready` deltaP `21.9069` edge `0.7006` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5555` n `93` status `ready` deltaP `17.0994` edge `0.5074` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.4023` n `93` status `ready` deltaP `14.7883` edge `0.491` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2014` n `93` status `ready` deltaP `12.7819` edge `0.1228` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.7235` n `101` status `ready` deltaP `6.8165` edge `0.1066` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.7062` n `101` status `ready` deltaP `7.1841` edge `0.0683` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.3671` n `93` status `ready` deltaP `2.2063` edge `0.1705` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3226` n `101` status `ready` deltaP `6.1258` edge `0.0357` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.168` n `101` status `ready` deltaP `5.112` edge `0.0897` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0208` n `75` status `ready` deltaP `9.7708` edge `0.0084` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.258` n `93` status `ready` deltaP `2.3423` edge `0.039` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3144` n `101` status `ready` deltaP `1.6008` edge `0.015` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4275` n `101` status `ready` deltaP `1.0938` edge `0.012` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7579` n `93` status `ready` deltaP `4.1552` edge `0.0004` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0339` n `93` status `ready` deltaP `-4.678` edge `-0.0025` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.4851` n `101` status `ready` deltaP `-8.6915` edge `-0.0048` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.5624` n `75` status `ready` deltaP `6.625` edge `0.0446` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6919` n `75` status `ready` deltaP `-0.1111` edge `-0.0899` maxDD `-27.5371`
- `market_context_high->unknown_24h` score `-5.1078` n `75` status `ready` deltaP `27.1805` edge `-0.5726` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
