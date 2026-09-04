# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T07:07:31.021139+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11466`

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

- `risk_on_high->unknown_4h` score `21.0113` n `133` status `ready` deltaP `8.846` edge `1.7538` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.0113` n `133` status `ready` deltaP `8.846` edge `1.7538` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `14.4021` n `175` status `ready` deltaP `11.4024` edge `1.1937` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.6175` n `133` status `ready` deltaP `-0.6045` edge `1.1132` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.6175` n `133` status `ready` deltaP `-0.6045` edge `1.1132` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.4804` n `185` status `ready` deltaP `0.4685` edge `0.9333` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.4919` n `156` status `ready` deltaP `16.8135` edge `0.4468` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.3601` n `133` status `ready` deltaP `13.3289` edge `0.439` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.3601` n `133` status `ready` deltaP `13.3289` edge `0.439` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2718` n `67` status `ready` deltaP `5.1852` edge `0.0362` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.1311` n `133` status `ready` deltaP `12.5625` edge `0.0043` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1311` n `133` status `ready` deltaP `12.5625` edge `0.0043` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.1154` n `67` status `ready` deltaP `3.5772` edge `-0.0033` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1536` n `133` status `ready` deltaP `3.9924` edge `-0.0018` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1536` n `133` status `ready` deltaP `3.9924` edge `-0.0018` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1885` n `67` status `ready` deltaP `4.3078` edge `0.0002` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.2138` n `133` status `ready` deltaP `4.9007` edge `0.0512` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2138` n `133` status `ready` deltaP `4.9007` edge `0.0512` maxDD `-5.4685`
- `news_risk_high->commodity_24h` score `-0.2148` n `67` status `ready` deltaP `4.1045` edge `-0.026` maxDD `-0.2074`
- `news_risk_high->fx_4h` score `-0.334` n `67` status `ready` deltaP `5.5356` edge `0.0009` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
