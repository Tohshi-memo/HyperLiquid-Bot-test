# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T12:07:33.937201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1276.9719` n `148` status `ready` deltaP `-2.135` edge `106.5213` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `34.0636` n `148` status `ready` deltaP `4.8492` edge `2.8196` maxDD `-0.3966`
- `market_context_high->index_24h` score `0.6532` n `148` status `ready` deltaP `18.4873` edge `-0.0064` maxDD `-1.993`
- `market_context_high->fx_1h` score `0.0906` n `148` status `ready` deltaP `6.3845` edge `0.0008` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.0529` n `148` status `ready` deltaP `10.8108` edge `0.0454` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1457` n `148` status `ready` deltaP `7.574` edge `0.0055` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1668` n `148` status `ready` deltaP `6.4725` edge `0.0028` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.4956` n `148` status `ready` deltaP `1.1248` edge `0.0096` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.7511` n `148` status `ready` deltaP `8.1905` edge `-0.0016` maxDD `-4.611`
- `market_context_high->index_1h` score `-0.8093` n `148` status `ready` deltaP `-4.6448` edge `-0.0045` maxDD `-1.4631`
- `market_context_high->crypto_major_1h` score `-0.8095` n `148` status `ready` deltaP `4.9563` edge `0.0278` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-1.4047` n `148` status `ready` deltaP `4.0541` edge `0.0085` maxDD `-1.2066`
- `market_context_high->equity_1h` score `-1.5109` n `148` status `ready` deltaP `-0.3763` edge `-0.0022` maxDD `-9.1198`
- `market_context_high->crypto_alt_1h` score `-1.6846` n `148` status `ready` deltaP `1.2623` edge `0.0088` maxDD `-11.9884`
- `market_context_high->index_4h` score `-3.1329` n `148` status `ready` deltaP `-10.6955` edge `-0.0332` maxDD `-5.5256`
- `market_context_high->crypto_major_4h` score `-3.4839` n `148` status `ready` deltaP `2.0517` edge `-0.0303` maxDD `-27.0697`
- `market_context_high->crypto_major_24h` score `-3.6489` n `148` status `ready` deltaP `-2.0833` edge `0.0318` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.8723` n `148` status `ready` deltaP `-0.2393` edge `-0.0189` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.3373` n `148` status `ready` deltaP `-4.9893` edge `-0.1523` maxDD `-33.2303`
- `market_context_high->equity_24h` score `-5.5497` n `148` status `ready` deltaP `2.271` edge `-0.2005` maxDD `-14.1693`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
