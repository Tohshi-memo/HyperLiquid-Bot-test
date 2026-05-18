# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T22:37:18.636792+00:00`
- Price records: `672`
- Market context records: `1161`
- Flow alert records: `5245`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.6896` n `142` status `ready` deltaP `45.2734` edge `1.5355` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1142` n `142` status `ready` deltaP `21.672` edge `0.9` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.746` n `142` status `ready` deltaP `21.1512` edge `0.5975` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.9216` n `142` status `ready` deltaP `19.7623` edge `0.4175` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.5449` n `142` status `ready` deltaP `-3.0908` edge `0.6494` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4187` n `158` status `ready` deltaP `11.9076` edge `0.1885` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1202` n `158` status `ready` deltaP `8.8723` edge `0.1025` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.416` n `158` status `ready` deltaP `6.8483` edge `0.0207` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2964` n `158` status `ready` deltaP `2.9352` edge `0.0429` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1885` n `158` status `ready` deltaP `9.0132` edge `0.1562` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1242` n `158` status `ready` deltaP `8.2828` edge `0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0244` n `158` status `ready` deltaP `7.2141` edge `0.0316` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.1387` n `142` status `ready` deltaP `3.2717` edge `0.2396` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.2895` n `158` status `ready` deltaP `3.1722` edge `0.039` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.3406` n `158` status `ready` deltaP `6.3235` edge `-0.0095` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.8888` n `158` status `ready` deltaP `-4.0154` edge `-0.0064` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.948` n `158` status `ready` deltaP `-2.8038` edge `-0.0032` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1386` n `158` status `ready` deltaP `4.9533` edge `0.1175` maxDD `-16.7194`
- `market_context_high->unknown_4h` score `-1.3734` n `158` status `ready` deltaP `6.7498` edge `-0.0378` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-1.7979` n `158` status `ready` deltaP `5.6557` edge `-0.0728` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
