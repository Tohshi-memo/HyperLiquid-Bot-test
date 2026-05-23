# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T00:52:17.405566+00:00`
- Price records: `672`
- Market context records: `1580`
- Flow alert records: `6461`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.4466` n `182` status `ready` deltaP `27.8102` edge `1.0352` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7366` n `182` status `ready` deltaP `26.9974` edge `0.9997` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.1505` n `182` status `ready` deltaP `26.7399` edge `0.7808` maxDD `-8.0553`
- `market_context_high->equity_24h` score `4.1849` n `182` status `ready` deltaP `18.4085` edge `0.4587` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.0785` n `182` status `ready` deltaP `21.3008` edge `0.3065` maxDD `-5.3574`
- `market_context_high->equity_4h` score `0.922` n `199` status `ready` deltaP `8.2922` edge `0.131` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2426` n `199` status `ready` deltaP `13.2545` edge `0.2747` maxDD `-19.5565`
- `market_context_high->fx_24h` score `0.152` n `182` status `ready` deltaP `11.3209` edge `0.0421` maxDD `-1.3925`
- `market_context_high->crypto_major_4h` score `0.0575` n `199` status `ready` deltaP `9.2796` edge `0.2164` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.27` n `199` status `ready` deltaP `1.2668` edge `0.0593` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5611` n `199` status `ready` deltaP `0.7636` edge `0.029` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.5943` n `199` status `ready` deltaP `1.5226` edge `0.0035` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6257` n `199` status `ready` deltaP `-1.9942` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6963` n `199` status `ready` deltaP `5.7466` edge `0.006` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7796` n `199` status `ready` deltaP `-0.9463` edge `-0.0015` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8233` n `199` status `ready` deltaP `0.0053` edge `0.0301` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.1686` n `199` status `ready` deltaP `-2.4582` edge `0.0279` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3006` n `199` status `ready` deltaP `10.516` edge `0.0907` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.387` n `199` status `ready` deltaP `-10.5497` edge `-0.0146` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2206` n `199` status `ready` deltaP `-14.7001` edge `-0.1086` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
