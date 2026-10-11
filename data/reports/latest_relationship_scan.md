# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T18:37:25.257960+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8206`

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

- `market_context_high->unknown_24h` score `1381.036` n `40` status `ready` deltaP `-21.1806` edge `115.2639` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `58.1301` n `83` status `ready` deltaP `-5.6953` edge `4.9402` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `9.1785` n `95` status `ready` deltaP `-1.8909` edge `0.8111` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.796` n `40` status `ready` deltaP `27.6736` edge `0.5914` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.388` n `40` status `ready` deltaP `52.4306` edge `0.1828` maxDD `0.0`
- `market_context_high->fx_24h` score `3.2505` n `40` status `ready` deltaP `36.7708` edge `0.0387` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.5553` n `40` status `ready` deltaP `-20.5903` edge `0.5817` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.835` n `83` status `ready` deltaP `13.4918` edge `0.008` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.5367` n `95` status `ready` deltaP `6.4119` edge `0.1054` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.316` n `83` status `ready` deltaP `10.0004` edge `0.013` maxDD `-1.6002`
- `market_context_high->crypto_major_4h` score `0.0204` n `83` status `ready` deltaP `0.3417` edge `0.2109` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `-0.0141` n `95` status `ready` deltaP `3.4037` edge `0.0045` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0519` n `95` status `ready` deltaP `2.8049` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.1203` n `95` status `ready` deltaP `1.434` edge `0.0693` maxDD `-3.7778`
- `market_context_high->metal_4h` score `-0.1571` n `83` status `ready` deltaP `5.6972` edge `0.0212` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.245` n `95` status `ready` deltaP `5.2001` edge `0.0038` maxDD `-0.7107`
- `market_context_high->crypto_alt_4h` score `-0.296` n `83` status `ready` deltaP `-3.3757` edge `0.2404` maxDD `-13.8008`
- `market_context_high->index_1h` score `-0.6626` n `95` status `ready` deltaP `-2.7718` edge `-0.0014` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.6924` n `83` status `ready` deltaP `-3.4987` edge `0.0046` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-0.9324` n `95` status `ready` deltaP `-5.3073` edge `0.0028` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
