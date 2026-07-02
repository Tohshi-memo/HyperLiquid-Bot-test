# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T10:52:30.994748+00:00`
- Price records: `672`
- Market context records: `5447`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->equity_24h` score `4.1115` n `185` status `ready` deltaP `11.8694` edge `0.6171` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.2067` n `196` status `ready` deltaP `15.8506` edge `0.3908` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.0803` n `185` status `ready` deltaP `17.4174` edge `0.5946` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.6974` n `196` status `ready` deltaP `12.9666` edge `0.3022` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.4501` n `196` status `ready` deltaP `10.9134` edge `0.2955` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5435` n `199` status `ready` deltaP `8.4622` edge `0.0854` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3188` n `185` status `ready` deltaP `11.8656` edge `0.037` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1702` n `199` status `ready` deltaP `6.9336` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2926` n `199` status `ready` deltaP `1.2563` edge `0.0634` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.3168` n `199` status `ready` deltaP `3.5123` edge `0.0177` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.3991` n `199` status `ready` deltaP `2.2936` edge `0.076` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5788` n `199` status `ready` deltaP `0.1121` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7783` n `196` status `ready` deltaP `7.8397` edge `0.0438` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1296` n `196` status `ready` deltaP `0.7467` edge `0.0034` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.137` n `185` status `ready` deltaP `16.1627` edge `0.0961` maxDD `-12.5551`
- `market_context_high->commodity_1h` score `-1.4307` n `199` status `ready` deltaP `-2.7209` edge `-0.0063` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6593` n `196` status `ready` deltaP `-8.4277` edge `-0.0323` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2721` n `196` status `ready` deltaP `-6.8224` edge `-0.0467` maxDD `-14.1062`
- `market_context_high->metal_24h` score `-7.4955` n `185` status `ready` deltaP `-5.7742` edge `-0.1847` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.5782` n `185` status `ready` deltaP `8.1297` edge `0.184` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
