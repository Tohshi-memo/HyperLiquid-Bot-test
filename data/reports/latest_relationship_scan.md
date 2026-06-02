# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T13:07:23.855171+00:00`
- Price records: `672`
- Market context records: `2665`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `8.8752` n `113` status `ready` deltaP `15.5036` edge `0.9856` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.4207` n `113` status `ready` deltaP `17.2428` edge `0.6196` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.3403` n `121` status `ready` deltaP `22.4539` edge `0.4799` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `2.5105` n `121` status `ready` deltaP `10.5309` edge `0.32` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.2675` n `121` status `ready` deltaP `6.7199` edge `0.1658` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7197` n `132` status `ready` deltaP `8.7915` edge `0.1201` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.0838` n `132` status `ready` deltaP `6.0697` edge `0.0897` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.0156` n `113` status `ready` deltaP `8.1567` edge `0.045` maxDD `-2.5127`
- `market_context_high->fx_24h` score `-0.1388` n `113` status `ready` deltaP `10.7439` edge `0.004` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.153` n `132` status `ready` deltaP `2.6084` edge `0.0278` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.2982` n `121` status `ready` deltaP `6.8245` edge `0.0138` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.3061` n `132` status `ready` deltaP `3.9285` edge `0.0099` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.3114` n `132` status `ready` deltaP `2.3181` edge `0.008` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.5149` n `121` status `ready` deltaP `1.3443` edge `0.0135` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-0.5503` n `132` status `ready` deltaP `-0.4582` edge `0.0019` maxDD `-1.8854`
- `market_context_high->fx_1h` score `-0.5819` n `132` status `ready` deltaP `-1.1885` edge `0.0038` maxDD `-0.2164`
- `market_context_high->metal_4h` score `-0.7383` n `121` status `ready` deltaP `1.5281` edge `0.0126` maxDD `-2.7452`
- `market_context_high->commodity_24h` score `-0.9942` n `113` status `ready` deltaP `6.8784` edge `0.1658` maxDD `-14.7965`
- `market_context_high->commodity_4h` score `-1.2935` n `121` status `ready` deltaP `2.6519` edge `0.0085` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.3299` n `132` status `ready` deltaP `-5.185` edge `0.0076` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
