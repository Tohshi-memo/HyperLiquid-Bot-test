# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T23:07:26.709488+00:00`
- Price records: `672`
- Market context records: `7191`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->crypto_major_4h` score `6.1935` n `34` status `ready` deltaP `28.9096` edge `0.3617` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.1935` n `34` status `ready` deltaP `28.9096` edge `0.3617` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.477` n `34` status `ready` deltaP `18.6245` edge `0.2882` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.477` n `34` status `ready` deltaP `18.6245` edge `0.2882` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.052` n `34` status `ready` deltaP `22.1293` edge `0.0385` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.052` n `34` status `ready` deltaP `22.1293` edge `0.0385` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.4313` n `34` status `ready` deltaP `8.3393` edge `0.148` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.4313` n `34` status `ready` deltaP `8.3393` edge `0.148` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3947` n `34` status `ready` deltaP `8.6738` edge `0.0218` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3947` n `34` status `ready` deltaP `8.6738` edge `0.0218` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3874` n `34` status `ready` deltaP `4.2444` edge `0.034` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3874` n `34` status `ready` deltaP `4.2444` edge `0.034` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.2854` n `34` status `ready` deltaP `4.2863` edge `-0.0053` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.2854` n `34` status `ready` deltaP `4.2863` edge `-0.0053` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2907` n `178` status `ready` deltaP `3.5575` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.5218` n `178` status `ready` deltaP `5.4683` edge `0.0377` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5994` n `178` status `ready` deltaP `0.4861` edge `0.0238` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.6015` n `178` status `ready` deltaP `-0.4087` edge `-0.0123` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.6988` n `34` status `ready` deltaP `-0.4753` edge `-0.0123` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.6988` n `34` status `ready` deltaP `-0.4753` edge `-0.0123` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
