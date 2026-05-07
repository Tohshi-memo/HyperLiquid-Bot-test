# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T16:22:19.186476+00:00`
- Price records: `565`
- Market context records: `662`
- Flow alert records: `1879`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `848`

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

- `market_context_high->crypto_major_24h` score `8.2377` n `146` status `ready` deltaP `21.2051` edge `0.5785` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3516` n `146` status `ready` deltaP `8.91` edge `0.4747` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1621` n `146` status `ready` deltaP `7.944` edge `0.0134` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3439` n `147` status `ready` deltaP `1.6671` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.471` n `147` status `ready` deltaP `2.1593` edge `0.0438` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5931` n `147` status `ready` deltaP `0.9013` edge `0.0033` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1464` n `147` status `ready` deltaP `-4.1398` edge `-0.0076` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1751` n `147` status `ready` deltaP `-1.5743` edge `-0.0064` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.1911` n `147` status `ready` deltaP `5.6568` edge `-0.0055` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5897` n `147` status `ready` deltaP `6.0643` edge `-0.0006` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8132` n `146` status `ready` deltaP `4.8868` edge `0.0733` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.9347` n `146` status `ready` deltaP `1.5823` edge `-0.0195` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-1.9595` n `146` status `ready` deltaP `15.4515` edge `0.1043` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.8131` n `146` status `ready` deltaP `-8.9424` edge `0.0247` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.0671` n `146` status `ready` deltaP `-2.6379` edge `-0.0228` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.1883` n `146` status `ready` deltaP `-4.469` edge `0.1142` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.3871` n `147` status `ready` deltaP `-5.1948` edge `-0.0517` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-4.6004` n `146` status `ready` deltaP `-11.3242` edge `-0.0474` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6405` n `146` status `ready` deltaP `-7.1469` edge `-0.0301` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7167` n `146` status `ready` deltaP `1.4035` edge `-0.2146` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
