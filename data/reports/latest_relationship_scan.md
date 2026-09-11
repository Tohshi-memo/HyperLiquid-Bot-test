# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T04:07:35.524105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11398`

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

- `news_risk_high->unknown_1h` score `893.6207` n `53` status `ready` deltaP `-9.1713` edge `74.5717` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `581.6047` n `41` status `ready` deltaP `-26.6768` edge `48.7177` maxDD `-2.824`
- `risk_on_high->crypto_alt_24h` score `20.8786` n `91` status `ready` deltaP `36.5194` edge `1.5194` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.8786` n `91` status `ready` deltaP `36.5194` edge `1.5194` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.6432` n `189` status `ready` deltaP `32.4901` edge `1.3364` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.9379` n `91` status `ready` deltaP `41.4885` edge `0.5054` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9379` n `91` status `ready` deltaP `41.4885` edge `0.5054` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.4979` n `189` status `ready` deltaP `30.7292` edge `0.5033` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.7777` n `91` status `ready` deltaP `32.5064` edge `0.5173` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7777` n `91` status `ready` deltaP `32.5064` edge `0.5173` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `7.3999` n `91` status `ready` deltaP `30.7292` edge `0.4118` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.3999` n `91` status `ready` deltaP `30.7292` edge `0.4118` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.2963` n `91` status `ready` deltaP `25.021` edge `1.1754` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2963` n `91` status `ready` deltaP `25.021` edge `1.1754` maxDD `-24.5429`
- `risk_on_high->index_24h` score `4.988` n `91` status `ready` deltaP `46.5297` edge `0.1097` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.988` n `91` status `ready` deltaP `46.5297` edge `0.1097` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.0108` n `189` status `ready` deltaP `40.3026` edge `0.1049` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.68` n `91` status `ready` deltaP `34.1078` edge `0.0886` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.68` n `91` status `ready` deltaP `34.1078` edge `0.0886` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5178` n `189` status `ready` deltaP `27.4737` edge `0.1122` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
