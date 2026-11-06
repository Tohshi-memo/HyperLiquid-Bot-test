# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T23:52:28.793411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.9885` n `75` status `ready` deltaP `8.4004` edge `0.1613` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.2493` n `75` status `ready` deltaP `9.2765` edge `0.0179` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.136` n `75` status `ready` deltaP `8.8443` edge `0.0038` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.1122` n `75` status `ready` deltaP `2.7345` edge `0.0511` maxDD `-1.396`
- `news_risk_high->index_24h` score `0.0562` n `75` status `ready` deltaP `4.8473` edge `0.1417` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.0124` n `75` status `ready` deltaP `6.4918` edge `0.0029` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.198` n `75` status `ready` deltaP `-2.0764` edge `0.0416` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2164` n `75` status `ready` deltaP `1.3593` edge `0.0018` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4233` n `75` status `ready` deltaP `-1.8643` edge `-0.0061` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-1.0819` n `75` status `ready` deltaP `-4.6387` edge `-0.0139` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-1.2809` n `75` status `ready` deltaP `-5.126` edge `-0.0395` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.3527` n `75` status `ready` deltaP `-2.7066` edge `-0.0326` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-2.6378` n `75` status `ready` deltaP `-6.6463` edge `-0.0069` maxDD `-9.1553`
- `news_risk_high->commodity_1h` score `-2.8851` n `75` status `ready` deltaP `-18.014` edge `-0.0077` maxDD `-1.6769`
- `news_risk_high->equity_24h` score `-2.9707` n `75` status `ready` deltaP `22.1667` edge `0.63` maxDD `-86.0244`
- `news_risk_high->metal_24h` score `-3.2783` n `75` status `ready` deltaP `0.3473` edge `-0.233` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.9692` n `75` status `ready` deltaP `-25.3902` edge `-0.0017` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.7886` n `75` status `ready` deltaP `-9.9613` edge `-0.069` maxDD `-14.0916`
- `news_risk_high->commodity_24h` score `-9.6362` n `75` status `ready` deltaP `-26.4306` edge `-0.0589` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.0788` n `75` status `ready` deltaP `-29.9514` edge `-0.0399` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
