# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T19:52:28.138345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4155`

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

- `news_risk_high->equity_4h` score `1.9353` n `91` status `ready` deltaP `15.5974` edge `0.2347` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.9078` n `91` status `ready` deltaP `15.0195` edge `0.0233` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.5225` n `91` status `ready` deltaP `6.095` edge `0.0813` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.3373` n `91` status `ready` deltaP `12.236` edge `0.007` maxDD `-0.2931`
- `news_risk_high->metal_1h` score `-0.2733` n `91` status `ready` deltaP `0.6005` edge `-0.0033` maxDD `-0.5256`
- `news_risk_high->fx_4h` score `-0.3078` n `91` status `ready` deltaP `1.7187` edge `-0.0011` maxDD `-0.3194`
- `news_risk_high->crypto_major_4h` score `-0.3582` n `91` status `ready` deltaP `2.6836` edge `0.1048` maxDD `-9.1553`
- `news_risk_high->fx_1h` score `-0.4324` n `91` status `ready` deltaP `-2.2438` edge `-0.0005` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.4783` n `91` status `ready` deltaP `3.7442` edge `0.0365` maxDD `-5.8225`
- `news_risk_high->index_24h` score `-0.506` n `91` status `ready` deltaP `0.002` edge `0.1413` maxDD `-6.6786`
- `news_risk_high->equity_24h` score `-0.6815` n `91` status `ready` deltaP `27.6992` edge `0.8866` maxDD `-86.0244`
- `news_risk_high->crypto_major_1h` score `-0.6931` n `91` status `ready` deltaP `-1.451` edge `0.0147` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-0.9493` n `91` status `ready` deltaP `-0.0536` edge `-0.0308` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.0164` n `91` status `ready` deltaP `-8.8216` edge `0.0189` maxDD `-0.25`
- `news_risk_high->crypto_alt_4h` score `-1.129` n `91` status `ready` deltaP `-0.8544` edge `0.1246` maxDD `-14.0916`
- `news_risk_high->metal_24h` score `-2.9056` n `91` status `ready` deltaP `4.1842` edge `-0.2108` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.1771` n `91` status `ready` deltaP `-18.7307` edge `-0.0125` maxDD `-2.5244`
- `news_risk_high->commodity_4h` score `-4.3313` n `91` status `ready` deltaP `-26.6819` edge `-0.0067` maxDD `-5.4425`
- `news_risk_high->crypto_major_24h` score `-6.6591` n `91` status `ready` deltaP `-17.3558` edge `0.1123` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.3676` n `91` status `ready` deltaP `-25.41` edge `-0.0138` maxDD `-30.4613`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
