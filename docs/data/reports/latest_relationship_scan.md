# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T04:37:30.680436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11416`

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

- `news_risk_high->unknown_1h` score `842.8352` n `55` status `ready` deltaP `-8.1546` edge `70.3328` maxDD `-1.7068`
- `news_risk_high->unknown_4h` score `449.3402` n `43` status `ready` deltaP `-28.5274` edge `37.7211` maxDD `-3.8719`
- `risk_on_high->crypto_alt_24h` score `20.9326` n `91` status `ready` deltaP `36.5194` edge `1.5239` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.9326` n `91` status `ready` deltaP `36.5194` edge `1.5239` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `17.9666` n `187` status `ready` deltaP `33.4578` edge `1.3569` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8811` n `91` status `ready` deltaP `41.1837` edge `0.5027` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8811` n `91` status `ready` deltaP `41.1837` edge `0.5027` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.5881` n `187` status `ready` deltaP `31.0764` edge `0.5085` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.7209` n `91` status `ready` deltaP `32.2015` edge `0.5146` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7209` n `91` status `ready` deltaP `32.2015` edge `0.5146` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `7.5513` n `91` status `ready` deltaP `31.0764` edge `0.4221` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.5513` n `91` status `ready` deltaP `31.0764` edge `0.4221` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.2924` n `91` status `ready` deltaP `25.021` edge `1.1749` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2924` n `91` status `ready` deltaP `25.021` edge `1.1749` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.0302` n `91` status `ready` deltaP `46.8769` edge `0.1109` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0302` n `91` status `ready` deltaP `46.8769` edge `0.1109` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.046` n `187` status `ready` deltaP `40.5479` edge `0.1062` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.7164` n `91` status `ready` deltaP `34.4127` edge `0.0896` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.7164` n `91` status `ready` deltaP `34.4127` edge `0.0896` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.5333` n `187` status `ready` deltaP `27.6371` edge `0.1124` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
