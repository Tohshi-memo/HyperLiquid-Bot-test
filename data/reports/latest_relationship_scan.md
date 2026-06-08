# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T02:37:30.232329+00:00`
- Price records: `672`
- Market context records: `3240`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.2794` n `103` status `ready` deltaP `18.6505` edge `2.6905` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.6745` n `103` status `ready` deltaP `49.2095` edge `0.8543` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.6558` n `103` status `ready` deltaP `32.0102` edge `0.8467` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.587` n `103` status `ready` deltaP `19.3956` edge `1.5568` maxDD `-53.663`
- `risk_on_high->crypto_major_1h` score `2.6328` n `31` status `ready` deltaP `10.8267` edge `0.3723` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.6328` n `31` status `ready` deltaP `10.8267` edge `0.3723` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.5393` n `103` status `ready` deltaP `22.7211` edge `2.244` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.8351` n `138` status `ready` deltaP `16.8964` edge `0.1361` maxDD `-3.9989`
- `risk_on_high->crypto_alt_1h` score `0.7472` n `31` status `ready` deltaP `4.0081` edge `0.2128` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7472` n `31` status `ready` deltaP `4.0081` edge `0.2128` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4655` n `31` status `ready` deltaP `7.9148` edge `0.0754` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4655` n `31` status `ready` deltaP `7.9148` edge `0.0754` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3422` n `31` status `ready` deltaP `2.6608` edge `0.1165` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3422` n `31` status `ready` deltaP `2.6608` edge `0.1165` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1024` n `31` status `ready` deltaP `0.1835` edge `0.048` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1024` n `31` status `ready` deltaP `0.1835` edge `0.048` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.4277` n `150` status `ready` deltaP `3.483` edge `0.0227` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.5044` n `150` status `ready` deltaP `3.7964` edge `0.0163` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.5242` n `138` status `ready` deltaP `9.7296` edge `0.0945` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7738` n `150` status `ready` deltaP `3.988` edge `0.1005` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
