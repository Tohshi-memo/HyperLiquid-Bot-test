# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T07:52:19.292526+00:00`
- Price records: `672`
- Market context records: `1610`
- Flow alert records: `6544`
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

- `market_context_high->metal_24h` score `12.9883` n `185` status `ready` deltaP `28.9856` edge `1.01` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.7911` n `185` status `ready` deltaP `25.3238` edge `0.9778` maxDD `-30.7893`
- `market_context_high->crypto_major_24h` score `7.2436` n `185` status `ready` deltaP `25.1464` edge `0.7542` maxDD `-22.457`
- `market_context_high->equity_24h` score `4.5683` n `185` status `ready` deltaP `19.6462` edge `0.4824` maxDD `-14.2815`
- `market_context_high->index_24h` score `3.9615` n `185` status `ready` deltaP `21.1139` edge `0.298` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2685` n `195` status `ready` deltaP `10.7638` edge `0.1434` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2042` n `195` status `ready` deltaP `12.9799` edge `0.2716` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0958` n `195` status `ready` deltaP `9.0854` edge `0.2226` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2001` n `185` status `ready` deltaP `7.8801` edge `0.0357` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3397` n `195` status `ready` deltaP `0.5113` edge `0.0554` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5246` n `195` status `ready` deltaP `1.0403` edge `0.0302` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6945` n `195` status `ready` deltaP `0.2695` edge `0.0035` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8778` n `195` status `ready` deltaP `-0.9634` edge `-0.0035` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8992` n `195` status `ready` deltaP `-1.0049` edge `0.0271` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9229` n `195` status `ready` deltaP `-0.061` edge `0.0324` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.1354` n `195` status `ready` deltaP `-0.4921` edge `0.0008` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1706` n `195` status `ready` deltaP `4.6553` edge `0.005` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.4109` n `195` status `ready` deltaP `-11.0248` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4249` n `195` status `ready` deltaP `8.7664` edge `0.092` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.2067` n `195` status `ready` deltaP `-14.2832` edge `-0.1096` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
