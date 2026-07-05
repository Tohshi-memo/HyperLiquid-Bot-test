# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T01:52:25.771232+00:00`
- Price records: `672`
- Market context records: `5725`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.9619` n `218` status `ready` deltaP `16.3975` edge `0.5219` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.163` n `275` status `ready` deltaP `7.2816` edge `0.1289` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `-0.0033` n `275` status `ready` deltaP `8.7345` edge `0.1786` maxDD `-12.9681`
- `market_context_high->fx_1h` score `-0.2217` n `285` status `ready` deltaP `2.786` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4626` n `285` status `ready` deltaP `1.3358` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6238` n `285` status `ready` deltaP `3.212` edge `0.0273` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7496` n `285` status `ready` deltaP `-1.5884` edge `-0.0048` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8884` n `285` status `ready` deltaP `2.6316` edge `0.0319` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-1.0342` n `285` status `ready` deltaP `0.8867` edge `0.0283` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1309` n `218` status `ready` deltaP `10.6875` edge `0.0421` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1459` n `275` status `ready` deltaP `1.638` edge `0.0109` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2559` n `275` status `ready` deltaP `2.6574` edge `0.0058` maxDD `-1.4288`
- `market_context_high->crypto_alt_4h` score `-1.493` n `275` status `ready` deltaP `6.5765` edge `0.1258` maxDD `-15.5248`
- `market_context_high->metal_4h` score `-2.5832` n `275` status `ready` deltaP `-6.6319` edge `-0.0494` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.906` n `218` status `ready` deltaP `1.9209` edge `0.0291` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8364` n `275` status `ready` deltaP `-3.5166` edge `-0.0287` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3677` n `218` status `ready` deltaP `7.0225` edge `0.0349` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5857` n `218` status `ready` deltaP `-6.5606` edge `-0.2403` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.4018` n `218` status `ready` deltaP `-9.8799` edge `-0.0703` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
