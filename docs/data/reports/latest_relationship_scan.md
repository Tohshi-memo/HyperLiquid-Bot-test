# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T18:07:36.657326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4238`

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

- `market_context_high->unknown_1h` score `368.9756` n `50` status `ready` deltaP `11.9222` edge `30.6734` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.9738` n `50` status `ready` deltaP `12.6524` edge `24.7468` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.1571` n `50` status `ready` deltaP `29.4593` edge `1.1537` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.7611` n `50` status `ready` deltaP `37.1127` edge `0.8743` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6708` n `62` status `ready` deltaP `29.9575` edge `0.738` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4327` n `68` status `ready` deltaP `37.8766` edge `0.6372` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4986` n `68` status `ready` deltaP `27.2239` edge `0.5778` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0328` n `50` status `ready` deltaP `16.1707` edge `0.5486` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.7819` n `50` status `ready` deltaP `16.3415` edge `0.5018` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5842` n `62` status `ready` deltaP `33.4629` edge `0.1748` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8607` n `68` status `ready` deltaP `27.2686` edge `0.2012` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1643` n `50` status `ready` deltaP `13.7545` edge `0.2383` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.0496` n `68` status `ready` deltaP `33.4559` edge `0.0573` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8863` n `68` status `ready` deltaP `12.9095` edge `0.19` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8215` n `50` status `ready` deltaP `12.2036` edge `0.1988` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3746` n `68` status `ready` deltaP `20.1399` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9971` n `68` status `ready` deltaP `24.6478` edge `0.0171` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.6076` n `50` status `ready` deltaP `22.2874` edge `0.0118` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.509` n `68` status `ready` deltaP `5.1074` edge `0.1436` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
