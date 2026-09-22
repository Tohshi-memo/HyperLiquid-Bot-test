# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T05:22:26.973845+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9986`

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

- `market_context_high->unknown_4h` score `50.077` n `46` status `ready` deltaP `7.3171` edge `4.1243` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `35.224` n `46` status `ready` deltaP `22.0411` edge `2.804` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.7951` n `46` status `ready` deltaP `20.8333` edge `1.5107` maxDD `0.0`
- `market_context_high->equity_24h` score `17.2349` n `46` status `ready` deltaP `15.2703` edge `1.3445` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.5069` n `101` status `ready` deltaP `-3.3141` edge `1.3335` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6556` n `46` status `ready` deltaP `20.1314` edge `0.3458` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.3141` n `101` status `ready` deltaP `-2.9291` edge `0.7838` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.8048` n `101` status `ready` deltaP `34.4815` edge `0.2603` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6771` n `101` status `ready` deltaP `13.2788` edge `0.2555` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.299` n `101` status `ready` deltaP `13.9859` edge `0.1449` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1572` n `101` status `ready` deltaP `16.3276` edge `0.1967` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9737` n `46` status `ready` deltaP `23.3165` edge `0.0224` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6276` n `101` status `ready` deltaP `15.6326` edge `0.0837` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1215` n `46` status `ready` deltaP `8.974` edge `0.0931` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0872` n `46` status `ready` deltaP `8.1389` edge `0.067` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9336` n `46` status `ready` deltaP `7.3614` edge `0.053` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8301` n `101` status `ready` deltaP `14.8907` edge `0.0335` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6471` n `46` status `ready` deltaP `10.2057` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.543` n `101` status `ready` deltaP `13.8495` edge `0.0131` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.5397` n `46` status `ready` deltaP `1.061` edge `0.0902` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
