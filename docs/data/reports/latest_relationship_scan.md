# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T09:37:48.467417+00:00`
- Price records: `672`
- Market context records: `7762`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `5.988` n `132` status `ready` deltaP `24.4483` edge `0.4702` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.0066` n `133` status `ready` deltaP `10.4937` edge `0.223` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.8475` n `133` status `ready` deltaP `11.9603` edge `0.035` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5301` n `132` status `ready` deltaP `21.0036` edge `0.0367` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4841` n `133` status `ready` deltaP `12.5172` edge `0.1287` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.4121` n `133` status `ready` deltaP `1.9694` edge `0.231` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3638` n `133` status `ready` deltaP `7.4454` edge `0.0666` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.305` n `133` status `ready` deltaP `8.194` edge `0.0138` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2438` n `133` status `ready` deltaP `6.9801` edge `0.0855` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0225` n `133` status `ready` deltaP `3.5298` edge `0.0216` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `-0.0158` n `133` status `ready` deltaP `4.9401` edge `0.0251` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0547` n `133` status `ready` deltaP `4.7461` edge `0.0097` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.26` n `133` status `ready` deltaP `10.5585` edge `0.0421` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.411` n `133` status `ready` deltaP `0.674` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8794` n `133` status `ready` deltaP `1.2674` edge `0.0186` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.3142` n `132` status `ready` deltaP `6.9053` edge `0.0028` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4769` n `133` status `ready` deltaP `-3.8559` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5618` n `133` status `ready` deltaP `0.3759` edge `0.0728` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.1042` n `132` status `ready` deltaP `-14.4467` edge `0.0368` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3243` n `133` status `ready` deltaP `-2.0226` edge `-0.1212` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
