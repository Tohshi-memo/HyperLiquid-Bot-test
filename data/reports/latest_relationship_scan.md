# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T12:37:31.694908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0329` n `54` status `ready` deltaP `38.5017` edge `0.3294` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0329` n `54` status `ready` deltaP `38.5017` edge `0.3294` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.2674` n `150` status `ready` deltaP `20.1159` edge `0.437` maxDD `-5.906`
- `market_context_high->crypto_alt_4h` score `4.47` n `150` status `ready` deltaP `12.2479` edge `0.5077` maxDD `-10.015`
- `risk_on_high->crypto_major_4h` score `4.4499` n `76` status `ready` deltaP `25.1685` edge `0.3008` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4499` n `76` status `ready` deltaP `25.1685` edge `0.3008` maxDD `-4.1548`
- `market_context_high->crypto_major_1h` score `0.6328` n `162` status `ready` deltaP `5.3689` edge `0.0975` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.361` n `150` status `ready` deltaP `13.0671` edge `0.0475` maxDD `-1.6961`
- `market_context_high->crypto_alt_1h` score `0.3286` n `162` status `ready` deltaP `6.9029` edge `0.1128` maxDD `-5.8485`
- `risk_on_high->index_1h` score `0.1188` n `88` status `ready` deltaP `6.3917` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1188` n `88` status `ready` deltaP `6.3917` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->crypto_alt_4h` score `0.1119` n `76` status `ready` deltaP `3.5462` edge `0.2067` maxDD `-9.9458`
- `risk_on_and_context->crypto_alt_4h` score `0.1119` n `76` status `ready` deltaP `3.5462` edge `0.2067` maxDD `-9.9458`
- `market_context_high->index_1h` score `-0.1774` n `162` status `ready` deltaP `7.1072` edge `0.0047` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2229` n `162` status `ready` deltaP `7.4647` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.3328` n `88` status `ready` deltaP `-0.215` edge `-0.0032` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3328` n `88` status `ready` deltaP `-0.215` edge `-0.0032` maxDD `-0.376`
- `market_context_high->equity_4h` score `-0.3698` n `150` status `ready` deltaP `13.9939` edge `0.2019` maxDD `-17.4086`
- `market_context_high->equity_1h` score `-0.3843` n `162` status `ready` deltaP `9.6597` edge `0.0373` maxDD `-7.0778`
- `risk_on_high->equity_1h` score `-0.4262` n `88` status `ready` deltaP `10.0805` edge `0.0269` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
