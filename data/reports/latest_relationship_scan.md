# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T15:06:29.402373+00:00`
- Price records: `672`
- Market context records: `8525`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6279.9009` n `52` status `ready` deltaP `44.7383` edge `523.0689` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6192` n `64` status `ready` deltaP `21.2652` edge `0.3862` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0399` n `64` status `ready` deltaP `16.8064` edge `0.077` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7038` n `64` status `ready` deltaP `15.8028` edge `0.0843` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8785` n `64` status `ready` deltaP `5.9832` edge `0.1503` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8174` n `64` status `ready` deltaP `14.7866` edge `0.1454` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5014` n `64` status `ready` deltaP `8.8604` edge `0.0579` maxDD `-1.8813`
- `market_context_high->crypto_alt_4h` score `0.3933` n `41` status `ready` deltaP `5.9451` edge `0.0981` maxDD `-4.9853`
- `news_risk_high->crypto_major_1h` score `0.3064` n `64` status `ready` deltaP `6.3155` edge `0.0484` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1142` n `64` status `ready` deltaP `5.7354` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0675` n `64` status `ready` deltaP `2.9345` edge `0.0367` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0519` n `64` status `ready` deltaP `4.3694` edge `0.0092` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.029` n `64` status `ready` deltaP `11.471` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0868` n `64` status `ready` deltaP `3.7051` edge `0.0084` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.153` n `53` status `ready` deltaP `5.2254` edge `0.0081` maxDD `-2.0038`
- `market_context_high->commodity_4h` score `-0.3379` n `41` status `ready` deltaP `8.8415` edge `0.0492` maxDD `-5.4508`
- `market_context_high->crypto_major_4h` score `-0.3421` n `41` status `ready` deltaP `1.8292` edge `0.0547` maxDD `-5.8606`
- `market_context_high->fx_4h` score `-0.5629` n `41` status `ready` deltaP `1.3719` edge `-0.0001` maxDD `-0.8095`
- `market_context_high->metal_1h` score `-0.5945` n `53` status `ready` deltaP `-1.6015` edge `-0.0161` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8724` n `53` status `ready` deltaP `-7.4427` edge `0.0005` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
