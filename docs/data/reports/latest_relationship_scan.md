# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T18:22:31.118694+00:00`
- Price records: `672`
- Market context records: `7905`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `15.5343` n `95` status `ready` deltaP `29.4463` edge `1.2324` maxDD `-6.0681`
- `market_context_high->metal_24h` score `6.9114` n `95` status `ready` deltaP `34.0655` edge `0.3708` maxDD `-0.0894`
- `market_context_high->equity_4h` score `5.8583` n `101` status `ready` deltaP `20.9662` edge `0.4377` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.1954` n `101` status `ready` deltaP `22.6405` edge `0.068` maxDD `-0.8791`
- `market_context_high->metal_4h` score `1.9953` n `101` status `ready` deltaP `17.4022` edge `0.1125` maxDD `-0.979`
- `market_context_high->commodity_24h` score `1.9951` n `95` status `ready` deltaP `21.091` edge `0.184` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.5507` n `101` status `ready` deltaP `11.8419` edge `0.162` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4554` n `104` status `ready` deltaP `12.1708` edge `0.1219` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.3431` n `95` status `ready` deltaP `6.4072` edge `0.1404` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.3215` n `101` status `ready` deltaP `13.7451` edge `0.1903` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.2126` n `95` status `ready` deltaP `32.6444` edge `0.0466` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1317` n `104` status `ready` deltaP `13.3752` edge `0.046` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.7239` n `104` status `ready` deltaP `12.5` edge `0.02` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.3695` n `104` status `ready` deltaP `6.3047` edge `0.0266` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2961` n `104` status `ready` deltaP `4.5947` edge `0.0373` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1772` n `104` status `ready` deltaP `1.952` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2304` n `101` status `ready` deltaP `5.8543` edge `0.0062` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.2399` n `101` status `ready` deltaP `5.4955` edge `0.0178` maxDD `-2.2874`
- `market_context_high->commodity_1h` score `-0.4971` n `104` status `ready` deltaP `1.9548` edge `0.0024` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.2195` n `104` status `ready` deltaP `6.132` edge `-0.1835` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
