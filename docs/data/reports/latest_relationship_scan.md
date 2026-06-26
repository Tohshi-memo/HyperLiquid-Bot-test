# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T20:07:33.671724+00:00`
- Price records: `672`
- Market context records: `4861`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7626`

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

- `market_context_high->unknown_1h` score `13.4526` n `110` status `ready` deltaP `10.1715` edge `1.095` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.9565` n `109` status `ready` deltaP `24.3203` edge `0.7207` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.2055` n `109` status `ready` deltaP `19.8828` edge `0.5198` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.9346` n `109` status `ready` deltaP `17.1249` edge `0.5028` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1598` n `91` status `ready` deltaP `25.2957` edge `0.2956` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3199` n `109` status `ready` deltaP `9.9183` edge `0.1101` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.7622` n `109` status `ready` deltaP `11.005` edge `0.1625` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4783` n `109` status `ready` deltaP `10.3924` edge `0.0383` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4313` n `110` status `ready` deltaP `6.3201` edge `0.117` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3887` n `110` status `ready` deltaP `7.8715` edge `0.0996` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2059` n `110` status `ready` deltaP `4.0855` edge `0.0589` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1487` n `110` status `ready` deltaP `1.1431` edge `0.0313` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2035` n `110` status `ready` deltaP `3.5819` edge `0.016` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4892` n `110` status `ready` deltaP `0.3103` edge `0.0107` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.5825` n `109` status `ready` deltaP `1.8307` edge `0.0059` maxDD `-1.0899`
- `market_context_high->commodity_4h` score `-0.7248` n `109` status `ready` deltaP `7.4597` edge `0.0074` maxDD `-4.4027`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9339` n `91` status `ready` deltaP `-7.204` edge `-0.0121` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8251` n `91` status `ready` deltaP `-8.7073` edge `-0.152` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.4065` n `91` status `ready` deltaP `10.5063` edge `-0.0097` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
