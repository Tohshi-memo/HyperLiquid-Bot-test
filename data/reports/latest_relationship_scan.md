# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T22:22:31.171950+00:00`
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

- `market_context_high->unknown_24h` score `41.6772` n `42` status `ready` deltaP `26.9593` edge `3.2977` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `13.5789` n `62` status `ready` deltaP `10.0806` edge `1.1116` maxDD `-1.4448`
- `market_context_high->crypto_alt_24h` score `10.6314` n `42` status `ready` deltaP `48.5863` edge `0.5794` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.8374` n `42` status `ready` deltaP `48.1895` edge `0.5106` maxDD `-0.2995`
- `market_context_high->commodity_4h` score `1.036` n `62` status `ready` deltaP `13.1196` edge `0.0835` maxDD `-2.7703`
- `news_risk_high->fx_24h` score `1.0205` n `31` status `ready` deltaP `12.192` edge `0.069` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8875` n `31` status `ready` deltaP `19.0892` edge `0.0077` maxDD `-0.6947`
- `market_context_high->fx_1h` score `0.4625` n `74` status `ready` deltaP `11.264` edge `-0.0017` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.3837` n `62` status `ready` deltaP `17.1863` edge `0.0034` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.3158` n `74` status `ready` deltaP `6.7527` edge `0.0229` maxDD `-1.3282`
- `news_risk_high->equity_4h` score `0.1723` n `31` status `ready` deltaP `-9.2594` edge `0.1445` maxDD `-2.8064`
- `news_risk_high->fx_4h` score `0.109` n `31` status `ready` deltaP `4.2831` edge `0.0357` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.1058` n `31` status `ready` deltaP `9.8938` edge `-0.0247` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1077` n `31` status `ready` deltaP `1.8447` edge `-0.0063` maxDD `-0.5845`
- `news_risk_high->index_4h` score `-0.1144` n `31` status `ready` deltaP `-2.3505` edge `0.0442` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `-0.1814` n `31` status `ready` deltaP `9.7933` edge `-0.0245` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.2811` n `62` status `ready` deltaP `6.604` edge `0.0105` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.358` n `31` status `ready` deltaP `-2.5111` edge `0.002` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.3832` n `74` status `ready` deltaP `2.4114` edge `-0.0118` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.4208` n `74` status `ready` deltaP `1.2057` edge `0.0049` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
