# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T23:31:04.098689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `93.6681` n `81` status `ready` deltaP `-31.848` edge `12.4894` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `5.2962` n `81` status `ready` deltaP `36.1497` edge `0.224` maxDD `-0.2251`
- `market_context_high->commodity_4h` score `1.0658` n `109` status `ready` deltaP `12.244` edge `0.0543` maxDD `-0.7687`
- `market_context_high->metal_4h` score `-0.2177` n `109` status `ready` deltaP `15.4509` edge `0.0098` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.2442` n `113` status `ready` deltaP `1.2877` edge `0.0122` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.3255` n `113` status `ready` deltaP `1.1645` edge `0.0016` maxDD `-0.2527`
- `market_context_high->index_24h` score `-0.4863` n `81` status `ready` deltaP `8.9699` edge `-0.0447` maxDD `-0.7831`
- `market_context_high->metal_1h` score `-0.5132` n `113` status `ready` deltaP `1.4506` edge `-0.0039` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.5286` n `109` status `ready` deltaP `2.4628` edge `0.0` maxDD `-0.504`
- `market_context_high->crypto_major_4h` score `-0.5987` n `109` status `ready` deltaP `3.211` edge `0.0055` maxDD `-3.9599`
- `market_context_high->index_1h` score `-0.6375` n `113` status `ready` deltaP `-4.2247` edge `-0.0014` maxDD `-0.5064`
- `market_context_high->crypto_major_24h` score `-1.0092` n `81` status `ready` deltaP `-3.6266` edge `0.1392` maxDD `-14.219`
- `market_context_high->index_4h` score `-1.1895` n `109` status `ready` deltaP `-9.9015` edge `-0.0056` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-1.1959` n `113` status `ready` deltaP `-5.017` edge `-0.0215` maxDD `-3.8701`
- `market_context_high->crypto_alt_1h` score `-1.7209` n `113` status `ready` deltaP `-4.4314` edge `-0.0117` maxDD `-4.5069`
- `market_context_high->fx_24h` score `-2.4011` n `81` status `ready` deltaP `-20.0232` edge `-0.0136` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.4072` n `81` status `ready` deltaP `-14.1783` edge `0.0371` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-2.429` n `113` status `ready` deltaP `-9.5609` edge `-0.0434` maxDD `-4.289`
- `market_context_high->equity_24h` score `-4.7463` n `81` status `ready` deltaP `3.26` edge `-0.2878` maxDD `-21.7277`
- `market_context_high->crypto_alt_4h` score `-5.2674` n `109` status `ready` deltaP `-6.1185` edge `-0.03` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
