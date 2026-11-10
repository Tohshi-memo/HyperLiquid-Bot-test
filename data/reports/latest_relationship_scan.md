# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T00:52:34.413328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `38.4743` n `88` status `ready` deltaP `7.525` edge `3.2008` maxDD `-0.9153`
- `market_context_high->equity_24h` score `20.048` n `63` status `ready` deltaP `28.8768` edge `2.6182` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.3957` n `63` status `ready` deltaP `23.76` edge `0.3232` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `1.8639` n `63` status `ready` deltaP `13.4687` edge `0.6586` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3101` n `63` status `ready` deltaP `12.8773` edge `-0.0047` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3437` n `88` status `ready` deltaP `3.9467` edge `0.0127` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5748` n `88` status `ready` deltaP `-0.6056` edge `-0.0014` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8279` n `88` status `ready` deltaP `0.3464` edge `-0.0107` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8506` n `88` status `ready` deltaP `-1.9263` edge `0.0144` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0765` n `88` status `ready` deltaP `-8.8527` edge `0.0041` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1498` n `88` status `ready` deltaP `-2.2727` edge `0.0061` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3685` n `88` status `ready` deltaP `-15.1061` edge `-0.0063` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7726` n `88` status `ready` deltaP `-8.5533` edge `0.0144` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9117` n `88` status `ready` deltaP `0.9322` edge `-0.0534` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1731` n `88` status `ready` deltaP `-7.525` edge `-0.0103` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4381` n `63` status `ready` deltaP `-15.576` edge `-0.0498` maxDD `-3.3815`
- `market_context_high->commodity_24h` score `-2.6559` n `63` status `ready` deltaP `-16.9817` edge `0.0357` maxDD `-10.7054`
- `market_context_high->crypto_major_1h` score `-3.2079` n `88` status `ready` deltaP `-5.4096` edge `-0.1129` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3935` n `88` status `ready` deltaP `-2.439` edge `-0.2187` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1038` n `88` status `ready` deltaP `2.245` edge `-0.2618` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
