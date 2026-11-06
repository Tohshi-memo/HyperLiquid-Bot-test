# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T20:37:25.384160+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4184`

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

- `news_risk_high->equity_4h` score `1.6468` n `88` status `ready` deltaP `14.3986` edge `0.2057` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7935` n `88` status `ready` deltaP `14.0105` edge `0.0205` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.2655` n `88` status `ready` deltaP `4.6339` edge `0.0581` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.2469` n `88` status `ready` deltaP `10.8873` edge `0.0044` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.158` n `88` status `ready` deltaP `3.5892` edge `0.0004` maxDD `-0.2336`
- `news_risk_high->fx_1h` score `-0.335` n `88` status `ready` deltaP `-0.4831` edge `0.0001` maxDD `-0.1858`
- `news_risk_high->metal_1h` score `-0.359` n `88` status `ready` deltaP `-0.7485` edge `-0.0053` maxDD `-0.5256`
- `news_risk_high->crypto_major_4h` score `-0.5814` n `88` status `ready` deltaP `1.1502` edge `0.0864` maxDD `-9.1553`
- `news_risk_high->index_24h` score `-0.6607` n `88` status `ready` deltaP `-1.6464` edge `0.1394` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.6717` n `88` status `ready` deltaP `2.0958` edge `0.0227` maxDD `-5.8225`
- `news_risk_high->fx_24h` score `-0.7792` n `88` status `ready` deltaP `-6.6113` edge `0.0234` maxDD `-0.2073`
- `news_risk_high->crypto_major_1h` score `-0.8517` n `88` status `ready` deltaP `-2.9872` edge `0.0046` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-1.0348` n `88` status `ready` deltaP `-1.2472` edge `-0.0338` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.1908` n `88` status `ready` deltaP `26.8001` edge `0.8273` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-1.5905` n `88` status `ready` deltaP `-2.4251` edge `0.0759` maxDD `-14.0916`
- `news_risk_high->metal_24h` score `-2.9651` n `88` status `ready` deltaP `3.7301` edge `-0.2154` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-2.9756` n `88` status `ready` deltaP `-17.794` edge `-0.0084` maxDD `-2.0082`
- `news_risk_high->commodity_4h` score `-4.1578` n `88` status `ready` deltaP `-26.4274` edge `-0.0029` maxDD `-4.7251`
- `news_risk_high->crypto_major_24h` score `-7.02` n `88` status `ready` deltaP `-19.2709` edge `0.0788` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.2851` n `88` status `ready` deltaP `-25.6677` edge `-0.0171` maxDD `-29.5096`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
