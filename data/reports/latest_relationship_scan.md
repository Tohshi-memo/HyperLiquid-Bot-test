# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T16:52:28.898338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5913`

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

- `market_context_high->unknown_24h` score `19.2114` n `39` status `ready` deltaP `30.3819` edge `1.3984` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.8948` n `39` status `ready` deltaP `51.5091` edge `0.6652` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.3561` n `39` status `ready` deltaP `53.6458` edge `0.5887` maxDD `0.0`
- `news_risk_high->equity_4h` score `0.956` n `31` status `ready` deltaP `-7.2777` edge `0.1966` maxDD `-2.8064`
- `news_risk_high->fx_24h` score `0.9509` n `31` status `ready` deltaP `12.192` edge `0.0632` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9365` n `31` status `ready` deltaP `19.8377` edge `0.009` maxDD `-0.6947`
- `market_context_high->commodity_1h` score `0.3518` n `52` status `ready` deltaP `7.865` edge `0.0301` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3087` n `46` status `ready` deltaP `4.7256` edge `0.0927` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.3041` n `52` status `ready` deltaP `9.9148` edge `-0.006` maxDD `-0.7804`
- `news_risk_high->commodity_4h` score `0.1979` n `31` status `ready` deltaP `12.7901` edge `-0.0187` maxDD `-1.6728`
- `news_risk_high->index_4h` score `0.1378` n `31` status `ready` deltaP `-0.3688` edge `0.052` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1376` n `31` status `ready` deltaP `4.8928` edge `0.0353` maxDD `-0.356`
- `market_context_high->fx_4h` score `-0.0646` n `46` status `ready` deltaP `12.9573` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0828` n `31` status `ready` deltaP `2.2938` edge `-0.0061` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.0863` n `31` status `ready` deltaP `10.3921` edge `-0.0163` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2941` n `31` status `ready` deltaP `-1.3135` edge `0.0022` maxDD `-0.1588`
- `market_context_high->fx_24h` score `-0.5859` n `39` status `ready` deltaP `1.1084` edge `0.0402` maxDD `-2.3798`
- `market_context_high->crypto_alt_1h` score `-0.5981` n `52` status `ready` deltaP `-0.8982` edge `-0.0038` maxDD `-3.0178`
- `news_risk_high->metal_1h` score `-0.602` n `31` status `ready` deltaP `-2.5111` edge `-0.0015` maxDD `-0.5538`
- `news_risk_high->metal_4h` score `-0.9137` n `31` status `ready` deltaP `-4.0765` edge `-0.0144` maxDD `-0.7654`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
