# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T12:37:24.875732+00:00`
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

- `news_risk_high->unknown_24h` score `48.0289` n `51` status `ready` deltaP `16.6667` edge `3.8913` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.8079` n `51` status `ready` deltaP `40.237` edge `0.9755` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0837` n `51` status `ready` deltaP `24.1063` edge `0.9342` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5936` n `51` status `ready` deltaP `48.9481` edge `0.155` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7396` n `51` status `ready` deltaP `26.623` edge `0.2112` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6953` n `51` status `ready` deltaP `16.9337` edge `0.2255` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2748` n `51` status `ready` deltaP `38.5402` edge `0.0294` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `1.7198` n `80` status `ready` deltaP `4.1667` edge `0.1658` maxDD `-1.0208`
- `market_context_high->unknown_4h` score `1.6961` n `136` status `ready` deltaP `19.4495` edge `0.0525` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.2695` n `51` status `ready` deltaP `30.6781` edge `-0.0945` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->index_4h` score `0.9909` n `51` status `ready` deltaP `14.3113` edge `0.0269` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9226` n `51` status `ready` deltaP `18.0433` edge `0.0344` maxDD `-0.9128`
- `market_context_high->metal_4h` score `0.2901` n `136` status `ready` deltaP `12.0247` edge `-0.0101` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2177` n `51` status `ready` deltaP `8.8235` edge `0.0044` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1488` n `51` status `ready` deltaP `8.0897` edge `-0.0107` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0094` n `136` status `ready` deltaP `11.0514` edge `-0.028` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1372` n `51` status `ready` deltaP `1.8933` edge `-0.0079` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1511` n `51` status `ready` deltaP `7.3679` edge `-0.0086` maxDD `-0.249`
- `market_context_high->fx_24h` score `-0.3411` n `80` status `ready` deltaP `12.3958` edge `-0.0047` maxDD `-3.1759`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
