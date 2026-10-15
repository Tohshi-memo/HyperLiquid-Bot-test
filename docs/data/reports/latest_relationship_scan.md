# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T14:52:31.717461+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9160`

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

- `risk_on_high->commodity_24h` score `7.8859` n `54` status `ready` deltaP `41.2892` edge `0.3819` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8859` n `54` status `ready` deltaP `41.2892` edge `0.3819` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.7324` n `122` status `ready` deltaP `17.9578` edge `0.6161` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.9439` n `122` status `ready` deltaP `19.5572` edge `0.4971` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.5388` n `54` status `ready` deltaP `20.7204` edge `0.3681` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.5388` n `54` status `ready` deltaP `20.7204` edge `0.3681` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.0737` n `54` status `ready` deltaP `33.0059` edge `0.3875` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0737` n `54` status `ready` deltaP `33.0059` edge `0.3875` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.744` n `122` status `ready` deltaP `13.5565` edge `0.1614` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0616` n `122` status `ready` deltaP `5.5095` edge `0.1323` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.0135` n `122` status `ready` deltaP `9.8561` edge `0.0377` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2981` n `115` status `ready` deltaP `13.4631` edge `0.1502` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3454` n `122` status `ready` deltaP `-0.613` edge `-0.0018` maxDD `-0.4047`
- `risk_on_high->crypto_major_1h` score `-0.403` n `54` status `ready` deltaP `0.804` edge `0.0152` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.403` n `54` status `ready` deltaP `0.804` edge `0.0152` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.4416` n `54` status `ready` deltaP `4.358` edge `0.0166` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.4416` n `54` status `ready` deltaP `4.358` edge `0.0166` maxDD `-5.8485`
- `market_context_high->index_1h` score `-0.4944` n `122` status `ready` deltaP `1.664` edge `0.0003` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5147` n `54` status `ready` deltaP `0.9537` edge `0.0008` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5147` n `54` status `ready` deltaP `0.9537` edge `0.0008` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
