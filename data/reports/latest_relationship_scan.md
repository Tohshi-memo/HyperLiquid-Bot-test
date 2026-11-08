# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T15:37:24.041623+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4781`

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

- `market_context_high->unknown_4h` score `30.0898` n `39` status `ready` deltaP `-4.6591` edge `2.5833` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1226` n `37` status `ready` deltaP `15.2403` edge `0.8381` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3691` n `39` status `ready` deltaP `12.5864` edge `0.2428` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.8208` n `39` status `ready` deltaP `30.2924` edge `0.0421` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8881` n `39` status `ready` deltaP `24.789` edge `0.0391` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2052` n `39` status `ready` deltaP `14.5133` edge `0.0852` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1405` n `39` status `ready` deltaP `12.1181` edge `0.0728` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.9343` n `37` status `ready` deltaP `11.3927` edge `0.1069` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7514` n `37` status `ready` deltaP `10.9422` edge `-0.0015` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5207` n `39` status `ready` deltaP `8.414` edge `0.0144` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.4895` n `37` status `ready` deltaP `4.8236` edge `0.1501` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2503` n `39` status `ready` deltaP `3.2282` edge `0.0376` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0808` n `39` status `ready` deltaP `8.2451` edge `0.01` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0277` n `39` status `ready` deltaP `2.0306` edge `0.0157` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1246` n `39` status `ready` deltaP `0.9499` edge `0.0231` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5861` n `39` status `ready` deltaP `23.1669` edge `0.0984` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7999` n `39` status `ready` deltaP `-3.3615` edge `-0.0351` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9096` n `39` status `ready` deltaP `16.1664` edge `0.0199` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.1531` n `37` status `ready` deltaP `3.0124` edge `-0.1442` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.827` n `39` status `ready` deltaP `1.794` edge `-0.1059` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
