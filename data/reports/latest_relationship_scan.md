# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T11:22:10.622295+00:00`
- Price records: `641`
- Market context records: `749`
- Flow alert records: `2116`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.0246` n `146` status `ready` deltaP `31.0469` edge `0.9118` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6405` n `146` status `ready` deltaP `7.572` edge `0.5077` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.3696` n `146` status `ready` deltaP `2.4169` edge `0.2142` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.2436` n `146` status `ready` deltaP `0.8508` edge `0.2345` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.3674` n `167` status `ready` deltaP `3.6732` edge `0.0027` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4688` n `156` status `ready` deltaP `5.8312` edge `0.0092` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.5768` n `167` status `ready` deltaP `1.6167` edge `0.0386` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9813` n `167` status `ready` deltaP `0.1314` edge `0.0027` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0244` n `167` status `ready` deltaP `6.2493` edge `-0.0007` maxDD `-11.4508`
- `market_context_high->equity_1h` score `-1.1291` n `167` status `ready` deltaP `-1.7643` edge `-0.0013` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.354` n `167` status `ready` deltaP `5.0452` edge `-0.015` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5578` n `167` status `ready` deltaP `-4.3721` edge `-0.0235` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.657` n `156` status `ready` deltaP `17.0728` edge `0.1187` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7888` n `156` status `ready` deltaP `1.4555` edge `-0.0065` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.989` n `167` status `ready` deltaP `-3.5355` edge `-0.0355` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.2483` n `156` status `ready` deltaP `2.1928` edge `0.055` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6403` n `156` status `ready` deltaP `-1.4431` edge `0.0048` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7447` n `156` status `ready` deltaP `-5.9643` edge `0.0778` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.8065` n `156` status `ready` deltaP `4.7415` edge `-0.161` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.4339` n `146` status `ready` deltaP `-16.1497` edge `-0.0718` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
