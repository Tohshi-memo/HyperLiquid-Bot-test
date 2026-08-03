# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T20:52:42.267911+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5931`

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

- `market_context_high->unknown_24h` score `44.3272` n `40` status `ready` deltaP `28.8194` edge `3.5018` maxDD `0.0`
- `market_context_high->unknown_4h` score `15.4118` n `56` status `ready` deltaP `12.0427` edge `1.2485` maxDD `-1.2244`
- `market_context_high->crypto_alt_24h` score `10.9572` n `40` status `ready` deltaP `48.9236` edge `0.6043` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `10.5588` n `40` status `ready` deltaP `50.9722` edge `0.5461` maxDD `-0.1479`
- `news_risk_high->fx_24h` score `0.9941` n `31` status `ready` deltaP `12.192` edge `0.0668` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.896` n `31` status `ready` deltaP `19.2389` edge `0.0078` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.83` n `56` status `ready` deltaP `9.7344` edge `0.0889` maxDD `-2.7703`
- `news_risk_high->equity_4h` score `0.4687` n `31` status `ready` deltaP `-8.3448` edge `0.1631` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.2675` n `68` status `ready` deltaP `5.9088` edge `0.0245` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2242` n `68` status `ready` deltaP `8.5241` edge `-0.0033` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.1059` n `31` status `ready` deltaP `4.2831` edge `0.0353` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.0008` n `31` status `ready` deltaP `-1.4359` edge `0.0477` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.0328` n `31` status `ready` deltaP `10.656` edge `-0.0237` maxDD `-1.6728`
- `market_context_high->fx_4h` score `-0.0645` n `56` status `ready` deltaP `12.3476` edge `-0.0017` maxDD `-1.8797`
- `news_risk_high->index_1h` score `-0.0898` n `31` status `ready` deltaP `2.1441` edge `-0.006` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1042` n `31` status `ready` deltaP `10.2424` edge `-0.0176` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.1877` n `56` status `ready` deltaP `6.1193` edge `0.0257` maxDD `-4.9116`
- `market_context_high->crypto_alt_1h` score `-0.3203` n `68` status `ready` deltaP `1.8933` edge `0.0132` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.3253` n `31` status `ready` deltaP `-1.9123` edge `0.0022` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.3561` n `68` status `ready` deltaP `3.1878` edge `-0.0135` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
