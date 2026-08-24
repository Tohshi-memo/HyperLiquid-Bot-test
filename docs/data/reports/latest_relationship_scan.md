# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T23:22:25.513397+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.9028` n `51` status `ready` deltaP `9.375` edge `3.6794` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9483` n `51` status `ready` deltaP `24.2587` edge `0.9219` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.4063` n `51` status `ready` deltaP `40.237` edge `0.8587` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2684` n `51` status `ready` deltaP `48.9481` edge `0.1279` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.9066` n `51` status `ready` deltaP `27.6901` edge `0.218` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5538` n `51` status `ready` deltaP `16.3349` edge `0.2177` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.331` n `51` status `ready` deltaP `39.3024` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7438` n `130` status `ready` deltaP `19.2964` edge `0.0575` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2937` n `51` status `ready` deltaP `17.5942` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.02` n `51` status `ready` deltaP `18.7918` edge `0.0419` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9655` n `51` status `ready` deltaP `14.1589` edge `0.0258` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `0.81` n `111` status `ready` deltaP `4.8705` edge `0.0643` maxDD `-0.6752`
- `news_risk_high->commodity_1h` score `0.2998` n `51` status `ready` deltaP `9.2873` edge `-0.0061` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1835` n `51` status `ready` deltaP `8.075` edge `0.005` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1657` n `130` status `ready` deltaP `11.3251` edge `-0.0158` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0109` n `130` status `ready` deltaP `10.9051` edge `-0.0269` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `-0.0363` n `51` status `ready` deltaP `23.3864` edge `-0.1547` maxDD `-0.0053`
- `news_risk_high->metal_1h` score `-0.1722` n `51` status `ready` deltaP `1.1448` edge `-0.0074` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2603` n `51` status `ready` deltaP `6.4533` edge `-0.0116` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3999` n `130` status `ready` deltaP `3.1598` edge `0.0009` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
