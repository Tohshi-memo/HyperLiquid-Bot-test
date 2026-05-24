# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T13:37:19.016925+00:00`
- Price records: `672`
- Market context records: `1741`
- Flow alert records: `6916`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8852`

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

- `market_context_high->metal_24h` score `7.085` n `156` status `ready` deltaP `26.1932` edge `0.6584` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7987` n `196` status `ready` deltaP `20.3615` edge `0.5241` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.5813` n `156` status `ready` deltaP `15.7068` edge `0.8091` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.3643` n `156` status `ready` deltaP `18.7241` edge `0.3617` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.1177` n `196` status `ready` deltaP `21.1952` edge `0.4424` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0697` n `196` status `ready` deltaP `13.4893` edge `0.393` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9076` n `196` status `ready` deltaP `15.5021` edge `0.2484` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.7939` n `156` status `ready` deltaP `17.1999` edge `0.608` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7237` n `196` status `ready` deltaP `7.2712` edge `0.1142` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.7171` n `196` status `ready` deltaP `10.4935` edge `0.0987` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.5646` n `156` status `ready` deltaP `20.1795` edge `0.7711` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.1954` n `156` status `ready` deltaP `21.2694` edge `1.0554` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1537` n `196` status `ready` deltaP `4.598` edge `0.0895` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0179` n `196` status `ready` deltaP `4.6713` edge `0.0512` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2766` n `196` status `ready` deltaP `3.1682` edge `0.019` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3069` n `196` status `ready` deltaP `12.2916` edge `0.1479` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5066` n `196` status `ready` deltaP `6.2447` edge `0.027` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6809` n `196` status `ready` deltaP `-3.4156` edge `-0.0013` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.6875` n `156` status `ready` deltaP `6.2269` edge `0.0061` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.6378` n `196` status `ready` deltaP `0.3391` edge `0.0082` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
