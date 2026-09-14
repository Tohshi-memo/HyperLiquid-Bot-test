# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T02:37:26.705685+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11352`

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

- `news_risk_high->unknown_1h` score `444.5224` n `82` status `ready` deltaP `-5.5499` edge `37.1227` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.371` n `82` status `ready` deltaP `37.582` edge `1.4125` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3652` n `82` status `ready` deltaP `38.0236` edge `1.424` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.0169` n `82` status `ready` deltaP `32.7881` edge `0.8775` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.8241` n `82` status `ready` deltaP `56.5601` edge `0.2926` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.3206` n `61` status `ready` deltaP `39.8276` edge `0.2612` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.0926` n `38` status `ready` deltaP `39.8276` edge `0.2422` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0926` n `38` status `ready` deltaP `39.8276` edge `0.2422` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6077` n `38` status `ready` deltaP `61.8512` edge `0.0592` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6077` n `38` status `ready` deltaP `61.8512` edge `0.0592` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.2396` n `82` status `ready` deltaP `30.9672` edge `0.2756` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.846` n `61` status `ready` deltaP `54.6467` edge `0.0611` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9853` n `52` status `ready` deltaP `26.7472` edge `0.0221` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9853` n `52` status `ready` deltaP `26.7472` edge `0.0221` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6949` n `130` status `ready` deltaP `20.978` edge `0.0432` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6963` n `137` status `ready` deltaP `12.0635` edge `0.0153` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5643` n `82` status `ready` deltaP `14.7866` edge `0.0366` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3419` n `130` status `ready` deltaP `11.9747` edge `0.0116` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
