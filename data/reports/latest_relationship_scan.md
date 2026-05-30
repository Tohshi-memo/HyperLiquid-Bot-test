# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T16:52:19.226783+00:00`
- Price records: `672`
- Market context records: `2370`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_alt_24h` score `21.8557` n `43` status `ready` deltaP `50.0363` edge `1.5466` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.7745` n `43` status `ready` deltaP `47.5008` edge `1.2085` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0955` n `43` status `ready` deltaP `29.7925` edge `1.0908` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.7866` n `43` status `ready` deltaP `19.7674` edge `0.9085` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.0068` n `43` status `ready` deltaP `27.8141` edge `0.5044` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.9972` n `139` status `ready` deltaP `19.7842` edge `0.9238` maxDD `-25.1408`
- `market_context_high->unknown_24h` score `5.8599` n `139` status `ready` deltaP `23.8322` edge `0.3706` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.7381` n `148` status `ready` deltaP `24.1761` edge `0.498` maxDD `-10.1468`
- `news_risk_high->index_24h` score `5.2324` n `43` status `ready` deltaP `13.0976` edge `0.3906` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `5.02` n `148` status `ready` deltaP `19.3103` edge `0.5575` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.9648` n `148` status `ready` deltaP `20.8801` edge `0.3355` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7607` n `43` status `ready` deltaP `32.0051` edge `0.3359` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4392` n `43` status `ready` deltaP `36.5351` edge `0.0615` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9589` n `43` status `ready` deltaP `25.1453` edge `0.014` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.7956` n `148` status `ready` deltaP `19.2774` edge `0.1037` maxDD `-2.2732`
- `market_context_high->crypto_major_1h` score `1.6272` n `155` status `ready` deltaP `14.1028` edge `0.161` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.6202` n `139` status `ready` deltaP `12.4451` edge `0.1038` maxDD `-1.4737`
- `market_context_high->crypto_alt_1h` score `1.3927` n `155` status `ready` deltaP `10.7842` edge `0.1629` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `0.9542` n `43` status `ready` deltaP `13.4005` edge `0.0625` maxDD `-2.7857`
- `market_context_high->equity_24h` score `0.9406` n `139` status `ready` deltaP `19.8879` edge `0.0985` maxDD `-6.8828`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
