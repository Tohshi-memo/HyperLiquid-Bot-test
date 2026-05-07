# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T07:52:23.364726+00:00`
- Price records: `531`
- Market context records: `627`
- Flow alert records: `1774`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `5.4108` n `146` status `ready` deltaP `15.6888` edge `0.3797` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2317` n `146` status `ready` deltaP `7.3611` edge `0.3917` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.07` n `146` status `ready` deltaP `9.2955` edge `0.0162` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2987` n `146` status `ready` deltaP `2.356` edge `0.0038` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4841` n `146` status `ready` deltaP `2.0561` edge `0.0434` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7362` n `146` status `ready` deltaP `-0.8002` edge `-0.0037` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1169` n `146` status `ready` deltaP `-3.8158` edge `-0.0073` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2608` n `146` status `ready` deltaP `5.3703` edge `-0.0094` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3679` n `146` status `ready` deltaP `-2.9034` edge `-0.0136` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7904` n `146` status `ready` deltaP `5.1298` edge `-0.0111` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.883` n `146` status `ready` deltaP `4.5392` edge `0.0698` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3646` n `146` status `ready` deltaP `-1.272` edge `-0.0363` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4024` n `146` status `ready` deltaP `13.8595` edge `0.078` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9436` n `146` status `ready` deltaP `-8.1286` edge `0.0084` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.3737` n `146` status `ready` deltaP `-3.816` edge `-0.0405` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4291` n `146` status `ready` deltaP `-5.1351` edge `-0.0556` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5873` n `146` status `ready` deltaP `-6.0665` edge `0.0916` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2504` n `146` status `ready` deltaP `-2.0914` edge `-0.0138` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7114` n `146` status `ready` deltaP `2.1452` edge `-0.2191` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.9199` n `146` status `ready` deltaP `-11.4324` edge `-0.0733` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
