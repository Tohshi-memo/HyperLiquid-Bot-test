# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T22:37:37.456316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11376`

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

- `news_risk_high->unknown_1h` score `1959.6928` n `31` status `ready` deltaP `2.8009` edge `163.3126` maxDD `-0.8832`
- `risk_on_high->crypto_alt_24h` score `20.1512` n `91` status `ready` deltaP `36.1722` edge `1.4611` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.1512` n `91` status `ready` deltaP `36.1722` edge `1.4611` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5625` n `201` status `ready` deltaP `27.7364` edge `1.1947` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8735` n `91` status `ready` deltaP `41.7934` edge `0.498` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8735` n `91` status `ready` deltaP `41.7934` edge `0.498` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.5839` n `91` status `ready` deltaP `32.0491` edge `0.5042` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.5839` n `91` status `ready` deltaP `32.0491` edge `0.5042` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2152` n `91` status `ready` deltaP `25.021` edge `1.165` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2152` n `91` status `ready` deltaP `25.021` edge `1.165` maxDD `-24.5429`
- `market_context_high->equity_24h` score `7.1952` n `201` status `ready` deltaP `26.9097` edge `0.4202` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.5992` n `91` status `ready` deltaP `26.9097` edge `0.2872` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.5992` n `91` status `ready` deltaP `26.9097` edge `0.2872` maxDD `0.0`
- `risk_on_high->index_24h` score `4.4653` n `91` status `ready` deltaP `42.7102` edge `0.0916` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.4653` n `91` status `ready` deltaP `42.7102` edge `0.0916` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.5935` n `201` status `ready` deltaP `37.0517` edge `0.0918` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.3059` n `91` status `ready` deltaP `31.5164` edge `0.0747` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.3059` n `91` status `ready` deltaP `31.5164` edge `0.0747` maxDD `-0.079`
- `news_risk_high->commodity_1h` score `2.5161` n `31` status `ready` deltaP `22.4793` edge `0.073` maxDD `-0.0547`
- `market_context_high->equity_4h` score `2.1813` n `201` status `ready` deltaP `24.677` edge `0.1028` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
