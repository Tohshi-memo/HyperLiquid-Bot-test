# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T11:52:19.033998+00:00`
- Price records: `672`
- Market context records: `973`
- Flow alert records: `2724`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.2078` n `150` status `ready` deltaP `34.8611` edge `1.0683` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.6611` n `150` status `ready` deltaP `11.4583` edge `0.7287` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2784` n `150` status `ready` deltaP `0.8264` edge `0.3615` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5939` n `150` status `ready` deltaP `-0.9444` edge `0.2553` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2379` n `209` status `ready` deltaP `3.3536` edge `0.0386` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3777` n `209` status `ready` deltaP `1.2814` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6374` n `209` status `ready` deltaP `1.267` edge `0.0153` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6439` n `197` status `ready` deltaP `2.2339` edge `0.0022` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7299` n `209` status `ready` deltaP `2.9137` edge `0.0051` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.111` n `209` status `ready` deltaP `5.6492` edge `-0.0078` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.2077` n `209` status `ready` deltaP `-1.4662` edge `-0.0137` maxDD `-3.5069`
- `market_context_high->crypto_alt_1h` score `-1.3294` n `209` status `ready` deltaP `0.1103` edge `-0.0272` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5059` n `197` status `ready` deltaP `0.7367` edge `0.0848` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6734` n `197` status `ready` deltaP `-1.4966` edge `0.0228` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8326` n `209` status `ready` deltaP `-1.4132` edge `-0.0296` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.5296` n `197` status `ready` deltaP `8.8801` edge `0.1006` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.9297` n `197` status `ready` deltaP `-0.9564` edge `0.079` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.1508` n `197` status `ready` deltaP `8.0174` edge `-0.1282` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.1868` n `197` status `ready` deltaP `-1.1337` edge `0.0198` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0034` n `150` status `ready` deltaP `5.0139` edge `0.0039` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
