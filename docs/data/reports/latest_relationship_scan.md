# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T00:37:35.772580+00:00`
- Price records: `672`
- Market context records: `5198`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `18.2876` n `93` status `ready` deltaP `33.5461` edge `1.3193` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.6773` n `93` status `ready` deltaP `29.0659` edge `1.3955` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `11.0047` n `93` status `ready` deltaP `29.5139` edge `1.059` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.3889` n `155` status `ready` deltaP `19.5741` edge `0.4208` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5935` n `155` status `ready` deltaP `13.8464` edge `0.4504` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4454` n `155` status `ready` deltaP `14.0696` edge `0.5059` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.588` n `155` status `ready` deltaP `8.9878` edge `0.2199` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.8452` n `155` status `ready` deltaP `8.1599` edge `0.1799` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6068` n `155` status `ready` deltaP `4.803` edge `0.1147` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5908` n `155` status `ready` deltaP `6.8524` edge `0.1281` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.4256` n `93` status `ready` deltaP `12.7352` edge `0.0401` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1554` n `155` status `ready` deltaP `6.8669` edge `0.0637` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0469` n `155` status `ready` deltaP `5.0348` edge `0.0129` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0818` n `155` status `ready` deltaP `4.7102` edge `0.0173` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2666` n `155` status `ready` deltaP `1.6593` edge `0.0` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.5464` n `155` status `ready` deltaP `4.1011` edge `0.006` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.5474` n `155` status `ready` deltaP `5.4485` edge `0.0298` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5969` n `155` status `ready` deltaP `0.7253` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.8371` n `93` status `ready` deltaP `10.1815` edge `-0.0117` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3527` n `155` status `ready` deltaP `-0.1023` edge `0.0276` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
