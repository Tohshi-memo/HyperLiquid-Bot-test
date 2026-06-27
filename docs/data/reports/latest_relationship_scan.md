# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T22:07:26.925811+00:00`
- Price records: `672`
- Market context records: `4977`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `18.9596` n `95` status `ready` deltaP `5.7989` edge `1.5914` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.3976` n `88` status `ready` deltaP `27.4806` edge `0.9025` maxDD `-1.8723`
- `market_context_high->crypto_major_4h` score `6.8264` n `88` status `ready` deltaP `18.0571` edge `0.5709` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.2955` n `88` status `ready` deltaP `18.653` edge `0.5355` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8723` n `82` status `ready` deltaP `27.9175` edge `0.3375` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.4778` n `88` status `ready` deltaP `12.5416` edge `0.1266` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9688` n `88` status `ready` deltaP `10.8371` edge `0.1901` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6544` n `88` status `ready` deltaP `8.3565` edge `0.045` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.4574` n `95` status `ready` deltaP `6.2386` edge `0.0744` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.2571` n `95` status `ready` deltaP `3.5109` edge `0.1134` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.2045` n `95` status `ready` deltaP `5.7847` edge `0.0899` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.161` n `95` status `ready` deltaP `1.4056` edge `0.0352` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3926` n `95` status `ready` deltaP `1.2654` edge `0.0072` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4888` n `95` status `ready` deltaP `0.0772` edge `0.0123` maxDD `-0.7054`
- `market_context_high->fx_24h` score `-0.503` n `82` status `ready` deltaP `2.2824` edge `-0.0035` maxDD `-1.7626`
- `market_context_high->fx_4h` score `-1.1269` n `88` status `ready` deltaP `-6.6658` edge `-0.003` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2826` n `88` status `ready` deltaP `4.2267` edge `-0.0098` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.6713` n `95` status `ready` deltaP `-11.2213` edge `-0.0045` maxDD `-0.4639`
- `market_context_high->commodity_24h` score `-3.2672` n `82` status `ready` deltaP `14.2065` edge `-0.0027` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9208` n `82` status `ready` deltaP `-6.7877` edge `0.014` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
