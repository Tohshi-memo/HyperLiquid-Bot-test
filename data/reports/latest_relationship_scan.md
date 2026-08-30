# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T07:52:26.101087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `9.0624` n `59` status `ready` deltaP `22.8374` edge `0.6458` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.0624` n `59` status `ready` deltaP `22.8374` edge `0.6458` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.2836` n `154` status `ready` deltaP `19.0074` edge `0.3606` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5509` n `91` status `ready` deltaP `31.4942` edge `0.2712` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.1854` n `59` status `ready` deltaP `23.07` edge `0.2233` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.1854` n `59` status `ready` deltaP `23.07` edge `0.2233` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.7752` n `59` status `ready` deltaP `9.6113` edge `0.2708` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.7752` n `59` status `ready` deltaP `9.6113` edge `0.2708` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.2586` n `59` status `ready` deltaP `29.5809` edge `0.093` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.2586` n `59` status `ready` deltaP `29.5809` edge `0.093` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.658` n `59` status `ready` deltaP `32.3429` edge `0.0144` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.658` n `59` status `ready` deltaP `32.3429` edge `0.0144` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.6229` n `154` status `ready` deltaP `10.899` edge `0.1868` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `1.8657` n `59` status `ready` deltaP `12.1021` edge `0.2068` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `1.8657` n `59` status `ready` deltaP `12.1021` edge `0.2068` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.7674` n `59` status `ready` deltaP `22.2096` edge `0.029` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7674` n `59` status `ready` deltaP `22.2096` edge `0.029` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7263` n `59` status `ready` deltaP `22.8281` edge `0.0087` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7263` n `59` status `ready` deltaP `22.8281` edge `0.0087` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.2362` n `59` status `ready` deltaP `16.2946` edge `0.0178` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
