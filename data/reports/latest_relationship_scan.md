# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T00:37:21.019396+00:00`
- Price records: `672`
- Market context records: `1579`
- Flow alert records: `6458`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.4075` n `182` status `ready` deltaP `27.6366` edge `1.0331` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6742` n `182` status `ready` deltaP `26.9974` edge `0.9945` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.1001` n `182` status `ready` deltaP `26.7399` edge `0.7766` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.111` n `182` status `ready` deltaP `18.2349` edge `0.4537` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.0586` n `182` status `ready` deltaP `21.1271` edge `0.306` maxDD `-5.3574`
- `market_context_high->equity_4h` score `0.8966` n `199` status `ready` deltaP `8.1398` edge `0.1299` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2333` n `199` status `ready` deltaP `13.2545` edge `0.2735` maxDD `-19.5565`
- `market_context_high->fx_24h` score `0.1695` n `182` status `ready` deltaP `11.4945` edge `0.0424` maxDD `-1.3925`
- `market_context_high->crypto_major_4h` score `0.0505` n `199` status `ready` deltaP `9.2796` edge `0.2155` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.2607` n `199` status `ready` deltaP `1.2668` edge `0.0605` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5659` n `199` status `ready` deltaP `0.7636` edge `0.0286` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5967` n `199` status `ready` deltaP `1.5226` edge `0.0033` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6971` n `199` status `ready` deltaP `5.7466` edge `0.0059` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.771` n `199` status `ready` deltaP `-0.7966` edge `-0.0014` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8225` n `199` status `ready` deltaP `0.0053` edge `0.0302` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1734` n `199` status `ready` deltaP `-2.4582` edge `0.0275` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3018` n `199` status `ready` deltaP `10.516` edge `0.0906` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3783` n `199` status `ready` deltaP `-10.3973` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2112` n `199` status `ready` deltaP `-14.7001` edge `-0.1074` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
