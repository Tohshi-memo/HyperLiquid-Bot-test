# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T13:22:27.480836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4099`

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

- `market_context_high->equity_1h` score `3.0927` n `37` status `ready` deltaP `8.711` edge `0.2456` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2424` n `61` status `ready` deltaP `11.5329` edge `0.1563` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7567` n `37` status `ready` deltaP `9.7508` edge `0.0566` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.7155` n `61` status `ready` deltaP `12.9448` edge `0.0211` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.4817` n `37` status `ready` deltaP `7.8209` edge `0.0151` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3953` n `37` status `ready` deltaP `10.649` edge `0.0612` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.3795` n `61` status `ready` deltaP `10.6159` edge `0.1447` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.3105` n `37` status `ready` deltaP `2.0999` edge `0.0389` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1872` n `37` status `ready` deltaP `10.2161` edge `0.0105` maxDD `-1.7019`
- `news_risk_high->fx_24h` score `0.1835` n `61` status `ready` deltaP `-2.1544` edge `0.0693` maxDD `-0.1715`
- `news_risk_high->index_1h` score `0.0962` n `61` status `ready` deltaP `8.1255` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0489` n `61` status `ready` deltaP `0.0712` edge `0.0482` maxDD `-1.396`
- `market_context_high->metal_1h` score `-0.091` n `37` status `ready` deltaP `0.7526` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.124` n `61` status `ready` deltaP `3.0357` edge `0.0024` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.191` n `61` status `ready` deltaP `2.3091` edge `0.0045` maxDD `-0.2175`
- `news_risk_high->metal_1h` score `-0.5776` n `61` status `ready` deltaP `-4.6972` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9251` n `61` status `ready` deltaP `1.9267` edge `-0.0409` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.0439` n `61` status `ready` deltaP `-0.2062` edge `-0.0169` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2103` n `61` status `ready` deltaP `-2.8414` edge `0.0242` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5657` n `61` status `ready` deltaP `-10.9625` edge `-0.0021` maxDD `-1.09`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
