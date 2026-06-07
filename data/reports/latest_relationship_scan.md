# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T11:52:33.466664+00:00`
- Price records: `672`
- Market context records: `3174`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.9243` n `101` status `ready` deltaP `47.2171` edge `0.8884` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.126` n `101` status `ready` deltaP `20.2643` edge `0.9242` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.4708` n `101` status `ready` deltaP `14.2379` edge `2.3733` maxDD `-71.142`
- `market_context_high->index_24h` score `6.1773` n `101` status `ready` deltaP `29.2216` edge `0.8526` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.4104` n `101` status `ready` deltaP `12.8026` edge `1.3217` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1234` n `134` status `ready` deltaP `19.8125` edge `0.174` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7512` n `101` status `ready` deltaP `12.3539` edge `0.003` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.3426` n `134` status `ready` deltaP `11.0506` edge `0.1771` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3385` n `139` status `ready` deltaP `5.8157` edge `0.0317` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3511` n `139` status `ready` deltaP `6.1442` edge `0.0203` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.3744` n `139` status `ready` deltaP `6.323` edge `0.1228` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.9097` n `134` status `ready` deltaP `15.7763` edge `0.0691` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0043` n `139` status `ready` deltaP `3.47` edge `0.0744` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2349` n `139` status `ready` deltaP `4.4059` edge `0.0163` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3386` n `134` status `ready` deltaP `-11.4352` edge `-0.0069` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.587` n `139` status `ready` deltaP `-8.7559` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0443` n `139` status `ready` deltaP `-3.4787` edge `-0.0078` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2062` n `134` status `ready` deltaP `17.6602` edge `0.4039` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0026` n `139` status `ready` deltaP `3.2127` edge `-0.069` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6576` n `134` status `ready` deltaP `10.598` edge `0.2528` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
