# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T04:22:29.264424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11460`

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

- `news_risk_high->unknown_1h` score `443.884` n `82` status `ready` deltaP `-5.8493` edge `37.0715` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.6242` n `82` status `ready` deltaP `38.6165` edge `1.4267` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.2068` n `82` status `ready` deltaP `37.6788` edge `1.4131` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.4087` n `82` status `ready` deltaP `33.995` edge `0.9021` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.989` n `82` status `ready` deltaP `57.767` edge `0.2983` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.641` n `68` status `ready` deltaP `39.8276` edge `0.2879` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.311` n `41` status `ready` deltaP `39.8276` edge `0.2604` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.311` n `41` status `ready` deltaP `39.8276` edge `0.2604` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5133` n `41` status `ready` deltaP `60.8369` edge `0.0581` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5133` n `41` status `ready` deltaP `60.8369` edge `0.0581` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.3925` n `82` status `ready` deltaP `32.1741` edge `0.2803` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8089` n `68` status `ready` deltaP `54.4524` edge `0.0593` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9925` n `52` status `ready` deltaP `26.7472` edge `0.0227` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9925` n `52` status `ready` deltaP `26.7472` edge `0.0227` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7928` n `137` status `ready` deltaP `22.1571` edge `0.0435` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6819` n `137` status `ready` deltaP `11.9138` edge `0.0151` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5912` n `82` status `ready` deltaP `15.2439` edge `0.037` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3387` n `137` status `ready` deltaP `11.9881` edge `0.0111` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.2166` n `137` status `ready` deltaP `6.1104` edge `0.0031` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1665` n `52` status `ready` deltaP `6.299` edge `0.0071` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
