# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T11:07:29.878941+00:00`
- Price records: `672`
- Market context records: `8509`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6275.8929` n `52` status `ready` deltaP `44.7383` edge `522.7349` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8646` n `64` status `ready` deltaP `21.7226` edge `0.4036` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0121` n `64` status `ready` deltaP `16.654` edge `0.0757` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7158` n `64` status `ready` deltaP `15.8028` edge `0.0853` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9127` n `64` status `ready` deltaP `5.8308` edge `0.1557` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8421` n `64` status `ready` deltaP `14.4817` edge `0.1506` maxDD `-5.8012`
- `market_context_high->equity_1h` score `0.5956` n `37` status `ready` deltaP `4.5275` edge `0.0486` maxDD `-0.9985`
- `news_risk_high->crypto_alt_1h` score `0.5708` n `64` status `ready` deltaP `9.3095` edge `0.0638` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3532` n `64` status `ready` deltaP `6.7646` edge `0.0514` maxDD `-2.0972`
- `market_context_high->index_1h` score `0.2874` n `37` status `ready` deltaP `8.4197` edge `0.0004` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1173` n `64` status `ready` deltaP `5.8851` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0301` n `64` status `ready` deltaP `4.07` edge `0.0084` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0254` n `64` status `ready` deltaP `11.471` edge `0.0214` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0682` n `64` status `ready` deltaP `1.1052` edge `0.0315` maxDD `-0.8085`
- `market_context_high->crypto_major_1h` score `-0.1262` n `37` status `ready` deltaP `5.7089` edge `-0.0045` maxDD `-1.9791`
- `news_risk_high->metal_1h` score `-0.1287` n `64` status `ready` deltaP `3.256` edge `0.0079` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.1451` n `37` status `ready` deltaP `3.7628` edge `-0.0069` maxDD `-0.6101`
- `market_context_high->commodity_1h` score `-0.2086` n `37` status `ready` deltaP `6.0002` edge `-0.0042` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5414` n `37` status `ready` deltaP `-5.2598` edge `0.0158` maxDD `-2.012`
- `market_context_high->fx_1h` score `-0.7808` n `37` status `ready` deltaP `-8.2619` edge `0.0015` maxDD `-0.3888`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
