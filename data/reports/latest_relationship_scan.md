# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T15:22:31.001156+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->index_1h` score `0.0992` n `130` status `ready` deltaP `9.4219` edge `0.003` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0718` n `118` status `ready` deltaP `7.5237` edge `0.0093` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1355` n `130` status `ready` deltaP `2.1165` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3083` n `130` status `ready` deltaP `5.6794` edge `0.0296` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3863` n `130` status `ready` deltaP `-0.129` edge `-0.0068` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5048` n `118` status `ready` deltaP `2.7` edge `-0.0243` maxDD `-1.3402`
- `market_context_high->commodity_24h` score `-0.5547` n `105` status `ready` deltaP `3.7203` edge `0.1123` maxDD `-4.666`
- `market_context_high->index_4h` score `-0.574` n `118` status `ready` deltaP `2.2556` edge `0.01` maxDD `-2.2235`
- `market_context_high->crypto_alt_1h` score `-0.6388` n `130` status `ready` deltaP `0.7393` edge `0.022` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6717` n `130` status `ready` deltaP `-4.5325` edge `0.0007` maxDD `-1.1941`
- `market_context_high->unknown_1h` score `-0.6829` n `130` status `ready` deltaP `8.5813` edge `-0.0914` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.7172` n `118` status `ready` deltaP `-2.1781` edge `0.0076` maxDD `-2.4692`
- `market_context_high->equity_4h` score `-0.9778` n `118` status `ready` deltaP `0.3281` edge `0.0803` maxDD `-11.9613`
- `market_context_high->crypto_major_1h` score `-1.1522` n `130` status `ready` deltaP `-1.0525` edge `-0.0382` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.8244` n `118` status `ready` deltaP `1.8086` edge `-0.0371` maxDD `-5.4926`
- `market_context_high->unknown_4h` score `-2.8039` n `118` status `ready` deltaP `20.0935` edge `-0.3237` maxDD `-0.5133`
- `market_context_high->fx_24h` score `-2.8902` n `105` status `ready` deltaP `-11.2599` edge `-0.0048` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.2218` n `118` status `ready` deltaP `-0.6175` edge `-0.2456` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.232` n `105` status `ready` deltaP `-6.2897` edge `-0.0504` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.5742` n `105` status `ready` deltaP `-17.2421` edge `-0.1407` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
