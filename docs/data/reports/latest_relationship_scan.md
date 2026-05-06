# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T20:37:23.600280+00:00`
- Price records: `486`
- Market context records: `578`
- Flow alert records: `1634`
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

- `market_context_high->crypto_alt_24h` score `4.7307` n `146` status `ready` deltaP `7.2638` edge `0.3506` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9671` n `146` status `ready` deltaP `9.4731` edge `0.2175` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0511` n `146` status `ready` deltaP `11.0089` edge `0.0203` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2888` n `146` status `ready` deltaP `2.456` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5598` n `146` status `ready` deltaP `1.9201` edge `0.038` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7076` n `146` status `ready` deltaP `-0.129` edge `-0.0045` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.169` n `146` status `ready` deltaP `-4.2119` edge `-0.009` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3006` n `146` status `ready` deltaP `4.6326` edge `-0.0078` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3408` n `146` status `ready` deltaP `-2.4302` edge `-0.0145` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.9548` n `146` status `ready` deltaP `3.7799` edge `-0.0158` maxDD `-11.4508`
- `market_context_high->index_24h` score `-1.9895` n `146` status `ready` deltaP `-5.8024` edge `0.0724` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.184` n `146` status `ready` deltaP `2.9816` edge `0.0551` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2211` n `146` status `ready` deltaP `0.4762` edge `-0.036` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-3.0096` n `146` status `ready` deltaP `11.2795` edge `0.0446` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.3175` n `146` status `ready` deltaP `-4.7292` edge `-0.049` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3358` n `146` status `ready` deltaP `-3.3864` edge `-0.0402` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.5493` n `146` status `ready` deltaP `-5.6676` edge `0.0921` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.9134` n `146` status `ready` deltaP `-9.8907` edge `0.0003` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5617` n `146` status `ready` deltaP `-4.9117` edge `-0.0349` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.107` n `146` status `ready` deltaP `1.1454` edge `-0.2454` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
