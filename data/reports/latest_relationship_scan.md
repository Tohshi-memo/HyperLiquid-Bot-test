# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T08:52:21.778954+00:00`
- Price records: `535`
- Market context records: `631`
- Flow alert records: `1786`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `5.657` n `146` status `ready` deltaP `16.3822` edge `0.3956` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2918` n `146` status `ready` deltaP `7.2878` edge `0.3972` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0696` n `146` status `ready` deltaP `9.2872` edge `0.0163` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3198` n `146` status `ready` deltaP `2.0106` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.507` n `146` status `ready` deltaP `2.0249` edge `0.0417` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7308` n `146` status `ready` deltaP `-0.7109` edge `-0.0036` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1373` n `146` status `ready` deltaP `-3.9806` edge `-0.0079` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2542` n `146` status `ready` deltaP `5.4382` edge `-0.0093` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3263` n `146` status `ready` deltaP `-2.6085` edge `-0.0121` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7817` n `146` status `ready` deltaP `5.1634` edge `-0.0106` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0315` n `146` status `ready` deltaP `4.2877` edge `0.0591` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3975` n `146` status `ready` deltaP `-1.5334` edge `-0.0373` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5039` n `146` status `ready` deltaP `13.5363` edge `0.0717` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0459` n `146` status `ready` deltaP `-8.3121` edge `0.0011` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.4231` n `146` status `ready` deltaP `-4.0577` edge `-0.043` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4503` n `146` status `ready` deltaP `-5.2641` edge `-0.0565` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.4986` n `146` status `ready` deltaP `-5.7534` edge `0.0969` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2929` n `146` status `ready` deltaP `-2.7272` edge `-0.015` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7639` n `146` status `ready` deltaP `1.8489` edge `-0.2215` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9716` n `146` status `ready` deltaP `-11.5541` edge `-0.0768` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
