# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T16:52:29.624688+00:00`
- Price records: `672`
- Market context records: `4742`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7454`

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

- `market_context_high->unknown_1h` score `80.7311` n `139` status `ready` deltaP `13.9125` edge `6.6766` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1893` n `136` status `ready` deltaP `13.0022` edge `0.4668` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.3125` n `127` status `ready` deltaP `16.3768` edge `0.2592` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.4039` n `136` status `ready` deltaP `7.3798` edge `0.0059` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.5706` n `139` status `ready` deltaP `1.7027` edge `0.0207` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.649` n `136` status `ready` deltaP `5.5775` edge `0.0482` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.933` n `136` status `ready` deltaP `-1.363` edge `-0.0031` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.947` n `139` status `ready` deltaP `-1.5282` edge `-0.0147` maxDD `-5.3889`
- `market_context_high->fx_1h` score `-1.2495` n `139` status `ready` deltaP `-4.8594` edge `-0.0052` maxDD `-0.9892`
- `market_context_high->index_1h` score `-1.5417` n `139` status `ready` deltaP `-3.0543` edge `-0.0077` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.765` n `136` status `ready` deltaP `6.7162` edge `0.0189` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.5884` n `139` status `ready` deltaP `-3.8115` edge `-0.07` maxDD `-15.5811`
- `market_context_high->crypto_alt_1h` score `-2.6011` n `139` status `ready` deltaP `0.3888` edge `-0.0382` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.1918` n `139` status `ready` deltaP `0.1766` edge `-0.0627` maxDD `-25.1479`
- `market_context_high->commodity_24h` score `-3.9152` n `127` status `ready` deltaP `17.2217` edge `0.0698` maxDD `-27.5371`
- `market_context_high->fx_24h` score `-4.4906` n `127` status `ready` deltaP `-14.4425` edge `-0.0201` maxDD `-4.9601`
- `market_context_high->crypto_alt_4h` score `-5.9994` n `136` status `ready` deltaP `0.6635` edge `-0.0566` maxDD `-52.0251`
- `market_context_high->index_24h` score `-7.5283` n `127` status `ready` deltaP `-11.3558` edge `-0.1039` maxDD `-24.8201`
- `market_context_high->metal_4h` score `-8.4467` n `136` status `ready` deltaP `2.2686` edge `-0.2725` maxDD `-61.3761`
- `market_context_high->crypto_major_4h` score `-8.8937` n `136` status `ready` deltaP `1.0222` edge `-0.1682` maxDD `-72.9735`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
