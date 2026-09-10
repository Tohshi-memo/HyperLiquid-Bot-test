# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T20:22:38.119863+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11822`

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

- `risk_on_high->crypto_alt_24h` score `20.0132` n `91` status `ready` deltaP `36.1722` edge `1.4496` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.0132` n `91` status `ready` deltaP `36.1722` edge `1.4496` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.4245` n `201` status `ready` deltaP `27.7364` edge `1.1832` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0521` n `91` status `ready` deltaP `42.5556` edge `0.5078` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0521` n `91` status `ready` deltaP `42.5556` edge `0.5078` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.7541` n `91` status `ready` deltaP `32.8113` edge `0.5133` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7541` n `91` status `ready` deltaP `32.8113` edge `0.5133` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2565` n `91` status `ready` deltaP `25.021` edge `1.1703` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2565` n `91` status `ready` deltaP `25.021` edge `1.1703` maxDD `-24.5429`
- `market_context_high->equity_24h` score `6.3958` n `201` status `ready` deltaP `25.3472` edge `0.364` maxDD `0.0`
- `risk_on_high->equity_24h` score `4.8022` n `91` status `ready` deltaP `25.3472` edge `0.2312` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.8022` n `91` status `ready` deltaP `25.3472` edge `0.2312` maxDD `0.0`
- `risk_on_high->index_24h` score `4.2443` n `91` status `ready` deltaP `41.1477` edge `0.0836` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.2443` n `91` status `ready` deltaP `41.1477` edge `0.0836` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.3725` n `201` status `ready` deltaP `35.4892` edge `0.0838` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.0772` n `91` status `ready` deltaP `30.1444` edge `0.0648` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `3.0772` n `91` status `ready` deltaP `30.1444` edge `0.0648` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.9515` n `201` status `ready` deltaP `23.305` edge `0.0928` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.5181` n `91` status `ready` deltaP `20.1356` edge `0.0201` maxDD `-0.2263`
- `risk_on_and_context->equity_1h` score `1.5181` n `91` status `ready` deltaP `20.1356` edge `0.0201` maxDD `-0.2263`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
