# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T23:22:24.854400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7053`

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

- `market_context_high->unknown_24h` score `7557.6703` n `55` status `ready` deltaP `1.3889` edge `629.7966` maxDD `0.0`
- `market_context_high->unknown_4h` score `343.1378` n `55` status `ready` deltaP `7.1757` edge `28.5513` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `42.7514` n `55` status `ready` deltaP `4.3604` edge `3.5446` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.2764` n `55` status `ready` deltaP `42.7999` edge `1.5113` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2966` n `94` status `ready` deltaP `31.1355` edge `1.0361` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.2059` n `55` status `ready` deltaP `49.4792` edge `0.1873` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.176` n `55` status `ready` deltaP `24.3598` edge `0.3817` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8897` n `55` status `ready` deltaP `40.7545` edge `0.2502` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6107` n `55` status `ready` deltaP `31.1974` edge `0.2932` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.3376` n `55` status `ready` deltaP `6.2001` edge `0.307` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.0704` n `55` status `ready` deltaP `29.3902` edge `0.085` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.4981` n `126` status `ready` deltaP `10.2328` edge `0.2786` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4056` n `55` status `ready` deltaP `10.5114` edge `0.306` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9532` n `55` status `ready` deltaP `-4.1256` edge `0.4297` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7615` n `55` status `ready` deltaP `20.6374` edge `0.0517` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.586` n `55` status `ready` deltaP `3.6255` edge `0.1605` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.4339` n `55` status `ready` deltaP `3.9249` edge `0.1604` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4264` n `55` status `ready` deltaP `8.1818` edge `0.1253` maxDD `-2.2118`
- `market_context_high->metal_1h` score `1.0025` n `55` status `ready` deltaP `12.3734` edge `0.0259` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5638` n `55` status `ready` deltaP `13.6364` edge `-0.0002` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
