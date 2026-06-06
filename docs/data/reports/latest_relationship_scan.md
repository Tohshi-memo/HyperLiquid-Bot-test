# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T14:52:21.971852+00:00`
- Price records: `672`
- Market context records: `3083`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `17.2805` n `86` status `ready` deltaP `12.7664` edge `2.5415` maxDD `-24.2265`
- `market_context_high->commodity_24h` score `15.2402` n `86` status `ready` deltaP `46.4269` edge `0.9958` maxDD `-1.8236`
- `market_context_high->unknown_24h` score `14.2941` n `86` status `ready` deltaP `21.9517` edge `1.0913` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.3399` n `86` status `ready` deltaP `34.5203` edge `0.9478` maxDD `-9.3021`
- `market_context_high->equity_24h` score `9.8601` n `86` status `ready` deltaP `22.9126` edge `1.4941` maxDD `-26.2853`
- `market_context_high->commodity_4h` score `2.9444` n `121` status `ready` deltaP `18.1302` edge `0.1703` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.0345` n `121` status `ready` deltaP `3.6472` edge `0.0839` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2219` n `124` status `ready` deltaP `0.2656` edge `0.022` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5448` n `124` status `ready` deltaP `3.2596` edge `0.0147` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.683` n `124` status `ready` deltaP `4.4234` edge `0.0959` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.9061` n `124` status `ready` deltaP `1.8109` edge `-0.0145` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.0239` n `86` status `ready` deltaP `0.8277` edge `-0.0047` maxDD `-0.5582`
- `market_context_high->fx_1h` score `-1.1926` n `124` status `ready` deltaP `-8.9869` edge `-0.0022` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2088` n `124` status `ready` deltaP `-1.1059` edge `-0.0003` maxDD `-8.7845`
- `market_context_high->fx_4h` score `-1.3056` n `121` status `ready` deltaP `-11.5665` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.3938` n `121` status `ready` deltaP `9.6163` edge `0.0481` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.9046` n `124` status `ready` deltaP `0.5505` edge `0.0639` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3106` n `124` status `ready` deltaP `-6.7993` edge `-0.0101` maxDD `-7.3029`
- `market_context_high->crypto_alt_4h` score `-3.251` n `121` status `ready` deltaP `16.8288` edge `0.2755` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7933` n `121` status `ready` deltaP `7.8512` edge `-0.0148` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
