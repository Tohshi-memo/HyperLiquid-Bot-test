# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T20:07:32.565856+00:00`
- Price records: `672`
- Market context records: `5074`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_24h` score `12.4346` n `81` status `ready` deltaP `27.9707` edge `0.884` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `11.3619` n `103` status `ready` deltaP `3.8428` edge `0.9713` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.3768` n `95` status `ready` deltaP `21.0927` edge `0.743` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.7778` n `95` status `ready` deltaP `19.8219` edge `0.5546` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.0797` n `95` status `ready` deltaP `18.3264` edge `0.5429` maxDD `-8.3416`
- `market_context_high->metal_4h` score `1.0628` n `95` status `ready` deltaP `11.1249` edge `0.1223` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9492` n `95` status `ready` deltaP `7.1615` edge `0.1871` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.743` n `103` status `ready` deltaP `7.3586` edge `0.0702` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.6825` n `103` status `ready` deltaP `6.174` edge `0.1182` maxDD `-5.1989`
- `market_context_high->crypto_alt_1h` score `0.6471` n `103` status `ready` deltaP `4.9721` edge `0.1018` maxDD `-3.8153`
- `market_context_high->metal_1h` score `0.5282` n `103` status `ready` deltaP `8.5605` edge `0.0366` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.1426` n `95` status `ready` deltaP `6.8999` edge `0.042` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2423` n `103` status `ready` deltaP `1.3836` edge `0.0121` maxDD `-0.5245`
- `market_context_high->commodity_1h` score `-0.3179` n `103` status `ready` deltaP `3.4024` edge `0.0168` maxDD `-1.278`
- `market_context_high->fx_24h` score `-0.4452` n `81` status `ready` deltaP `2.3727` edge `0.0033` maxDD `-1.7626`
- `market_context_high->commodity_4h` score `-0.7416` n `95` status `ready` deltaP `7.8578` edge `0.0071` maxDD `-4.7025`
- `market_context_high->fx_4h` score `-0.9339` n `95` status `ready` deltaP `-3.1033` edge `-0.0001` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.5904` n `103` status `ready` deltaP `-10.0401` edge `-0.004` maxDD `-0.5945`
- `market_context_high->commodity_24h` score `-2.9682` n `81` status `ready` deltaP `7.5231` edge `-0.0098` maxDD `-22.3385`
- `market_context_high->metal_24h` score `-3.7549` n `81` status `ready` deltaP `1.1381` edge `0.0565` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
