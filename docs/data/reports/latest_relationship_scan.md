# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T08:52:30.120922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11870`

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

- `risk_on_high->crypto_alt_24h` score `15.276` n `91` status `ready` deltaP `32.3527` edge `1.0803` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.276` n `91` status `ready` deltaP `32.3527` edge `1.0803` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `11.0895` n `205` status `ready` deltaP `24.1887` edge `0.8456` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.6276` n `91` status `ready` deltaP `38.7446` edge `0.4145` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.6276` n `91` status `ready` deltaP `38.7446` edge `0.4145` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.7314` n `91` status `ready` deltaP `28.543` edge `0.3732` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.7314` n `91` status `ready` deltaP `28.543` edge `0.3732` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.6797` n `91` status `ready` deltaP `21.2016` edge `0.8654` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.6797` n `91` status `ready` deltaP `21.2016` edge `0.8654` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.0438` n `91` status `ready` deltaP `33.1616` edge `0.0368` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.0438` n `91` status `ready` deltaP `33.1616` edge `0.0368` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.7869` n `205` status `ready` deltaP `17.3611` edge `0.1165` maxDD `0.0`
- `market_context_high->index_24h` score `2.4524` n `205` status `ready` deltaP `27.6778` edge `0.0592` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9411` n `91` status `ready` deltaP `18.4657` edge `0.048` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9411` n `91` status `ready` deltaP `18.4657` edge `0.048` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.8569` n `91` status `ready` deltaP `25.5712` edge `-0.0064` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.8569` n `91` status `ready` deltaP `25.5712` edge `-0.0064` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.335` n `205` status `ready` deltaP `17.013` edge `0.0432` maxDD `-1.2965`
- `risk_on_high->equity_1h` score `1.1258` n `91` status `ready` deltaP `17.8901` edge `0.0024` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1258` n `91` status `ready` deltaP `17.8901` edge `0.0024` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
