# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T13:37:30.481542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `18.1883` n `91` status `ready` deltaP `35.6513` edge `1.301` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.1883` n `91` status `ready` deltaP `35.6513` edge `1.301` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.5996` n `201` status `ready` deltaP `27.2155` edge `1.0346` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.5767` n `91` status `ready` deltaP `41.4885` edge `0.4753` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5767` n `91` status `ready` deltaP `41.4885` edge `0.4753` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.0814` n `91` status `ready` deltaP `31.2869` edge `0.4674` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.0814` n `91` status `ready` deltaP `31.2869` edge `0.4674` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.5789` n `91` status `ready` deltaP `24.5002` edge `1.0869` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.5789` n `91` status `ready` deltaP `24.5002` edge `1.0869` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.0288` n `201` status `ready` deltaP `20.6597` edge `0.198` maxDD `0.0`
- `risk_on_high->index_24h` score `3.5765` n `91` status `ready` deltaP `36.4602` edge `0.0592` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.5765` n `91` status `ready` deltaP `36.4602` edge `0.0592` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.7047` n `201` status `ready` deltaP `30.8017` edge `0.0594` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.5912` n `91` status `ready` deltaP `28.3151` edge `0.0365` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.5912` n `91` status `ready` deltaP `28.3151` edge `0.0365` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `2.4232` n `91` status `ready` deltaP `20.6597` edge `0.0642` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.4232` n `91` status `ready` deltaP `20.6597` edge `0.0642` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.5681` n `201` status `ready` deltaP `16.8895` edge `0.032` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.5519` n `91` status `ready` deltaP `16.556` edge `0.0283` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.5519` n `91` status `ready` deltaP `16.556` edge `0.0283` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
