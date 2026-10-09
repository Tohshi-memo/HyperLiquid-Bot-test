# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T12:07:27.150455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8505`

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

- `market_context_high->unknown_4h` score `40.2979` n `91` status `ready` deltaP `-5.2734` edge `3.4472` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0833` n `91` status `ready` deltaP `33.3391` edge `0.6609` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.63` n `91` status `ready` deltaP `21.6652` edge `1.405` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1937` n `91` status `ready` deltaP `13.452` edge `0.931` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9907` n `91` status `ready` deltaP `18.7735` edge `0.2631` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.5788` n `91` status `ready` deltaP `14.4307` edge `0.1265` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3107` n `91` status `ready` deltaP `9.9938` edge `0.0621` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2954` n `91` status `ready` deltaP `7.1462` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0977` n `91` status `ready` deltaP `11.4179` edge `0.0067` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.2623` n `91` status `ready` deltaP `-5.7324` edge `0.1979` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2654` n `91` status `ready` deltaP `3.8972` edge `0.0031` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.295` n `91` status `ready` deltaP `8.3009` edge `0.0978` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.443` n `91` status `ready` deltaP `0.2534` edge `-0.001` maxDD `-0.3417`
- `market_context_high->metal_4h` score `-0.8019` n `91` status `ready` deltaP `-3.6368` edge `0.0222` maxDD `-1.0609`
- `market_context_high->crypto_alt_1h` score `-0.8388` n `91` status `ready` deltaP `-1.4953` edge `0.0539` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8582` n `91` status `ready` deltaP `-2.9413` edge `-0.0064` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8819` n `91` status `ready` deltaP `-2.7087` edge `-0.025` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2248` n `91` status `ready` deltaP `-10.0382` edge `-0.0039` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3133` n `91` status `ready` deltaP `-11.0175` edge `-0.0017` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3704` n `91` status `ready` deltaP `-4.6586` edge `0.0023` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
