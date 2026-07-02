# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T07:37:30.636682+00:00`
- Price records: `672`
- Market context records: `5433`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->equity_24h` score `4.6563` n `185` status `ready` deltaP `11.8694` edge `0.6625` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `4.414` n `185` status `ready` deltaP `19.6744` edge `0.6907` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8222` n `196` status `ready` deltaP `16.7652` edge `0.436` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0288` n `196` status `ready` deltaP `12.1329` edge `0.3356` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.8318` n `196` status `ready` deltaP `12.9666` edge `0.3134` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.6196` n `196` status `ready` deltaP `8.979` edge `0.0883` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2072` n `196` status `ready` deltaP `7.3812` edge `0.0174` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1047` n `185` status `ready` deltaP `9.6086` edge `0.0342` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1018` n `196` status `ready` deltaP `2.4563` edge `0.0713` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.1849` n `196` status `ready` deltaP `3.4706` edge `0.086` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3303` n `196` status `ready` deltaP `3.2995` edge `0.018` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5658` n `196` status `ready` deltaP `0.2444` edge `0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8379` n `196` status `ready` deltaP `7.2299` edge `0.0429` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0578` n `185` status `ready` deltaP `16.1627` edge `0.1027` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1782` n `196` status `ready` deltaP `0.2894` edge `0.0024` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4793` n `196` status `ready` deltaP `-3.3331` edge `-0.0066` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7167` n `196` status `ready` deltaP `-8.885` edge `-0.0366` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3923` n `196` status `ready` deltaP `-7.8895` edge `-0.0496` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.2204` n `185` status `ready` deltaP `10.3867` edge `0.2821` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3863` n `185` status `ready` deltaP `-5.7742` edge `-0.1707` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
