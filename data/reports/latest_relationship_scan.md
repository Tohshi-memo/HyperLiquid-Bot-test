# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T07:37:25.831040+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10942`

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

- `risk_on_high->crypto_alt_24h` score `14.5058` n `91` status `ready` deltaP `31.4847` edge `1.0219` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.5058` n `91` status `ready` deltaP `31.4847` edge `1.0219` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `10.5804` n `210` status `ready` deltaP `23.6459` edge `0.8068` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.502` n `91` status `ready` deltaP `38.1349` edge `0.4081` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.502` n `91` status `ready` deltaP `38.1349` edge `0.4081` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.5999` n `91` status `ready` deltaP `27.9332` edge `0.3663` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.5999` n `91` status `ready` deltaP `27.9332` edge `0.3663` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.1657` n `91` status `ready` deltaP `20.3335` edge `0.8053` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.1657` n `91` status `ready` deltaP `20.3335` edge `0.8053` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9251` n `91` status `ready` deltaP `32.2936` edge `0.0327` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9251` n `91` status `ready` deltaP `32.2936` edge `0.0327` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.739` n `210` status `ready` deltaP `16.4931` edge `0.1183` maxDD `0.0`
- `market_context_high->index_24h` score `2.4213` n `210` status `ready` deltaP `27.0189` edge `0.061` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9543` n `91` status `ready` deltaP `18.4657` edge `0.0491` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9543` n `91` status `ready` deltaP `18.4657` edge `0.0491` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.8653` n `91` status `ready` deltaP `25.5712` edge `-0.0057` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.8653` n `91` status `ready` deltaP `25.5712` edge `-0.0057` maxDD `-0.0802`
- `risk_on_high->equity_1h` score `1.1174` n `91` status `ready` deltaP `17.7404` edge `0.0027` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1174` n `91` status `ready` deltaP `17.7404` edge `0.0027` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.1028` n `91` status `ready` deltaP `4.5503` edge `0.0968` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
