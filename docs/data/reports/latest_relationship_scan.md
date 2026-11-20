# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T03:52:24.199065+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2778`

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

- `market_context_high->unknown_1h` score `11997.6332` n `108` status `ready` deltaP `1.1367` edge `999.815` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.1353` n `108` status `ready` deltaP `-0.0903` edge `621.2903` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `19.7154` n `95` status `ready` deltaP `36.0435` edge `1.554` maxDD `-9.7736`
- `market_context_high->crypto_alt_24h` score `9.0962` n `95` status `ready` deltaP `20.9266` edge `1.2991` maxDD `-18.1276`
- `market_context_high->crypto_major_4h` score `1.2188` n `108` status `ready` deltaP `3.7883` edge `0.3582` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.8125` n `108` status `ready` deltaP `5.0079` edge `0.2419` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7911` n `108` status `ready` deltaP `20.0034` edge `0.067` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.032` n `108` status `ready` deltaP `6.2874` edge `0.0219` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.246` n `108` status `ready` deltaP `3.5651` edge `0.0059` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.2976` n `108` status `ready` deltaP `4.5465` edge `0.0712` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.7278` n `108` status `ready` deltaP `-1.935` edge `0.0418` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0799` n `108` status `ready` deltaP `6.792` edge `0.0426` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6588` n `108` status `ready` deltaP `-11.9982` edge `-0.0023` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8356` n `108` status `ready` deltaP `-2.2245` edge `-0.0038` maxDD `-4.7471`
- `market_context_high->metal_24h` score `-1.988` n `95` status `ready` deltaP `16.6374` edge `0.1637` maxDD `-25.2223`
- `market_context_high->fx_4h` score `-2.4198` n `108` status `ready` deltaP `-15.56` edge `-0.0049` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4211` n `108` status `ready` deltaP `-9.8193` edge `-0.0281` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-6.8245` n `95` status `ready` deltaP `-20.0402` edge `-0.0078` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1236` n `108` status `ready` deltaP `-29.2626` edge `-0.1126` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3691` n `108` status `ready` deltaP `-6.8992` edge `-0.0526` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
