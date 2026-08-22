# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T22:52:27.297834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.6202` n `140` status `ready` deltaP `5.616` edge `0.1203` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8831` n `140` status `ready` deltaP `19.0027` edge `-0.0093` maxDD `-0.5036`
- `market_context_high->fx_4h` score `0.1148` n `140` status `ready` deltaP `8.3798` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0601` n `140` status `ready` deltaP `6.1634` edge `0.0043` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1111` n `140` status `ready` deltaP `2.5706` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3406` n `140` status `ready` deltaP `4.5637` edge `0.0329` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3909` n `140` status `ready` deltaP `6.8728` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.5095` n `140` status `ready` deltaP `0.6459` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6054` n `140` status `ready` deltaP `2.2866` edge `0.0107` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9732` n `140` status `ready` deltaP `-5.7665` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.0245` n `124` status `ready` deltaP `0.4424` edge `0.0092` maxDD `-2.1464`
- `market_context_high->commodity_1h` score `-1.1137` n `140` status `ready` deltaP `-8.2934` edge `-0.0025` maxDD `-1.1328`
- `market_context_high->crypto_alt_1h` score `-1.474` n `140` status `ready` deltaP `-1.574` edge `-0.029` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-1.6994` n `140` status `ready` deltaP `5.9844` edge `-0.0347` maxDD `-7.0785`
- `market_context_high->equity_4h` score `-1.7401` n `140` status `ready` deltaP `-1.3153` edge `0.0673` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-1.9223` n `124` status `ready` deltaP `-5.4603` edge `0.0505` maxDD `-4.6099`
- `market_context_high->crypto_major_1h` score `-2.3051` n `140` status `ready` deltaP `-5.3421` edge `-0.1122` maxDD `-7.8171`
- `market_context_high->crypto_major_4h` score `-5.375` n `140` status `ready` deltaP `1.9469` edge `-0.3279` maxDD `-5.6395`
- `market_context_high->metal_24h` score `-5.4004` n `124` status `ready` deltaP `-23.7399` edge `-0.2033` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-6.8958` n `124` status `ready` deltaP `7.0621` edge `-0.5711` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
