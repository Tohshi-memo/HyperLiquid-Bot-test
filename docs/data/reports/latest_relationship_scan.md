# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T04:52:25.986967+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.8533` n `91` status `ready` deltaP `-6.3404` edge `3.5006` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3777` n `91` status `ready` deltaP `33.2641` edge `0.6026` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7297` n `91` status `ready` deltaP `18.6166` edge `1.3099` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6249` n `91` status `ready` deltaP `10.0578` edge `0.7525` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4732` n `91` status `ready` deltaP `17.4015` edge `0.2059` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2248` n `91` status `ready` deltaP `6.248` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1953` n `91` status `ready` deltaP `9.6944` edge `0.0493` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.0437` n `91` status `ready` deltaP `10.5033` edge `0.0083` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.3098` n `91` status `ready` deltaP `3.5978` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3351` n `91` status `ready` deltaP `1.0019` edge `0.003` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3699` n `91` status `ready` deltaP `6.3706` edge `0.0586` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3754` n `91` status `ready` deltaP `7.8638` edge `0.0904` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.6736` n `91` status `ready` deltaP `-0.8794` edge `-0.0105` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.915` n `91` status `ready` deltaP `-4.2886` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->unknown_1h` score `-0.9582` n `91` status `ready` deltaP `-3.7688` edge `-0.0132` maxDD `-0.9885`
- `market_context_high->metal_4h` score `-1.0053` n `91` status `ready` deltaP `-6.2283` edge `0.0134` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0439` n `91` status `ready` deltaP `-7.5617` edge `0.1099` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1652` n `91` status `ready` deltaP `-2.0941` edge `0.0307` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2177` n `91` status `ready` deltaP `-10.0382` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2391` n `91` status `ready` deltaP `-9.9505` edge `0.0007` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
