# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T14:22:30.157914+00:00`
- Price records: `672`
- Market context records: `5152`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.342` n `63` status `ready` deltaP `34.7966` edge `2.3155` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.5809` n `129` status `ready` deltaP `19.654` edge `0.5196` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.6719` n `140` status `ready` deltaP `10.231` edge `0.4686` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.3807` n `129` status `ready` deltaP `16.7411` edge `0.4967` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `5.0771` n `63` status `ready` deltaP `19.8909` edge `0.857` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.9153` n `63` status `ready` deltaP `18.0803` edge `0.8758` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `4.3505` n `129` status `ready` deltaP `15.3431` edge `0.4895` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0021` n `63` status `ready` deltaP `20.2381` edge `0.1552` maxDD `-5.1955`
- `market_context_high->equity_4h` score `1.1588` n `129` status `ready` deltaP `11.2403` edge `0.1855` maxDD `-7.4425`
- `market_context_high->metal_24h` score `0.9964` n `63` status `ready` deltaP `0.9424` edge `0.2523` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.8923` n `140` status `ready` deltaP `8.2806` edge `0.1437` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.8598` n `140` status `ready` deltaP `5.8511` edge `0.1288` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.2642` n `140` status `ready` deltaP `7.0958` edge `0.0574` maxDD `-3.6667`
- `market_context_high->metal_1h` score `-0.0141` n `140` status `ready` deltaP `5.7699` edge `0.0163` maxDD `-1.8593`
- `market_context_high->index_1h` score `-0.1038` n `140` status `ready` deltaP `3.7896` edge `0.0118` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2469` n `140` status `ready` deltaP `1.9932` edge `0.0003` maxDD `-0.6194`
- `market_context_high->fx_24h` score `-0.3445` n `63` status `ready` deltaP `7.5645` edge `0.0104` maxDD `-0.8294`
- `market_context_high->index_4h` score `-0.4314` n `129` status `ready` deltaP `6.1933` edge `0.0345` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6198` n `129` status `ready` deltaP `2.7652` edge `0.0055` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6235` n `140` status `ready` deltaP `0.1839` edge `-0.0003` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
