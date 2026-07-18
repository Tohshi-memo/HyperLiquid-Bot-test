# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T07:37:27.669657+00:00`
- Price records: `672`
- Market context records: `7116`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.36` n `146` status `ready` deltaP `15.3086` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1172` n `147` status `ready` deltaP `4.1091` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1541` n `147` status `ready` deltaP `-0.5978` edge `0.047` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.5366` n `147` status `ready` deltaP `-0.0122` edge `-0.0066` maxDD `-2.3029`
- `market_context_high->crypto_major_1h` score `-0.5717` n `147` status `ready` deltaP `3.5918` edge `0.038` maxDD `-7.1523`
- `market_context_high->crypto_alt_1h` score `-0.6086` n `147` status `ready` deltaP `0.8707` edge `0.0309` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.8494` n `147` status `ready` deltaP `-4.1641` edge `-0.0195` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3827` n `146` status `ready` deltaP `-4.5794` edge `-0.0432` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4964` n `147` status `ready` deltaP `-6.3659` edge `-0.0057` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-1.5471` n `146` status `ready` deltaP `-6.8326` edge `0.0074` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0933` n `147` status `ready` deltaP `2.9268` edge `-0.0456` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-3.0415` n `146` status `ready` deltaP `4.0365` edge `0.0116` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.7088` n `146` status `ready` deltaP `-9.5082` edge `-0.1148` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.0842` n `146` status `ready` deltaP `-3.1866` edge `-0.0492` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.437` n `146` status `ready` deltaP `-9.1067` edge `-0.0122` maxDD `-5.414`
- `market_context_high->fx_24h` score `-4.6682` n `146` status `ready` deltaP `-12.5404` edge `-0.0227` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.6914` n `146` status `ready` deltaP `0.4636` edge `-0.0155` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.3771` n `146` status `ready` deltaP `-27.4567` edge `-0.0837` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.7038` n `146` status `ready` deltaP `-2.3472` edge `-0.2393` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7739` n `146` status `ready` deltaP `-27.1975` edge `-0.1595` maxDD `-42.2274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
