# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T02:22:27.364437+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `120.3899` n `96` status `ready` deltaP `-0.7859` edge `10.0792` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.794` n `95` status `ready` deltaP `2.4743` edge `5.9975` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.8574` n `53` status `ready` deltaP `30.4507` edge `0.7154` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.9621` n `53` status `ready` deltaP `25.1606` edge `0.7244` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.449` n `65` status `ready` deltaP `32.8565` edge `0.5887` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.3504` n `65` status `ready` deltaP `20.7012` edge `0.5256` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.6184` n `65` status `ready` deltaP `16.242` edge `0.2866` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.3418` n `95` status `ready` deltaP `18.4435` edge `0.3092` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4407` n `65` status `ready` deltaP `23.9583` edge `0.127` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9035` n `65` status `ready` deltaP `31.9137` edge `0.0554` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.8686` n `65` status `ready` deltaP `21.3391` edge `0.1578` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.566` n `65` status `ready` deltaP `10.4652` edge `0.1796` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.1988` n `96` status `ready` deltaP `15.1447` edge `0.1273` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.0821` n `65` status `ready` deltaP `19.0784` edge `0.0879` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.071` n `65` status `ready` deltaP `25.6172` edge `0.0168` maxDD `-0.1997`
- `market_context_high->fx_24h` score `1.9274` n `53` status `ready` deltaP `23.2705` edge `0.0976` maxDD `-1.703`
- `market_context_high->equity_24h` score `1.6353` n `53` status `ready` deltaP `3.5279` edge `0.133` maxDD `-0.6196`
- `market_context_high->fx_4h` score `1.4429` n `95` status `ready` deltaP `25.1717` edge `0.0281` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.3592` n `65` status `ready` deltaP `4.2699` edge `0.1367` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.2302` n `95` status `ready` deltaP `3.8591` edge `0.2557` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
