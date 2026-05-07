# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T09:37:23.690865+00:00`
- Price records: `538`
- Market context records: `634`
- Flow alert records: `1795`
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

- `market_context_high->crypto_major_24h` score `5.9044` n `146` status `ready` deltaP `16.8939` edge `0.4128` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.3943` n `146` status `ready` deltaP `7.2337` edge `0.4061` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0874` n `146` status `ready` deltaP `8.9914` edge `0.016` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3362` n `146` status `ready` deltaP `1.755` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4881` n `146` status `ready` deltaP `2.0961` edge `0.0428` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7072` n `146` status `ready` deltaP `-0.3619` edge `-0.0029` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1397` n `146` status `ready` deltaP `-4.0557` edge `-0.0076` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2295` n `146` status `ready` deltaP `5.5821` edge `-0.0082` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3253` n `146` status `ready` deltaP `-2.626` edge `-0.0119` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7333` n `146` status `ready` deltaP `5.4691` edge `-0.0086` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0752` n `146` status `ready` deltaP `4.1017` edge `0.0567` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.413` n `146` status `ready` deltaP `-1.7269` edge `-0.0373` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5386` n `146` status `ready` deltaP `13.2971` edge `0.0704` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0531` n `146` status `ready` deltaP `-8.4475` edge `0.0014` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.4201` n `146` status `ready` deltaP `-5.5217` edge `0.1019` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4332` n `146` status `ready` deltaP `-5.1255` edge `-0.056` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4506` n `146` status `ready` deltaP `-4.2365` edge `-0.0441` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.3289` n `146` status `ready` deltaP `-3.1964` edge `-0.0165` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7815` n `146` status `ready` deltaP `1.6296` edge `-0.2215` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9368` n `146` status `ready` deltaP `-11.6438` edge `-0.0733` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
