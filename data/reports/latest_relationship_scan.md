# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T18:52:23.595687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10591`

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

- `risk_on_high->unknown_4h` score `19.8819` n `140` status `ready` deltaP `-2.1777` edge `1.8719` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `19.8819` n `140` status `ready` deltaP `-2.1777` edge `1.8719` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.0801` n `228` status `ready` deltaP `1.5191` edge `0.9002` maxDD `-8.9586`
- `news_risk_high->crypto_alt_24h` score `6.9563` n `37` status `ready` deltaP `25.1783` edge `0.4388` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8035` n `37` status `ready` deltaP `20.1389` edge `0.1827` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3782` n `37` status `ready` deltaP `16.8754` edge `0.2103` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3771` n `37` status `ready` deltaP `24.1513` edge `0.0592` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7511` n `37` status `ready` deltaP `9.752` edge `0.101` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5488` n `37` status `ready` deltaP `12.6356` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2586` n `37` status `ready` deltaP `15.0146` edge `0.0241` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1263` n `37` status `ready` deltaP `14.1245` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0779` n `37` status `ready` deltaP `5.717` edge `0.07` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.9345` n `37` status `ready` deltaP `9.0266` edge `0.0442` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.723` n `37` status `ready` deltaP `16.5776` edge `0.2598` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.7054` n `37` status `ready` deltaP `17.5253` edge `0.0435` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.5795` n `173` status `ready` deltaP `13.2245` edge `0.3947` maxDD `-20.7654`
- `news_risk_high->crypto_alt_4h` score `0.4761` n `37` status `ready` deltaP `5.3313` edge `0.037` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0234` n `146` status `ready` deltaP `7.5158` edge `-0.0024` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0234` n `146` status `ready` deltaP `7.5158` edge `-0.0024` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0254` n `37` status `ready` deltaP `5.7251` edge `0.0032` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
