# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T18:07:24.491635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.1385` n `60` status `ready` deltaP `33.8879` edge `432.3277` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.0533` n `53` status `ready` deltaP `55.1911` edge `1.0929` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.5574` n `60` status `ready` deltaP `24.2174` edge `0.4447` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.6922` n `60` status `ready` deltaP `23.7601` edge `0.085` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.0217` n `53` status `ready` deltaP `29.7374` edge `0.2468` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3581` n `60` status `ready` deltaP `8.2012` edge `0.197` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.5891` n `60` status `ready` deltaP `12.2866` edge `0.1328` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5746` n `53` status `ready` deltaP `8.8904` edge `0.1101` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.5606` n `68` status `ready` deltaP `8.1455` edge `0.0747` maxDD `-2.916`
- `news_risk_high->fx_4h` score `0.2657` n `60` status `ready` deltaP `13.9939` edge `0.0246` maxDD `-0.6604`
- `market_context_high->fx_4h` score `0.2137` n `53` status `ready` deltaP `13.7109` edge `0.0156` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.178` n `60` status `ready` deltaP `5.2845` edge `0.0352` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1357` n `68` status `ready` deltaP `7.08` edge `0.0384` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0161` n `53` status `ready` deltaP `7.2026` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0925` n `68` status `ready` deltaP `1.8669` edge `0.008` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.112` n `68` status `ready` deltaP `2.0694` edge `0.0041` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.1134` n `53` status `ready` deltaP `3.5787` edge `0.0157` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1333` n `68` status `ready` deltaP `2.4657` edge `0.0068` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1805` n `68` status `ready` deltaP `2.5185` edge `0.0321` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.211` n `53` status `ready` deltaP `4.8069` edge `0.0389` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
