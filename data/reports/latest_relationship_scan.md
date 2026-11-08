# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T11:37:26.364075+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4735`

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

- `market_context_high->unknown_4h` score `91.9062` n `37` status `ready` deltaP `-4.2436` edge `7.7319` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.0261` n `37` status `ready` deltaP `15.4139` edge `0.8289` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3086` n `38` status `ready` deltaP `11.4245` edge `0.2455` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1205` n `37` status `ready` deltaP `33.619` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.6013` n `37` status `ready` deltaP `30.9163` edge `0.0192` maxDD `-0.016`
- `market_context_high->index_4h` score `2.0694` n `37` status `ready` deltaP `26.9652` edge `0.0397` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.0289` n `38` status `ready` deltaP `13.4336` edge `0.0777` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.0001` n `38` status `ready` deltaP `11.1881` edge `0.0673` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8412` n `37` status `ready` deltaP `10.6982` edge `0.0996` maxDD `-2.7123`
- `market_context_high->commodity_24h` score `0.7876` n `37` status `ready` deltaP `7.6014` edge `0.1698` maxDD `-6.5601`
- `market_context_high->fx_24h` score `0.665` n `37` status `ready` deltaP `10.9422` edge `-0.0087` maxDD `-0.0397`
- `news_risk_high->fx_1h` score `0.6625` n `37` status `ready` deltaP `14.2823` edge `0.0071` maxDD `-0.0567`
- `news_risk_high->fx_24h` score `0.5015` n `34` status `ready` deltaP `0.4493` edge `0.0609` maxDD `-0.1014`
- `market_context_high->fx_1h` score `0.4248` n `38` status `ready` deltaP `7.1699` edge `0.0147` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.4045` n `38` status `ready` deltaP `3.3801` edge `0.0382` maxDD `-0.1621`
- `news_risk_high->equity_4h` score `0.078` n `37` status `ready` deltaP `-1.92` edge `0.0932` maxDD `-4.2454`
- `market_context_high->metal_1h` score `0.0153` n `38` status `ready` deltaP `2.7813` edge `0.0162` maxDD `-0.6226`
- `market_context_high->commodity_1h` score `0.0134` n `38` status `ready` deltaP `7.0832` edge `0.0091` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0607` n `37` status `ready` deltaP `2.2248` edge `0.0228` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0882` n `37` status `ready` deltaP `4.8026` edge `0.002` maxDD `-0.2931`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
