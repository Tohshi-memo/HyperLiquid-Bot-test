# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T07:37:16.660371+00:00`
- Price records: `530`
- Market context records: `626`
- Flow alert records: `1771`
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

- `market_context_high->crypto_major_24h` score `5.3607` n `146` status `ready` deltaP `15.5135` edge `0.3767` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2283` n `146` status `ready` deltaP `7.3796` edge `0.3913` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0758` n `146` status `ready` deltaP `9.1996` edge `0.0161` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3041` n `146` status `ready` deltaP `2.2516` edge `0.0038` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4995` n `146` status `ready` deltaP `1.9682` edge `0.0427` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7316` n `146` status `ready` deltaP `-0.7269` edge `-0.0036` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1086` n `146` status `ready` deltaP `-3.7267` edge `-0.0072` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2474` n `146` status `ready` deltaP `5.4482` edge `-0.0088` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3575` n `146` status `ready` deltaP `-2.8342` edge `-0.0132` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7751` n `146` status `ready` deltaP `5.2164` edge `-0.0104` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8371` n `146` status `ready` deltaP `4.6026` edge `0.0732` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3557` n `146` status `ready` deltaP `-1.206` edge `-0.036` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3695` n `146` status `ready` deltaP `13.9411` edge `0.0802` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9147` n `146` status `ready` deltaP `-8.0822` edge `0.0105` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.3569` n `146` status `ready` deltaP `-3.755` edge `-0.0395` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4119` n `146` status `ready` deltaP `-5.055` edge `-0.0547` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6104` n `146` status `ready` deltaP `-6.1456` edge `0.0902` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2534` n `146` status `ready` deltaP `-2.1631` edge `-0.0137` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7006` n `146` status `ready` deltaP `2.22` edge `-0.2187` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.8946` n `146` status `ready` deltaP `-11.4017` edge `-0.0714` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
