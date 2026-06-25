# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T22:07:27.881229+00:00`
- Price records: `672`
- Market context records: `4764`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `7.5555` n `129` status `ready` deltaP `13.0472` edge `0.5844` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.9272` n `129` status `ready` deltaP `16.2613` edge `0.5899` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.5211` n `114` status `ready` deltaP `13.4137` edge `0.213` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.1137` n `129` status `ready` deltaP `3.4779` edge `0.0261` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.2351` n `129` status `ready` deltaP `9.3815` edge `0.0392` maxDD `-5.5511`
- `market_context_high->equity_4h` score `-0.4432` n `129` status `ready` deltaP `7.3903` edge `0.0625` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4726` n `129` status `ready` deltaP `6.1189` edge `0.0055` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.5577` n `129` status `ready` deltaP `0.8449` edge `0.0005` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.9481` n `129` status `ready` deltaP `0.8901` edge `-0.0082` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0578` n `129` status `ready` deltaP `-2.9697` edge `-0.0034` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.4891` n `129` status `ready` deltaP `-2.4567` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2594` n `114` status `ready` deltaP `19.1429` edge `0.0936` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2885` n `129` status `ready` deltaP `-1.2963` edge `-0.0672` maxDD `-14.0715`
- `market_context_high->crypto_major_1h` score `-3.5058` n `129` status `ready` deltaP `-2.0181` edge `-0.0929` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-3.6836` n `114` status `ready` deltaP `-14.7661` edge `-0.0203` maxDD `-3.7248`
- `market_context_high->crypto_alt_1h` score `-4.5085` n `129` status `ready` deltaP `-2.2641` edge `-0.077` maxDD `-19.3557`
- `market_context_high->crypto_alt_4h` score `-5.065` n `129` status `ready` deltaP `3.7803` edge `-0.0257` maxDD `-46.5754`
- `market_context_high->index_24h` score `-6.264` n `114` status `ready` deltaP `-8.4887` edge `-0.1094` maxDD `-20.4809`
- `market_context_high->crypto_major_4h` score `-8.0813` n `129` status `ready` deltaP `3.9197` edge `-0.1391` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3449` n `129` status `ready` deltaP `5.4181` edge `-0.2819` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
