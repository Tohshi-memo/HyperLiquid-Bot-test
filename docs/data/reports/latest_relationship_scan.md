# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T03:37:25.628722+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.4254` n `162` status `ready` deltaP `15.9873` edge `0.0795` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7282` n `173` status `ready` deltaP `9.8828` edge `0.0291` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5714` n `137` status `ready` deltaP `19.414` edge `0.0246` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.1258` n `162` status `ready` deltaP `6.8052` edge `0.0067` maxDD `-1.1228`
- `market_context_high->fx_1h` score `-0.1677` n `173` status `ready` deltaP `4.1648` edge `-0.0006` maxDD `-0.8933`
- `market_context_high->index_24h` score `-0.6232` n `137` status `ready` deltaP `1.7411` edge `0.0896` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.7919` n `162` status `ready` deltaP `-2.0814` edge `-0.0094` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8069` n `173` status `ready` deltaP `-4.5221` edge `-0.0097` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8451` n `173` status `ready` deltaP `-2.268` edge `-0.0062` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.8846` n `173` status `ready` deltaP `-3.1956` edge `-0.0047` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-1.0754` n `137` status `ready` deltaP `-2.7689` edge `0.0393` maxDD `-2.503`
- `market_context_high->equity_24h` score `-1.3353` n `137` status `ready` deltaP `-1.2735` edge `0.2032` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5238` n `173` status `ready` deltaP `-8.6307` edge `-0.0357` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9498` n `162` status `ready` deltaP `-7.4243` edge `-0.0346` maxDD `-5.937`
- `market_context_high->equity_4h` score `-2.642` n `162` status `ready` deltaP `-7.7443` edge `-0.0992` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5477` n `173` status `ready` deltaP `-9.8785` edge `-0.0564` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0108` n `162` status `ready` deltaP `-12.2478` edge `-0.1568` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3721` n `137` status `ready` deltaP `-11.3152` edge `-0.1446` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7418` n `137` status `ready` deltaP `-1.6994` edge `-0.1344` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5343` n `173` status `ready` deltaP `-4.7636` edge `-0.5504` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
