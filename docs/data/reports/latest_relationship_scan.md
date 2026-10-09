# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T19:07:33.395918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7791`

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

- `market_context_high->unknown_4h` score `41.0839` n `91` status `ready` deltaP `-4.3889` edge `3.5068` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.8349` n `91` status `ready` deltaP `33.2641` edge `0.6407` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.5488` n `91` status `ready` deltaP `18.9632` edge `1.2844` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.8528` n `91` status `ready` deltaP `10.751` edge `0.7771` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5566` n `91` status `ready` deltaP `18.0892` edge `0.212` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.2914` n `91` status `ready` deltaP `10.3731` edge `0.0571` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2683` n `91` status `ready` deltaP `6.7774` edge `0.0014` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2143` n `91` status `ready` deltaP `12.5613` edge `0.0088` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0554` n `91` status `ready` deltaP `10.5301` edge `0.0854` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3364` n `91` status `ready` deltaP `7.8638` edge `0.0954` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3491` n `91` status `ready` deltaP `3.2261` edge `0.0006` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3743` n `91` status `ready` deltaP `0.7819` edge `0.0012` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.7941` n `91` status `ready` deltaP `-7.0183` edge `0.1383` maxDD `-8.7986`
- `market_context_high->commodity_4h` score `-0.8109` n `91` status `ready` deltaP `-2.3182` edge `-0.0185` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.8601` n `91` status `ready` deltaP `-1.2664` edge `0.0506` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8709` n `91` status `ready` deltaP `-3.456` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9704` n `91` status `ready` deltaP `-5.3925` edge `0.0123` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.199` n `91` status `ready` deltaP `-9.6618` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2335` n `91` status `ready` deltaP `-9.8734` edge `0.0009` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2827` n `91` status `ready` deltaP `-4.1112` edge `0.0099` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
