# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T22:22:27.359789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `55.5973` n `50` status `ready` deltaP `16.2912` edge `4.5245` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.3799` n `50` status `ready` deltaP `46.6066` edge `2.5984` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `8.8083` n `71` status `ready` deltaP `17.5863` edge `0.6478` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `8.4356` n `50` status `ready` deltaP `26.1144` edge `0.5782` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.4243` n `50` status `ready` deltaP `30.1005` edge `0.4275` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `4.906` n `120` status `ready` deltaP `9.6245` edge `0.4179` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4214` n `50` status `ready` deltaP `43.4073` edge `0.0833` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.4897` n `71` status `ready` deltaP `9.1064` edge `0.2658` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2386` n `120` status `ready` deltaP `28.7406` edge `0.1802` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4142` n `50` status `ready` deltaP `26.9948` edge `0.0363` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2509` n `120` status `ready` deltaP `17.246` edge `0.1133` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1176` n `71` status `ready` deltaP `31.3917` edge `0.0221` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.9023` n `120` status `ready` deltaP `8.9421` edge `0.0606` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.595` n `71` status `ready` deltaP `12.3598` edge `0.0059` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.358` n `71` status `ready` deltaP `11.1622` edge `0.0035` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0958` n `120` status `ready` deltaP `13.4553` edge `0.0143` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3958` n `120` status `ready` deltaP `3.4631` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.46` n `71` status `ready` deltaP `-0.8813` edge `-0.0097` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.6845` n `71` status `ready` deltaP `-0.5545` edge `-0.0265` maxDD `-2.605`
- `news_risk_high->equity_1h` score `-0.7334` n `71` status `ready` deltaP `6.61` edge `-0.0447` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
