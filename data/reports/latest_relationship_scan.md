# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T03:37:30.095834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.7253` n `104` status `ready` deltaP `29.3937` edge `0.9708` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.7253` n `104` status `ready` deltaP `29.3937` edge `0.9708` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.3525` n `226` status `ready` deltaP `21.812` edge `0.7167` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2284` n `104` status `ready` deltaP `37.2655` edge `0.3911` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2284` n `104` status `ready` deltaP `37.2655` edge `0.3911` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `6.0417` n `104` status `ready` deltaP `22.0886` edge `1.0341` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.0417` n `104` status `ready` deltaP `22.0886` edge `1.0341` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.0916` n `104` status `ready` deltaP `26.5596` edge `0.3331` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0916` n `104` status `ready` deltaP `26.5596` edge `0.3331` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9459` n `104` status `ready` deltaP `29.9279` edge `0.0502` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9459` n `104` status `ready` deltaP `29.9279` edge `0.0502` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.542` n `226` status `ready` deltaP `13.7153` edge `0.1204` maxDD `0.0`
- `market_context_high->index_24h` score `2.2848` n `226` status `ready` deltaP `24.8479` edge `0.0641` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.2424` n `104` status `ready` deltaP `13.7153` edge `0.0121` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2424` n `104` status `ready` deltaP `13.7153` edge `0.0121` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1826` n `104` status `ready` deltaP `5.1877` edge `0.0992` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1826` n `104` status `ready` deltaP `5.1877` edge `0.0992` maxDD `-1.1521`
- `risk_on_high->equity_4h` score `0.5038` n `104` status `ready` deltaP `17.3428` edge `-0.0264` maxDD `-1.7786`
- `risk_on_and_context->equity_4h` score `0.5038` n `104` status `ready` deltaP `17.3428` edge `-0.0264` maxDD `-1.7786`
- `risk_on_high->commodity_24h` score `0.4618` n `104` status `ready` deltaP `8.3734` edge `0.0269` maxDD `-0.8726`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
