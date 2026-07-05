# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T04:52:30.692288+00:00`
- Price records: `672`
- Market context records: `5737`
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

- `market_context_high->equity_24h` score `0.8507` n `218` status `ready` deltaP `15.0086` edge `0.5169` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1462` n `285` status `ready` deltaP `7.6728` edge `0.1249` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2061` n `285` status `ready` deltaP `3.0854` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4549` n `285` status `ready` deltaP `1.4855` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6932` n `285` status `ready` deltaP `2.4635` edge `0.0265` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7917` n `285` status `ready` deltaP `-2.1872` edge `-0.0062` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.9004` n `285` status `ready` deltaP `2.4819` edge `0.0319` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9635` n `285` status `ready` deltaP `1.3358` edge `0.0312` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.0607` n `218` status `ready` deltaP `11.9027` edge `0.043` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1559` n `285` status `ready` deltaP `1.4752` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2627` n `285` status `ready` deltaP `2.5567` edge `0.0056` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6471` n `285` status `ready` deltaP `-7.8461` edge `-0.0495` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.8892` n `285` status `ready` deltaP `7.1497` edge `0.1421` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.0283` n `218` status `ready` deltaP `-0.1624` edge `0.0273` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.6969` n `285` status `ready` deltaP `-2.0587` edge `-0.0268` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-4.0531` n `285` status `ready` deltaP `5.1823` edge `0.0967` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.1032` n `218` status `ready` deltaP `8.0642` edge `0.05` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.7263` n `218` status `ready` deltaP `-8.4703` edge `-0.2456` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.6693` n `218` status `ready` deltaP `-11.9633` edge `-0.0787` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
