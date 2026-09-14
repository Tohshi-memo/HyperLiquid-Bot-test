# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T03:22:30.230631+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11376`

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

- `news_risk_high->unknown_1h` score `444.436` n `82` status `ready` deltaP `-5.5499` edge `37.1155` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.5312` n `82` status `ready` deltaP `38.0992` edge `1.4224` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.352` n `82` status `ready` deltaP `38.0236` edge `1.4229` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.1879` n `82` status `ready` deltaP `33.3053` edge `0.8883` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.893` n `82` status `ready` deltaP `57.0773` edge `0.2949` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.467` n `64` status `ready` deltaP `39.8276` edge `0.2734` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.3602` n `41` status `ready` deltaP `39.8276` edge `0.2645` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3602` n `41` status `ready` deltaP `39.8276` edge `0.2645` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5997` n `41` status `ready` deltaP `61.5265` edge `0.0607` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5997` n `41` status `ready` deltaP `61.5265` edge `0.0607` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.3061` n `82` status `ready` deltaP `31.4845` edge `0.2777` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8439` n `64` status `ready` deltaP `54.5905` edge `0.0613` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9913` n `52` status `ready` deltaP `26.7472` edge `0.0226` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9913` n `52` status `ready` deltaP `26.7472` edge `0.0226` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7401` n `133` status `ready` deltaP `21.4985` edge `0.0435` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6688` n `137` status `ready` deltaP `11.7641` edge `0.015` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5817` n `82` status `ready` deltaP `15.0914` edge `0.0368` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3746` n `133` status `ready` deltaP `12.5894` edge `0.0117` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1914` n `137` status `ready` deltaP `5.811` edge `0.003` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1533` n `52` status `ready` deltaP `6.1493` edge `0.007` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
