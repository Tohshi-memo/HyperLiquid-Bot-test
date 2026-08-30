# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T17:52:25.891121+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11654`

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

- `risk_on_high->crypto_alt_24h` score `26.134` n `31` status `ready` deltaP `52.4306` edge `1.8283` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.134` n `31` status `ready` deltaP `52.4306` edge `1.8283` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.7307` n `31` status `ready` deltaP `46.3542` edge `1.0852` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.7307` n `31` status `ready` deltaP `46.3542` edge `1.0852` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.6763` n `62` status `ready` deltaP `26.4015` edge `0.6732` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.6763` n `62` status `ready` deltaP `26.4015` edge `0.6732` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `6.9318` n `31` status `ready` deltaP `40.9722` edge `0.3045` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.9318` n `31` status `ready` deltaP `40.9722` edge `0.3045` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.4669` n `31` status `ready` deltaP `72.9167` edge `0.0528` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.4669` n `31` status `ready` deltaP `72.9167` edge `0.0528` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2458` n `31` status `ready` deltaP `53.4722` edge `0.164` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2458` n `31` status `ready` deltaP `53.4722` edge `0.164` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.1481` n `149` status `ready` deltaP `21.054` edge `0.419` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.156` n `62` status `ready` deltaP `25.4377` edge `0.2884` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.156` n `62` status `ready` deltaP `25.4377` edge `0.2884` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.4988` n `117` status `ready` deltaP `36.3782` edge `0.2343` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `3.9294` n `62` status `ready` deltaP `14.2112` edge `0.281` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `3.9294` n `62` status `ready` deltaP `14.2112` edge `0.281` maxDD `-1.5298`
- `risk_on_high->unknown_1h` score `3.8534` n `73` status `ready` deltaP `11.1579` edge `0.267` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.8534` n `73` status `ready` deltaP `11.1579` edge `0.267` maxDD `-0.2885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
