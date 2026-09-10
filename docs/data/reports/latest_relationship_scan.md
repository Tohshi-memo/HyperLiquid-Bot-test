# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T21:22:28.114466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11770`

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

- `risk_on_high->crypto_alt_24h` score `20.1296` n `91` status `ready` deltaP `36.1722` edge `1.4593` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.1296` n `91` status `ready` deltaP `36.1722` edge `1.4593` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5409` n `201` status `ready` deltaP `27.7364` edge `1.1929` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9495` n `91` status `ready` deltaP `42.0983` edge `0.5023` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9495` n `91` status `ready` deltaP `42.0983` edge `0.5023` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.6563` n `91` status `ready` deltaP `32.3539` edge `0.5082` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6563` n `91` status `ready` deltaP `32.3539` edge `0.5082` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2526` n `91` status `ready` deltaP `25.021` edge `1.1698` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2526` n `91` status `ready` deltaP `25.021` edge `1.1698` maxDD `-24.5429`
- `market_context_high->equity_24h` score `6.7441` n `201` status `ready` deltaP `26.0417` edge `0.3884` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.1481` n `91` status `ready` deltaP `26.0417` edge `0.2554` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.1481` n `91` status `ready` deltaP `26.0417` edge `0.2554` maxDD `0.0`
- `risk_on_high->index_24h` score `4.343` n `91` status `ready` deltaP `41.8422` edge `0.0872` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.343` n `91` status `ready` deltaP `41.8422` edge `0.0872` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.4713` n `201` status `ready` deltaP `36.1837` edge `0.0874` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.1765` n `91` status `ready` deltaP `30.7542` edge `0.069` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.1765` n `91` status `ready` deltaP `30.7542` edge `0.069` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.0519` n `201` status `ready` deltaP `23.9148` edge `0.0971` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.504` n `91` status `ready` deltaP `19.9859` edge `0.0199` maxDD `-0.2246`
- `risk_on_and_context->equity_1h` score `1.504` n `91` status `ready` deltaP `19.9859` edge `0.0199` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
