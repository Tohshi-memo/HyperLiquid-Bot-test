# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T03:37:25.718713+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9972`

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

- `market_context_high->unknown_4h` score `48.8542` n `46` status `ready` deltaP `7.3171` edge `4.0224` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `36.4217` n `46` status `ready` deltaP `23.2564` edge `2.8957` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `20.7719` n `46` status `ready` deltaP `22.0486` edge `1.584` maxDD `0.0`
- `market_context_high->equity_24h` score `17.6777` n `46` status `ready` deltaP `16.4855` edge `1.3733` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `8.7045` n `101` status `ready` deltaP `-2.0988` edge `1.4252` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.741` n `46` status `ready` deltaP `20.4786` edge `0.3506` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `4.2909` n `101` status `ready` deltaP `-1.7138` edge `0.8571` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `2.7504` n `101` status `ready` deltaP `13.4312` edge `0.2606` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.7112` n `101` status `ready` deltaP `33.2663` edge `0.2564` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3062` n `101` status `ready` deltaP `13.9859` edge `0.1455` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.186` n `101` status `ready` deltaP `16.3276` edge `0.1991` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9773` n `46` status `ready` deltaP `23.3165` edge `0.0227` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6731` n `101` status `ready` deltaP `15.932` edge `0.0855` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1949` n `46` status `ready` deltaP `9.1264` edge `0.0982` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0752` n `46` status `ready` deltaP `8.1389` edge `0.066` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8653` n `46` status `ready` deltaP `6.9123` edge `0.0503` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.7219` n `101` status `ready` deltaP `13.8236` edge `0.0316` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6088` n `46` status `ready` deltaP `9.7566` edge `0.011` maxDD `-0.0249`
- `market_context_high->crypto_major_1h` score `0.5853` n `46` status `ready` deltaP `1.3604` edge `0.092` maxDD `-2.1836`
- `news_risk_high->metal_1h` score `0.5574` n `101` status `ready` deltaP `13.9992` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
