# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T14:07:15.639038+00:00`
- Price records: `672`
- Market context records: `7781`
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

- `market_context_high->equity_24h` score `7.1305` n `132` status `ready` deltaP `27.5842` edge `0.5445` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4318` n `133` status `ready` deltaP `13.6187` edge `0.2376` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9758` n `133` status `ready` deltaP `12.8585` edge `0.0397` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.7262` n `132` status `ready` deltaP `23.9653` edge `0.0421` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.6961` n `133` status `ready` deltaP `13.1269` edge `0.1423` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.6224` n `133` status `ready` deltaP `2.4281` edge `0.2549` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.505` n `133` status `ready` deltaP `7.5898` edge `0.1032` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.491` n `133` status `ready` deltaP `7.5955` edge `0.0762` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3038` n `133` status `ready` deltaP `8.0438` edge `0.0147` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2123` n `133` status `ready` deltaP `6.622` edge `0.0329` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.134` n `133` status `ready` deltaP `4.1286` edge `0.0269` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0331` n `133` status `ready` deltaP `4.8963` edge `0.0105` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2421` n `133` status `ready` deltaP `10.5585` edge `0.0444` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.363` n `133` status `ready` deltaP `1.2746` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.7225` n `132` status `ready` deltaP `10.0412` edge `0.0312` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9429` n `133` status `ready` deltaP `0.5189` edge `0.0183` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3643` n `133` status `ready` deltaP `-2.0211` edge `0.0014` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6092` n `133` status `ready` deltaP `-0.0814` edge `0.0719` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.8062` n `132` status `ready` deltaP `-11.3109` edge `0.0541` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.1314` n `133` status `ready` deltaP `-0.2262` edge `-0.1171` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
