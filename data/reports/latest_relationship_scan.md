# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T05:22:25.550471+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `6150.0359` n `61` status `ready` deltaP `1.9296` edge `512.4976` maxDD `-0.2646`
- `market_context_high->unknown_4h` score `313.493` n `61` status `ready` deltaP `5.5253` edge `26.0919` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `81.652` n `108` status `ready` deltaP `-5.1951` edge `6.8676` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `23.8319` n `61` status `ready` deltaP `3.4873` edge `1.9738` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0696` n `61` status `ready` deltaP `38.0038` edge `1.3898` maxDD `-2.3221`
- `news_risk_high->crypto_alt_24h` score `13.4534` n `98` status `ready` deltaP `31.8949` edge `1.0441` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5229` n `61` status `ready` deltaP `55.3251` edge `0.1884` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.1617` n `108` status `ready` deltaP `19.5122` edge `0.4387` maxDD `-7.4246`
- `market_context_high->commodity_24h` score `3.1479` n `61` status `ready` deltaP `38.6042` edge `0.2145` maxDD `-3.463`
- `market_context_high->crypto_major_4h` score `3.0054` n `61` status `ready` deltaP `23.1232` edge `0.1879` maxDD `-4.9952`
- `market_context_high->crypto_alt_4h` score `2.9005` n `61` status `ready` deltaP `16.6433` edge `0.2388` maxDD `-6.3107`
- `market_context_high->commodity_4h` score `2.8745` n `61` status `ready` deltaP `27.6964` edge `0.0883` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `1.8246` n `61` status `ready` deltaP `6.8562` edge `0.2609` maxDD `-3.4817`
- `market_context_high->equity_4h` score `1.5887` n `61` status `ready` deltaP `1.3919` edge `0.2646` maxDD `-2.283`
- `market_context_high->metal_4h` score `1.4092` n `61` status `ready` deltaP `16.9832` edge `0.0467` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.3933` n `61` status `ready` deltaP `-7.9178` edge `0.3832` maxDD `-8.8096`
- `news_risk_high->crypto_alt_1h` score `0.7737` n `108` status `ready` deltaP `8.4276` edge `0.1037` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7572` n `61` status `ready` deltaP `9.7722` edge `0.0228` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.6031` n `61` status `ready` deltaP `14.3762` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.3901` n `61` status `ready` deltaP `-2.3093` edge `0.1352` maxDD `-1.9167`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
