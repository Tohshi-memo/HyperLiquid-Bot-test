# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T22:07:27.636994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `market_context_high->unknown_24h` score `41.6585` n `42` status `ready` deltaP `26.7857` edge `3.2973` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `13.8106` n `61` status `ready` deltaP `9.6311` edge `1.1339` maxDD `-1.4448`
- `market_context_high->crypto_alt_24h` score `10.6638` n `42` status `ready` deltaP `48.5863` edge `0.5821` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.8621` n `42` status `ready` deltaP `48.3631` edge `0.5115` maxDD `-0.2995`
- `news_risk_high->fx_24h` score `1.0169` n `31` status `ready` deltaP `12.192` edge `0.0687` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `1.0142` n `61` status `ready` deltaP `12.6374` edge `0.0849` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.8789` n `31` status `ready` deltaP `18.9395` edge `0.0076` maxDD `-0.6947`
- `market_context_high->fx_1h` score `0.4295` n `73` status `ready` deltaP `10.8953` edge `-0.002` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.3753` n `73` status `ready` deltaP `7.362` edge `0.0238` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.3101` n `61` status `ready` deltaP `16.446` edge `0.0022` maxDD `-1.8797`
- `news_risk_high->equity_4h` score `0.2229` n `31` status `ready` deltaP `-9.107` edge `0.1477` maxDD `-2.8064`
- `news_risk_high->fx_4h` score `0.109` n `31` status `ready` deltaP `4.2831` edge `0.0357` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.0912` n `31` status `ready` deltaP `10.0462` edge `-0.0245` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.0938` n `31` status `ready` deltaP `-2.1981` edge `0.0449` maxDD `-0.3783`
- `news_risk_high->index_1h` score `-0.0991` n `31` status `ready` deltaP `1.9944` edge `-0.0062` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.165` n `31` status `ready` deltaP `9.7933` edge `-0.0224` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.1737` n `61` status `ready` deltaP `7.5294` edge `0.0181` maxDD `-4.9116`
- `market_context_high->crypto_alt_1h` score `-0.3443` n `73` status `ready` deltaP `1.9277` edge `0.0099` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.3494` n `31` status `ready` deltaP `-2.3614` edge `0.0021` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4126` n `73` status `ready` deltaP `1.9502` edge `-0.0125` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
