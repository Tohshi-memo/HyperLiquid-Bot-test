# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T16:22:30.314234+00:00`
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

- `market_context_high->crypto_alt_24h` score `11.9982` n `39` status `ready` deltaP `51.8563` edge `0.6715` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.4053` n `39` status `ready` deltaP `53.6458` edge `0.5928` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.022` n `31` status `ready` deltaP `-7.2777` edge `0.2021` maxDD `-2.8064`
- `news_risk_high->fx_24h` score `0.9485` n `31` status `ready` deltaP `12.192` edge `0.063` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9396` n `31` status `ready` deltaP `19.8377` edge `0.0094` maxDD `-0.6947`
- `market_context_high->commodity_1h` score `0.3716` n `50` status `ready` deltaP `8.0958` edge `0.0311` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.3421` n `50` status `ready` deltaP `10.4491` edge `-0.0064` maxDD `-0.7804`
- `market_context_high->commodity_4h` score `0.3323` n `46` status `ready` deltaP `5.0305` edge `0.0937` maxDD `-2.7703`
- `news_risk_high->commodity_4h` score `0.2343` n `31` status `ready` deltaP `13.095` edge `-0.0177` maxDD `-1.6728`
- `news_risk_high->index_4h` score `0.1414` n `31` status `ready` deltaP `-0.3688` edge `0.0523` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1376` n `31` status `ready` deltaP `4.8928` edge `0.0353` maxDD `-0.356`
- `market_context_high->fx_4h` score `-0.0646` n `46` status `ready` deltaP `12.9573` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0649` n `31` status `ready` deltaP `2.5932` edge `-0.0058` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.0925` n `31` status `ready` deltaP `10.3921` edge `-0.0171` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2848` n `31` status `ready` deltaP `-1.1638` edge `0.0024` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.572` n `31` status `ready` deltaP `-2.2117` edge `-0.001` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.5883` n `39` status `ready` deltaP `1.1084` edge `0.04` maxDD `-2.3798`
- `news_risk_high->metal_4h` score `-0.8845` n `31` status `ready` deltaP `-3.7716` edge `-0.014` maxDD `-0.7654`
- `news_risk_high->crypto_major_1h` score `-0.9429` n `31` status `ready` deltaP `2.062` edge `-0.0626` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-1.1389` n `50` status `ready` deltaP `-2.8982` edge `-0.0087` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
