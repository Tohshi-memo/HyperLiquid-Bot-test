# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T06:07:32.165697+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13755`

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

- `market_context_high->index_1h` score `0.3215` n `105` status `ready` deltaP `10.4078` edge `0.0061` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3125` n `105` status `ready` deltaP `8.4203` edge `0.0514` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.0747` n `105` status `ready` deltaP `7.7903` edge `0.0079` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0483` n `105` status `ready` deltaP `4.4353` edge `0.1374` maxDD `-8.3685`
- `market_context_high->commodity_24h` score `-0.1706` n `96` status `ready` deltaP `4.6875` edge `0.1302` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2453` n `105` status `ready` deltaP `6.5302` edge `-0.0174` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2868` n `105` status `ready` deltaP `2.4893` edge `-0.0018` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.3051` n `105` status `ready` deltaP `5.4283` edge `0.0171` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.429` n `105` status `ready` deltaP `7.4808` edge `-0.0629` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6481` n `105` status `ready` deltaP `-1.4329` edge `0.0115` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7463` n `105` status `ready` deltaP `-5.7285` edge `-0.0009` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7667` n `105` status `ready` deltaP `-1.2945` edge `-0.0095` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9134` n `105` status `ready` deltaP `-0.5589` edge `-0.0289` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.5045` n `105` status `ready` deltaP `0.9277` edge `-0.0879` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.8982` n `105` status `ready` deltaP `3.1765` edge `-0.1606` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.5355` n `96` status `ready` deltaP `-17.8819` edge `-0.0171` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.5843` n `96` status `ready` deltaP `1.0416` edge `-0.0497` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.9635` n `96` status `ready` deltaP `-21.0069` edge `-0.1655` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.5426` n `96` status `ready` deltaP `11.6319` edge `-0.4888` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
