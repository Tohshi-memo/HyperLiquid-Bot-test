# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T15:37:33.245491+00:00`
- Price records: `466`
- Market context records: `556`
- Flow alert records: `1571`
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

- `market_context_high->crypto_alt_24h` score `4.9643` n `140` status `ready` deltaP `7.6641` edge `0.3674` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0142` n `140` status `ready` deltaP `10.0772` edge `0.2174` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0141` n `146` status `ready` deltaP `10.2371` edge `0.0207` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3094` n `146` status `ready` deltaP `2.0458` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5195` n `146` status `ready` deltaP `2.0937` edge `0.0402` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6087` n `146` status `ready` deltaP `1.3519` edge `-0.0017` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1373` n `146` status `ready` deltaP `-0.8315` edge `-0.0082` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2` n `146` status `ready` deltaP `-3.7152` edge `-0.0149` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3058` n `146` status `ready` deltaP `4.6433` edge `-0.0083` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7796` n `140` status `ready` deltaP `-5.7884` edge `0.0898` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9989` n `146` status `ready` deltaP `3.5284` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0903` n `146` status `ready` deltaP `1.1672` edge `-0.0297` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.4693` n `146` status `ready` deltaP `1.6956` edge `0.0399` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.1096` n `146` status `ready` deltaP `-2.8687` edge `-0.0248` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3864` n `146` status `ready` deltaP `-5.4854` edge `-0.0497` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5274` n `146` status `ready` deltaP `-5.8879` edge `0.0954` maxDD `-13.0076`
- `market_context_high->crypto_major_4h` score `-3.5773` n `146` status `ready` deltaP `9.0289` edge `0.0123` maxDD `-22.648`
- `market_context_high->equity_24h` score `-3.6873` n `140` status `ready` deltaP `-10.1405` edge `0.0208` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.2802` n `146` status `ready` deltaP `0.3653` edge `-0.1713` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.3793` n `140` status `ready` deltaP `-5.5191` edge `-0.0417` maxDD `-18.3035`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
