# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T10:52:27.449423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9402`

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

- `market_context_high->unknown_4h` score `83.7393` n `135` status `ready` deltaP `5.4619` edge `6.9571` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.3804` n `135` status `ready` deltaP `1.2187` edge `1.3225` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9473` n `131` status `ready` deltaP `26.7401` edge `0.0528` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4847` n `135` status `ready` deltaP `10.906` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.074` n `135` status `ready` deltaP `10.9448` edge `0.0112` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2986` n `135` status `ready` deltaP `2.2777` edge `0.01` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4583` n `135` status `ready` deltaP `5.886` edge `0.0303` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5484` n `135` status `ready` deltaP `-0.0632` edge `-0.0016` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.662` n `135` status `ready` deltaP `9.843` edge `0.0036` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.729` n `131` status `ready` deltaP `6.8808` edge `0.0179` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7633` n `135` status `ready` deltaP `3.6405` edge `0.034` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.2162` n `131` status `ready` deltaP `13.4587` edge `0.0844` maxDD `-8.0379`
- `market_context_high->equity_1h` score `-1.3435` n `135` status `ready` deltaP `2.4894` edge `0.0024` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9218` n `135` status `ready` deltaP `-0.8916` edge `-0.0041` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.4826` n `135` status `ready` deltaP `-3.269` edge `-0.0229` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-2.5029` n `131` status `ready` deltaP `7.103` edge `0.0405` maxDD `-15.7143`
- `market_context_high->crypto_major_4h` score `-3.5367` n `135` status `ready` deltaP `4.7267` edge `-0.053` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6308` n `131` status `ready` deltaP `-1.7516` edge `-0.0963` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7257` n `135` status `ready` deltaP `3.7669` edge `-0.1076` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
