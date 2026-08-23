# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T07:22:24.168680+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `news_risk_high->unknown_4h` score `14.7548` n `51` status `ready` deltaP `26.5453` edge `1.0572` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `5.0444` n `33` status `ready` deltaP `-7.5802` edge `0.7421` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `5.0444` n `33` status `ready` deltaP `-7.5802` edge `0.7421` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.7983` n `51` status `ready` deltaP `20.2272` edge `0.2121` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.955` n `51` status `ready` deltaP `25.0986` edge `0.1562` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.8586` n `51` status `ready` deltaP `33.967` edge `0.0252` maxDD `-0.0746`
- `news_risk_high->fx_1h` score `1.2182` n `51` status `ready` deltaP `16.8457` edge `0.0062` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1333` n `135` status `ready` deltaP `6.7632` edge `0.0942` maxDD `-1.5876`
- `news_risk_high->equity_1h` score `0.8578` n `51` status `ready` deltaP `18.4924` edge `0.0232` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7525` n `123` status `ready` deltaP `22.002` edge `-0.0668` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.7044` n `51` status `ready` deltaP `11.7198` edge `0.0203` maxDD `-0.1788`
- `market_context_high->commodity_24h` score `0.4965` n `107` status `ready` deltaP `0.834` edge `0.1046` maxDD `-1.8362`
- `news_risk_high->index_1h` score `0.2558` n `51` status `ready` deltaP `9.7217` edge `0.0033` maxDD `-0.1583`
- `risk_on_high->fx_1h` score `0.2441` n `33` status `ready` deltaP `6.8636` edge `0.0032` maxDD `-0.0796`
- `risk_on_and_context->fx_1h` score `0.2441` n `33` status `ready` deltaP `6.8636` edge `0.0032` maxDD `-0.0796`
- `news_risk_high->commodity_1h` score `0.1476` n `51` status `ready` deltaP `8.0897` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1055` n `123` status `ready` deltaP `7.5203` edge `0.0089` maxDD `-0.3527`
- `news_risk_high->metal_4h` score `0.0382` n `51` status `ready` deltaP `9.9594` edge `-0.0101` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.0921` n `51` status `ready` deltaP `2.6418` edge `-0.0071` maxDD `-0.1184`
- `risk_on_high->index_1h` score `-0.1145` n `33` status `ready` deltaP `-0.617` edge `0.0076` maxDD `-0.1197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
