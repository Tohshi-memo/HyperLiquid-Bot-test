# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T17:52:32.106622+00:00`
- Price records: `672`
- Market context records: `1653`
- Flow alert records: `6668`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.5589` n `169` status `ready` deltaP `28.2417` edge `0.8509` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.1719` n `188` status `ready` deltaP `21.8814` edge `0.4682` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.737` n `169` status `ready` deltaP `20.2381` edge `0.3143` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.4064` n `188` status `ready` deltaP `17.8536` edge `0.3524` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.7798` n `188` status `ready` deltaP `12.0697` edge `0.1773` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.6407` n `169` status `ready` deltaP `19.2553` edge `0.4982` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.5814` n `169` status `ready` deltaP `25.0547` edge `0.74` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.409` n `169` status `ready` deltaP `25.709` edge `1.0436` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.3883` n `198` status `ready` deltaP `5.7038` edge `0.0967` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.3105` n `198` status `ready` deltaP `1.1009` edge `0.0337` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.4167` n `188` status `ready` deltaP `0.6719` edge `0.051` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.4942` n `169` status `ready` deltaP `6.214` edge `0.0223` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5049` n `198` status `ready` deltaP `-1.1628` edge `0.0062` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.514` n `198` status `ready` deltaP `1.739` edge `0.0499` maxDD `-5.5244`
- `market_context_high->fx_1h` score `-0.5225` n `198` status `ready` deltaP `-0.1134` edge `-0.003` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.8283` n `198` status `ready` deltaP `3.4038` edge `0.0047` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8396` n `198` status `ready` deltaP `1.683` edge `-0.0057` maxDD `-6.7191`
- `market_context_high->metal_4h` score `-1.3927` n `188` status `ready` deltaP `8.0597` edge `0.0994` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0177` n `188` status `ready` deltaP `-9.2773` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.4679` n `188` status `ready` deltaP `10.9387` edge `-0.1348` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
