# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T16:37:39.460787+00:00`
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

- `market_context_high->crypto_alt_24h` score `11.9519` n `39` status `ready` deltaP `51.6827` edge `0.6688` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.3777` n `39` status `ready` deltaP `53.6458` edge `0.5905` maxDD `0.0`
- `news_risk_high->equity_4h` score `0.9932` n `31` status `ready` deltaP `-7.2777` edge `0.1997` maxDD `-2.8064`
- `news_risk_high->fx_24h` score `0.9497` n `31` status `ready` deltaP `12.192` edge `0.0631` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.928` n `31` status `ready` deltaP `19.688` edge `0.0089` maxDD `-0.6947`
- `market_context_high->commodity_1h` score `0.4086` n `51` status `ready` deltaP `8.8088` edge `0.0311` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4` n `51` status `ready` deltaP `11.0837` edge `-0.0058` maxDD `-0.7804`
- `market_context_high->commodity_4h` score `0.319` n `46` status `ready` deltaP `4.878` edge `0.093` maxDD `-2.7703`
- `news_risk_high->commodity_4h` score `0.2137` n `31` status `ready` deltaP `12.9425` edge `-0.0184` maxDD `-1.6728`
- `news_risk_high->index_4h` score `0.1402` n `31` status `ready` deltaP `-0.3688` edge `0.0522` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1376` n `31` status `ready` deltaP `4.8928` edge `0.0353` maxDD `-0.356`
- `market_context_high->fx_4h` score `-0.0646` n `46` status `ready` deltaP `12.9573` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0734` n `31` status `ready` deltaP `2.4435` edge `-0.0059` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.0863` n `31` status `ready` deltaP `10.3921` edge `-0.0163` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2933` n `31` status `ready` deltaP `-1.3135` edge `0.0023` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5864` n `31` status `ready` deltaP `-2.3614` edge `-0.0012` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.5871` n `39` status `ready` deltaP `1.1084` edge `0.0401` maxDD `-2.3798`
- `news_risk_high->metal_4h` score `-0.8991` n `31` status `ready` deltaP `-3.9241` edge `-0.0142` maxDD `-0.7654`
- `news_risk_high->crypto_major_1h` score `-0.9358` n `31` status `ready` deltaP `2.062` edge `-0.0617` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-1.0274` n `51` status `ready` deltaP `-1.8786` edge `-0.0062` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
