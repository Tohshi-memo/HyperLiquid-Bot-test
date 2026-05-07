# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T11:37:16.622565+00:00`
- Price records: `546`
- Market context records: `642`
- Flow alert records: `1820`
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

- `market_context_high->crypto_major_24h` score `6.6889` n `146` status `ready` deltaP `18.2252` edge `0.4693` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.896` n `146` status `ready` deltaP `8.8707` edge `0.437` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.127` n `146` status `ready` deltaP `8.4093` edge `0.0148` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3419` n `146` status `ready` deltaP `1.6448` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4834` n `146` status `ready` deltaP `2.0344` edge `0.0436` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6802` n `146` status `ready` deltaP `-0.0076` edge `-0.0018` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1628` n `146` status `ready` deltaP `-4.3749` edge `-0.0074` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2047` n `146` status `ready` deltaP `5.712` edge `-0.007` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3055` n `146` status `ready` deltaP `-2.424` edge `-0.0116` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6761` n `146` status `ready` deltaP `5.899` edge `-0.0067` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0978` n `146` status `ready` deltaP `3.8046` edge `0.0568` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2933` n `146` status `ready` deltaP `-0.711` edge `-0.0341` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4627` n `146` status `ready` deltaP `13.6159` edge `0.0746` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9829` n `146` status `ready` deltaP `-8.7997` edge `0.0096` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3057` n `146` status `ready` deltaP `-4.9169` edge `0.1074` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4275` n `146` status `ready` deltaP `-5.0094` edge `-0.0563` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4467` n `146` status `ready` deltaP `-4.3231` edge `-0.0432` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.4306` n `146` status `ready` deltaP `-4.4168` edge `-0.0214` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7037` n `146` status `ready` deltaP `-11.2046` edge `-0.0568` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8249` n `146` status `ready` deltaP `1.0571` edge `-0.2213` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
