# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T20:07:26.757983+00:00`
- Price records: `672`
- Market context records: `7702`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.6327` n `132` status `ready` deltaP `19.396` edge `0.3076` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.3416` n `133` status `ready` deltaP `15.8708` edge `0.1778` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1197` n `133` status `ready` deltaP `13.3076` edge `0.0487` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8557` n `133` status `ready` deltaP `8.8093` edge `0.1243` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.8339` n `133` status `ready` deltaP `3.3455` edge `0.2759` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6855` n `133` status `ready` deltaP `8.7968` edge `0.0844` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3878` n `133` status `ready` deltaP `8.9447` edge `0.0157` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1533` n `133` status `ready` deltaP `3.5298` edge `0.0325` maxDD `-1.4603`
- `market_context_high->fx_24h` score `-0.0699` n `132` status `ready` deltaP `11.596` edge `0.0225` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.113` n `133` status `ready` deltaP `12.5463` edge `0.0477` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.2169` n `133` status `ready` deltaP `3.2446` edge `0.0062` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.3213` n `133` status `ready` deltaP `2.9523` edge `0.0129` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.5071` n `133` status `ready` deltaP `-0.377` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.6245` n `133` status `ready` deltaP `2.8548` edge `0.138` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8255` n `133` status `ready` deltaP `1.7165` edge `0.0201` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.2734` n `133` status `ready` deltaP `-0.3759` edge `-0.0446` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4235` n `133` status `ready` deltaP `1.5954` edge `0.0762` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5615` n `133` status `ready` deltaP `-5.0792` edge `-0.0035` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7273` n `132` status `ready` deltaP `5.6858` edge `-0.0235` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2483` n `133` status `ready` deltaP `15.3023` edge `-0.1637` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
