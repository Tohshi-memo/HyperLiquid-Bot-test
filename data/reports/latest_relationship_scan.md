# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T20:22:27.951055+00:00`
- Price records: `672`
- Market context records: `5592`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.7651` n `174` status `ready` deltaP `15.0084` edge `0.7216` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2143` n `206` status `ready` deltaP `11.9154` edge `0.251` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.0664` n `174` status `ready` deltaP `19.7019` edge `0.0549` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.5951` n `206` status `ready` deltaP `6.6082` edge `0.1694` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.542` n `206` status `ready` deltaP `6.953` edge `0.1629` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `-0.1201` n `174` status `ready` deltaP `12.063` edge `0.3636` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.2277` n `218` status `ready` deltaP `5.4895` edge `0.0349` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.2843` n `218` status `ready` deltaP `1.405` edge `0.001` maxDD `-0.4122`
- `market_context_high->index_1h` score `-0.3595` n `218` status `ready` deltaP `1.9022` edge `0.0067` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6049` n `218` status `ready` deltaP `-1.5355` edge `0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6279` n `218` status `ready` deltaP `0.8447` edge `0.0382` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6327` n `218` status `ready` deltaP `3.829` edge `0.0463` maxDD `-6.9639`
- `market_context_high->fx_4h` score `-0.9385` n `206` status `ready` deltaP `3.6792` edge `0.0087` maxDD `-0.915`
- `market_context_high->commodity_1h` score `-1.1757` n `218` status `ready` deltaP `-2.1343` edge `-0.0072` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.4837` n `206` status `ready` deltaP `3.4025` edge `0.0146` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2541` n `174` status `ready` deltaP `11.1291` edge `0.0355` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9471` n `206` status `ready` deltaP `-12.1922` edge `-0.0582` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1468` n `206` status `ready` deltaP `-5.0113` edge `-0.0446` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0185` n `174` status `ready` deltaP `-8.3273` edge `-0.2364` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.2166` n `174` status `ready` deltaP `1.8499` edge `0.006` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
