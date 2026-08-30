# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T09:07:24.570303+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11384`

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

- `risk_on_high->unknown_4h` score `9.1724` n `59` status `ready` deltaP `23.4471` edge `0.6509` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.1724` n `59` status `ready` deltaP `23.4471` edge `0.6509` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.4173` n `152` status `ready` deltaP `19.3437` edge `0.3695` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5323` n `93` status `ready` deltaP `31.9668` edge `0.2665` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.3418` n `59` status `ready` deltaP `23.3749` edge `0.2343` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.3418` n `59` status `ready` deltaP `23.3749` edge `0.2343` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.8471` n `59` status `ready` deltaP `10.2101` edge `0.2728` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.8471` n `59` status `ready` deltaP `10.2101` edge `0.2728` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.307` n `59` status `ready` deltaP `29.8858` edge `0.095` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.307` n `59` status `ready` deltaP `29.8858` edge `0.095` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.6982` n `59` status `ready` deltaP `32.8002` edge `0.0147` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.6982` n `59` status `ready` deltaP `32.8002` edge `0.0147` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.6713` n `152` status `ready` deltaP `11.1133` edge `0.1894` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `2.0022` n `59` status `ready` deltaP `12.1021` edge `0.2243` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.0022` n `59` status `ready` deltaP `12.1021` edge `0.2243` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.7674` n `59` status `ready` deltaP `22.2096` edge `0.029` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7674` n `59` status `ready` deltaP `22.2096` edge `0.029` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7251` n `59` status `ready` deltaP `22.8281` edge `0.0086` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7251` n `59` status `ready` deltaP `22.8281` edge `0.0086` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.2698` n `59` status `ready` deltaP `16.594` edge `0.0186` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
