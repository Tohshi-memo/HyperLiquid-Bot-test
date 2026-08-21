# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T18:52:27.292085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `1.1412` n `133` status `ready` deltaP `8.5375` edge `0.0609` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1904` n `132` status `ready` deltaP `9.7145` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1818` n `133` status `ready` deltaP `10.7559` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1401` n `133` status `ready` deltaP `2.0294` edge `0.0044` maxDD `-0.2043`
- `market_context_high->unknown_4h` score `-0.1795` n `132` status `ready` deltaP `21.129` edge `-0.1119` maxDD `-0.5133`
- `market_context_high->equity_1h` score `-0.2311` n `133` status `ready` deltaP `6.4146` edge `0.0346` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.369` n `133` status `ready` deltaP `0.0833` edge `-0.006` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5049` n `132` status `ready` deltaP `2.9795` edge `-0.023` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.6316` n `132` status `ready` deltaP `1.9632` edge `0.0095` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6461` n `132` status `ready` deltaP `-0.8407` edge `0.0078` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6877` n `133` status `ready` deltaP `-4.7206` edge `-0.0001` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.692` n `133` status `ready` deltaP `0.4199` edge `0.0197` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-0.8547` n `105` status `ready` deltaP `1.2897` edge `0.1035` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.203` n `133` status `ready` deltaP `-1.2505` edge `-0.0434` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3551` n `132` status `ready` deltaP `3.2197` edge `-0.0074` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8671` n `132` status `ready` deltaP `-2.319` edge `0.0566` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.6586` n `105` status `ready` deltaP `-8.8294` edge `-0.0017` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9631` n `132` status `ready` deltaP `-0.5497` edge `-0.2245` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2574` n `105` status `ready` deltaP `-6.4633` edge `-0.0525` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7544` n `105` status `ready` deltaP `-18.4574` edge `-0.1557` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
