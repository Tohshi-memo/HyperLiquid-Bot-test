# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T04:07:33.964753+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11400`

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

- `news_risk_high->unknown_1h` score `444.1156` n `82` status `ready` deltaP `-5.6996` edge `37.0898` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.5984` n `82` status `ready` deltaP `38.444` edge `1.4257` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.2506` n `82` status `ready` deltaP `37.8512` edge `1.4156` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.3517` n `82` status `ready` deltaP `33.8225` edge `0.8985` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.9644` n `82` status `ready` deltaP `57.5946` edge `0.2974` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.605` n `67` status `ready` deltaP `39.8276` edge `0.2849` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.323` n `41` status `ready` deltaP `39.8276` edge `0.2614` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.323` n `41` status `ready` deltaP `39.8276` edge `0.2614` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5355` n `41` status `ready` deltaP `61.0093` edge `0.0588` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5355` n `41` status `ready` deltaP `61.0093` edge `0.0588` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.3691` n `82` status `ready` deltaP `32.0017` edge `0.2795` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8206` n `67` status `ready` deltaP `54.4931` edge `0.06` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9913` n `52` status `ready` deltaP `26.7472` edge `0.0226` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9913` n `52` status `ready` deltaP `26.7472` edge `0.0226` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7823` n `136` status `ready` deltaP `21.9961` edge `0.0437` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6688` n `137` status `ready` deltaP `11.7641` edge `0.015` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5912` n `82` status `ready` deltaP `15.2439` edge `0.037` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3639` n `136` status `ready` deltaP `12.4282` edge `0.0114` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.2046` n `137` status `ready` deltaP `5.9607` edge `0.0031` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1533` n `52` status `ready` deltaP `6.1493` edge `0.007` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
