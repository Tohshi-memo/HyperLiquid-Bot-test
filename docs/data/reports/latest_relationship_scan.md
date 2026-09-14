# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T05:07:28.402885+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11598`

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

- `news_risk_high->unknown_1h` score `443.728` n `82` status `ready` deltaP `-5.8493` edge `37.0585` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.7472` n `82` status `ready` deltaP `39.1337` edge `1.4335` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.1078` n `82` status `ready` deltaP `37.1615` edge `1.4083` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.5856` n `82` status `ready` deltaP `34.5122` edge `0.9134` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.0652` n `82` status `ready` deltaP `58.2842` edge `0.3012` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.7166` n `71` status `ready` deltaP `39.8276` edge `0.2942` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.281` n `41` status `ready` deltaP `39.8276` edge `0.2579` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.281` n `41` status `ready` deltaP `39.8276` edge `0.2579` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.4663` n `82` status `ready` deltaP `32.6914` edge `0.283` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.4504` n `41` status `ready` deltaP `60.3196` edge `0.0563` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.4504` n `41` status `ready` deltaP `60.3196` edge `0.0563` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7745` n `71` status `ready` deltaP `54.3079` edge `0.0574` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0071` n `52` status `ready` deltaP `26.8996` edge `0.0229` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0071` n `52` status `ready` deltaP `26.8996` edge `0.0229` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8074` n `137` status `ready` deltaP `22.3095` edge `0.0437` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7251` n `137` status `ready` deltaP `12.3629` edge `0.0157` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5927` n `82` status `ready` deltaP `15.2439` edge `0.0372` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3379` n `137` status `ready` deltaP `11.9881` edge `0.011` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.231` n `137` status `ready` deltaP `6.2601` edge `0.0033` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.2096` n `52` status `ready` deltaP `6.7481` edge `0.0077` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
