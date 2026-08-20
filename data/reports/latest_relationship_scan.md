# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T03:37:27.608242+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `2.0495` n `96` status `ready` deltaP `11.001` edge `0.1863` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8308` n `96` status `ready` deltaP `15.151` edge `0.0817` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.969` n `96` status `ready` deltaP `16.361` edge `0.0104` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3548` n `96` status `ready` deltaP `11.9918` edge `0.0072` maxDD `-1.273`
- `market_context_high->index_4h` score `0.1862` n `96` status `ready` deltaP `8.8668` edge `0.0219` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1357` n `96` status `ready` deltaP `6.4236` edge `0.1579` maxDD `-4.666`
- `market_context_high->fx_4h` score `-0.0011` n `96` status `ready` deltaP `7.0376` edge `0.0032` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1352` n `96` status `ready` deltaP `3.4244` edge `0.0046` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.1632` n `96` status `ready` deltaP `5.7635` edge `-0.0293` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `-0.2721` n `96` status `ready` deltaP `17.7083` edge `-0.0901` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3416` n `96` status `ready` deltaP `-1.4721` edge `0.0019` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7051` n `96` status `ready` deltaP `-1.8546` edge `0.007` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7908` n `96` status `ready` deltaP `0.131` edge `-0.0221` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8555` n `96` status `ready` deltaP `1.9336` edge `-0.0381` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9491` n `96` status `ready` deltaP `-8.7887` edge `-0.0065` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0072` n `96` status `ready` deltaP `3.9634` edge `-0.0667` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.0685` n `96` status `ready` deltaP `7.0376` edge `-0.1172` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1062` n `96` status `ready` deltaP `-14.9305` edge `-0.001` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7928` n `96` status `ready` deltaP `-0.8681` edge `-0.0637` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-3.928` n `96` status `ready` deltaP `-13.8889` edge `-0.0802` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
