# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T17:52:26.231576+00:00`
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

- `market_context_high->unknown_4h` score `40.7561` n `91` status `ready` deltaP `-4.5112` edge `3.4803` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.015` n `91` status `ready` deltaP `33.6863` edge `0.6529` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7553` n `91` status `ready` deltaP `19.7555` edge `1.3056` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.1888` n `91` status `ready` deltaP `11.5423` edge `0.8149` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.6353` n `91` status `ready` deltaP `18.1637` edge `0.2216` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.3083` n `91` status `ready` deltaP `10.5926` edge `0.0578` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2978` n `91` status `ready` deltaP `7.1462` edge `0.0014` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2216` n `91` status `ready` deltaP `12.6374` edge `0.0089` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0986` n `91` status `ready` deltaP `10.6113` edge `0.0904` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.317` n `91` status `ready` deltaP `3.5978` edge `0.0008` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3177` n `91` status `ready` deltaP `7.9537` edge `0.0972` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.443` n `91` status `ready` deltaP `0.2534` edge `-0.001` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.5639` n `91` status `ready` deltaP `-6.3422` edge `0.1633` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-0.8101` n `91` status `ready` deltaP `-1.0462` edge `0.0533` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.841` n `91` status `ready` deltaP `-3.091` edge `-0.0032` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8852` n `91` status `ready` deltaP `-3.0136` edge `-0.0234` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9789` n `91` status `ready` deltaP `-5.4661` edge `0.0117` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1695` n `91` status `ready` deltaP `-9.14` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2193` n `91` status `ready` deltaP `-9.6456` edge `0.0012` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2354` n `91` status `ready` deltaP `-3.5915` edge `0.0125` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
