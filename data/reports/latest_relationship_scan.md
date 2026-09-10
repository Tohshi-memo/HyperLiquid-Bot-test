# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T17:22:32.863491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11967`

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

- `risk_on_high->crypto_alt_24h` score `19.4324` n `91` status `ready` deltaP `36.1722` edge `1.4012` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.4324` n `91` status `ready` deltaP `36.1722` edge `1.4012` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.8437` n `201` status `ready` deltaP `27.7364` edge `1.1348` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.2054` n `91` status `ready` deltaP `43.3178` edge `0.5155` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.2054` n `91` status `ready` deltaP `43.3178` edge `0.5155` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.8531` n `91` status `ready` deltaP `33.2686` edge `0.5185` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8531` n `91` status `ready` deltaP `33.2686` edge `0.5185` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.1169` n `91` status `ready` deltaP `25.021` edge `1.1524` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.1169` n `91` status `ready` deltaP `25.021` edge `1.1524` maxDD `-24.5429`
- `market_context_high->equity_24h` score `5.3603` n `201` status `ready` deltaP `23.2639` edge `0.2916` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9564` n `91` status `ready` deltaP `39.0644` edge `0.0735` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.9564` n `91` status `ready` deltaP `39.0644` edge `0.0735` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.7667` n `91` status `ready` deltaP `23.2639` edge `0.1588` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.7667` n `91` status `ready` deltaP `23.2639` edge `0.1588` maxDD `0.0`
- `market_context_high->index_24h` score `3.0846` n `201` status `ready` deltaP `33.4059` edge `0.0737` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.98` n `91` status `ready` deltaP `30.1444` edge `0.0567` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.98` n `91` status `ready` deltaP `30.1444` edge `0.0567` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.8543` n `201` status `ready` deltaP `23.305` edge `0.0847` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.5393` n `91` status `ready` deltaP `6.197` edge `0.1222` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.5393` n `91` status `ready` deltaP `6.197` edge `0.1222` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
