# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T23:37:19.825591+00:00`
- Price records: `498`
- Market context records: `591`
- Flow alert records: `1673`
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

- `market_context_high->crypto_alt_24h` score `4.6025` n `146` status `ready` deltaP `7.0265` edge `0.3415` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.4079` n `146` status `ready` deltaP `10.4375` edge `0.2478` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0902` n `146` status `ready` deltaP `11.7757` edge `0.0202` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2946` n `146` status `ready` deltaP `2.3595` edge `0.0043` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6031` n `146` status `ready` deltaP `1.6187` edge `0.0364` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6468` n `146` status `ready` deltaP `0.7548` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1525` n `146` status `ready` deltaP `-4.1262` edge `-0.0082` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2193` n `146` status `ready` deltaP `5.2743` edge `-0.0053` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2538` n `146` status `ready` deltaP `-1.8982` edge `-0.0108` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8332` n `146` status `ready` deltaP `4.7307` edge `-0.012` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1553` n `146` status `ready` deltaP `2.8307` edge `0.0585` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2636` n `146` status `ready` deltaP `0.0057` edge `-0.0364` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.3241` n `146` status `ready` deltaP `-6.4742` edge `0.049` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.8595` n `146` status `ready` deltaP `12.1668` edge `0.0512` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2922` n `146` status `ready` deltaP `-4.5477` edge `-0.0481` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3668` n `146` status `ready` deltaP `-3.9692` edge `-0.0389` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7541` n `146` status `ready` deltaP `-6.9668` edge `0.0837` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.3546` n `146` status `ready` deltaP `-10.3359` edge `-0.0335` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.3942` n `146` status `ready` deltaP `-3.8962` edge `-0.0202` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0908` n `146` status `ready` deltaP `0.6281` edge `-0.2406` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
