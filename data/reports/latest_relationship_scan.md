# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T13:07:32.288862+00:00`
- Price records: `672`
- Market context records: `4936`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `18.5257` n `98` status `ready` deltaP `11.1695` edge `1.5111` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.8403` n `98` status `ready` deltaP `29.0412` edge `0.8445` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2393` n `98` status `ready` deltaP `21.5685` edge `0.5819` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.2203` n `98` status `ready` deltaP `22.953` edge `0.5839` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `6.0636` n `86` status `ready` deltaP `26.5141` edge `0.3628` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8922` n `98` status `ready` deltaP `16.2798` edge `0.1873` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.4921` n `98` status `ready` deltaP `11.2462` edge `0.1156` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9356` n `98` status `ready` deltaP `12.1858` edge `0.0429` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8205` n `98` status `ready` deltaP `7.1429` edge `0.0781` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7715` n `98` status `ready` deltaP `7.4025` edge `0.1534` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.5754` n `98` status `ready` deltaP `8.1908` edge `0.1214` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0689` n `98` status `ready` deltaP `4.2191` edge `0.0356` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.4245` n `98` status `ready` deltaP `0.9532` edge `0.0052` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4435` n `98` status `ready` deltaP `0.9929` edge `0.012` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-1.0458` n `98` status `ready` deltaP `5.5221` edge `-0.0053` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.0543` n `98` status `ready` deltaP `-5.2078` edge `-0.0034` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.3997` n `98` status `ready` deltaP `-7.6317` edge `-0.0045` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.7173` n `86` status `ready` deltaP `-4.0617` edge `-0.015` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-5.112` n `86` status `ready` deltaP `12.9724` edge `-0.0016` maxDD `-27.5371`
- `market_context_high->index_24h` score `-7.5425` n `86` status `ready` deltaP `-9.9281` edge `-0.1538` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
