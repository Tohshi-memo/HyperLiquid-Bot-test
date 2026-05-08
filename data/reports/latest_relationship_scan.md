# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T08:12:40.550285+00:00`
- Price records: `628`
- Market context records: `735`
- Flow alert records: `2076`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.3611` n `146` status `ready` deltaP `29.5628` edge `0.8664` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5187` n `146` status `ready` deltaP `7.7737` edge `0.4962` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.0589` n `146` status `ready` deltaP `0.7057` edge `0.1899` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3299` n `151` status `ready` deltaP `5.482` edge `0.0083` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.424` n `156` status `ready` deltaP `3.0107` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5549` n `156` status `ready` deltaP `1.7866` edge `0.0393` maxDD `-3.7959`
- `market_context_high->equity_24h` score `-0.7768` n `146` status `ready` deltaP `-0.9833` edge `0.2023` maxDD `-10.5047`
- `market_context_high->index_1h` score `-0.8979` n `156` status `ready` deltaP `1.0546` edge `0.0035` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-1.0311` n `151` status `ready` deltaP `17.0854` edge `0.1245` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0717` n `156` status `ready` deltaP `-0.8809` edge `-0.0024` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.1056` n `156` status `ready` deltaP `5.2885` edge `-0.0047` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4979` n `156` status `ready` deltaP `3.8462` edge `-0.019` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.6327` n `156` status `ready` deltaP `-5.1282` edge `-0.0247` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8584` n `151` status `ready` deltaP `1.0805` edge `-0.0098` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1187` n `151` status `ready` deltaP `2.3882` edge `0.0645` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7965` n `151` status `ready` deltaP `-1.88` edge `-0.0053` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1709` n `156` status `ready` deltaP `-4.0064` edge `-0.0416` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5849` n `151` status `ready` deltaP `-5.1968` edge `0.086` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9399` n `151` status `ready` deltaP `4.4086` edge `-0.1699` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.3064` n `146` status `ready` deltaP `-14.7935` edge `-0.0645` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
