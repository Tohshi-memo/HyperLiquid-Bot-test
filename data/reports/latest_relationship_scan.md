# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T07:37:27.696700+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `48.115` n `46` status `ready` deltaP `7.3171` edge `3.9608` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `33.821` n `46` status `ready` deltaP `20.4786` edge `2.6975` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `18.5877` n `46` status `ready` deltaP `19.2708` edge `1.4205` maxDD `0.0`
- `market_context_high->equity_24h` score `16.8684` n `46` status `ready` deltaP `14.2286` edge `1.3209` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `6.1039` n `101` status `ready` deltaP `-4.8766` edge `1.227` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6112` n `46` status `ready` deltaP `20.1314` edge `0.3421` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `2.8953` n `101` status `ready` deltaP `35.6968` edge `0.2638` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.5743` n `101` status `ready` deltaP `12.669` edge `0.251` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.1683` n `101` status `ready` deltaP `13.2374` edge `0.139` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.11` n `101` status `ready` deltaP `16.0227` edge `0.1948` maxDD `-8.0625`
- `news_risk_high->crypto_alt_24h` score `2.1067` n `101` status `ready` deltaP `-4.4916` edge `0.6936` maxDD `-32.7147`
- `market_context_high->index_4h` score `2.0575` n `46` status `ready` deltaP `24.0787` edge `0.0243` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5065` n `101` status `ready` deltaP `14.8841` edge `0.0786` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.3296` n `46` status `ready` deltaP `9.0536` edge `0.0811` maxDD `-0.4529`
- `market_context_high->crypto_alt_4h` score `1.0187` n `46` status `ready` deltaP `8.3642` edge `0.0886` maxDD `-2.7574`
- `market_context_high->equity_1h` score `0.93` n `46` status `ready` deltaP `7.3614` edge `0.0527` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8971` n `101` status `ready` deltaP `15.6529` edge `0.034` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6555` n `46` status `ready` deltaP `10.3554` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5262` n `101` status `ready` deltaP `13.6998` edge `0.0127` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4187` n `46` status `ready` deltaP `0.3125` edge `0.0851` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
