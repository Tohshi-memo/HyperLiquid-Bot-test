# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T21:37:25.361137+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->crypto_alt_24h` score `24.7377` n `46` status `ready` deltaP `49.8264` edge `1.7293` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `24.7377` n `46` status `ready` deltaP `49.8264` edge `1.7293` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `14.0329` n `46` status `ready` deltaP `39.7494` edge `0.9183` maxDD `-0.4441`
- `risk_on_and_context->crypto_major_24h` score `14.0329` n `46` status `ready` deltaP `39.7494` edge `0.9183` maxDD `-0.4441`
- `risk_on_high->unknown_4h` score `8.8016` n `76` status `ready` deltaP `29.3726` edge `0.5805` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.8016` n `76` status `ready` deltaP `29.3726` edge `0.5805` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2586` n `46` status `ready` deltaP `70.3125` edge `0.0528` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2586` n `46` status `ready` deltaP `70.3125` edge `0.0528` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.1227` n `46` status `ready` deltaP `53.2986` edge `0.1549` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.1227` n `46` status `ready` deltaP `53.2986` edge `0.1549` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.0129` n `149` status `ready` deltaP `21.054` edge `0.3244` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `4.832` n `46` status `ready` deltaP `32.3672` edge `0.1996` maxDD `-0.0173`
- `risk_on_and_context->equity_24h` score `4.832` n `46` status `ready` deltaP `32.3672` edge `0.1996` maxDD `-0.0173`
- `market_context_high->metal_24h` score `4.5521` n `117` status `ready` deltaP `37.0593` edge `0.2342` maxDD `-3.1535`
- `market_context_high->crypto_major_24h` score `3.8106` n `117` status `ready` deltaP `16.7468` edge `0.48` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `3.1459` n `87` status `ready` deltaP `10.2296` edge `0.2184` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.1459` n `87` status `ready` deltaP `10.2296` edge `0.2184` maxDD `-0.2885`
- `risk_on_high->crypto_alt_4h` score `3.1246` n `76` status `ready` deltaP `14.3213` edge `0.2416` maxDD `-3.802`
- `risk_on_and_context->crypto_alt_4h` score `3.1246` n `76` status `ready` deltaP `14.3213` edge `0.2416` maxDD `-3.802`
- `risk_on_high->crypto_major_4h` score `3.0875` n `76` status `ready` deltaP `22.6171` edge `0.2039` maxDD `-5.791`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
