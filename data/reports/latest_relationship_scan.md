# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T06:37:24.431796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11344`

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

- `risk_on_high->unknown_4h` score `8.996` n `59` status `ready` deltaP `22.5325` edge `0.6423` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.996` n `59` status `ready` deltaP `22.5325` edge `0.6423` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.1651` n `159` status `ready` deltaP `19.3559` edge `0.3484` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6273` n `95` status `ready` deltaP `32.4196` edge `0.2714` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.0252` n `59` status `ready` deltaP `22.6127` edge `0.213` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.0252` n `59` status `ready` deltaP `22.6127` edge `0.213` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.7393` n `59` status `ready` deltaP `9.3119` edge `0.2698` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.7393` n `59` status `ready` deltaP `9.3119` edge `0.2698` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.2272` n `59` status `ready` deltaP `29.4285` edge `0.0914` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.2272` n `59` status `ready` deltaP `29.4285` edge `0.0914` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.6446` n `59` status `ready` deltaP `32.1905` edge `0.0143` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.6446` n `59` status `ready` deltaP `32.1905` edge `0.0143` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.5513` n `159` status `ready` deltaP `11.5185` edge `0.1767` maxDD `-0.9372`
- `risk_on_high->metal_4h` score `1.793` n `59` status `ready` deltaP `22.5144` edge `0.0291` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.793` n `59` status `ready` deltaP `22.5144` edge `0.0291` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7131` n `59` status `ready` deltaP `22.6784` edge `0.0086` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7131` n `59` status `ready` deltaP `22.6784` edge `0.0086` maxDD `-0.0291`
- `risk_on_high->crypto_alt_4h` score `1.7071` n `59` status `ready` deltaP `11.7973` edge `0.1885` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `1.7071` n `59` status `ready` deltaP `11.7973` edge `0.1885` maxDD `-1.5298`
- `risk_on_high->equity_1h` score `1.2207` n `59` status `ready` deltaP `16.1449` edge `0.0175` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
