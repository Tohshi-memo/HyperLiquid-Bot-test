# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T16:37:36.797429+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1495.616` n `98` status `ready` deltaP `3.4602` edge `124.6116` maxDD `0.0`
- `news_risk_high->equity_24h` score `60.2124` n `46` status `ready` deltaP `67.5793` edge `4.6378` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.8398` n `46` status `ready` deltaP `32.9397` edge `2.1819` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `17.1129` n `46` status `ready` deltaP `50.5302` edge `1.1473` maxDD `-3.9811`
- `market_context_high->crypto_major_24h` score `14.8603` n `98` status `ready` deltaP `44.386` edge `1.9363` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0955` n `98` status `ready` deltaP `30.4463` edge `1.8165` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.4165` n `46` status `ready` deltaP `58.9288` edge `0.4222` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.6732` n `46` status `ready` deltaP `54.3253` edge `0.3606` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2836` n `46` status `ready` deltaP `18.0683` edge `1.3921` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `6.5212` n `46` status `ready` deltaP `30.9252` edge `0.4203` maxDD `-4.6427`
- `news_risk_high->metal_4h` score `6.03` n `46` status `ready` deltaP `50.7954` edge `0.1766` maxDD `-0.3525`
- `news_risk_high->crypto_major_4h` score `5.9248` n `46` status `ready` deltaP `24.0986` edge `0.398` maxDD `-3.5274`
- `news_risk_high->equity_1h` score `4.1076` n `46` status `ready` deltaP `22.8586` edge `0.2458` maxDD `-3.1376`
- `news_risk_high->index_4h` score `3.88` n `46` status `ready` deltaP `34.935` edge `0.1163` maxDD `-0.4028`
- `news_risk_high->commodity_4h` score `3.1202` n `46` status `ready` deltaP `31.9592` edge `0.0723` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3009` n `46` status `ready` deltaP `25.8591` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->crypto_major_1h` score `2.0585` n `46` status `ready` deltaP `19.4871` edge `0.1099` maxDD `-4.1283`
- `news_risk_high->crypto_alt_1h` score `1.794` n `46` status `ready` deltaP `18.3611` edge `0.0958` maxDD `-3.83`
- `news_risk_high->index_1h` score `1.4926` n `46` status `ready` deltaP `18.8102` edge `0.0242` maxDD `-0.3507`
- `news_risk_high->metal_24h` score `0.5533` n `46` status `ready` deltaP `16.1727` edge `0.1804` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
