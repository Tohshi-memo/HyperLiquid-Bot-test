# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T16:07:24.333881+00:00`
- Price records: `672`
- Market context records: `7156`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.2471` n `156` status `ready` deltaP `11.6831` edge `0.0127` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2541` n `164` status `ready` deltaP `3.3482` edge `0.0021` maxDD `-0.3142`
- `market_context_high->unknown_1h` score `-0.5464` n `164` status `ready` deltaP `-1.5956` edge `0.0293` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6341` n `164` status `ready` deltaP `-0.482` edge `0.0258` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.663` n `164` status `ready` deltaP `3.1875` edge `0.0348` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.6877` n `164` status `ready` deltaP `-1.4532` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.6988` n `164` status `ready` deltaP `1.8804` edge `-0.0043` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.72` n `164` status `ready` deltaP `-6.8169` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.9899` n `156` status `ready` deltaP `-6.3047` edge `0.0129` maxDD `-6.0783`
- `market_context_high->commodity_4h` score `-2.0979` n `156` status `ready` deltaP `-4.964` edge `-0.0382` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9436` n `156` status `ready` deltaP `-10.5495` edge `-0.0122` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5662` n `164` status `ready` deltaP `-0.88` edge `-0.0406` maxDD `-15.3907`
- `market_context_high->index_4h` score `-3.9558` n `156` status `ready` deltaP `-2.482` edge `-0.0432` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5024` n `133` status `ready` deltaP `-13.4581` edge `-0.1546` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9132` n `133` status `ready` deltaP `-15.1838` edge `-0.0255` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.9212` n `156` status `ready` deltaP `2.4664` edge `0.0088` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5902` n `156` status `ready` deltaP `-3.6742` edge `-0.0317` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.098` n `133` status `ready` deltaP `-32.7029` edge `-0.1088` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7526` n `133` status `ready` deltaP `-32.1232` edge `-0.1971` maxDD `-40.7836`
- `market_context_high->equity_4h` score `-14.8036` n `156` status `ready` deltaP `-4.5302` edge `-0.218` maxDD `-66.5013`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
