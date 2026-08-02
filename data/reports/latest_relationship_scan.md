# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T08:07:25.384172+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.5439` n `60` status `ready` deltaP `31.4615` edge `432.211` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.1693` n `48` status `ready` deltaP `60.4709` edge `1.1507` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `5.2665` n `48` status `ready` deltaP `35.1495` edge `0.3309` maxDD `-7.1082`
- `news_risk_high->equity_4h` score `4.5337` n `68` status `ready` deltaP `16.5261` edge `0.344` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `1.0211` n `48` status `ready` deltaP `21.2399` edge `0.0231` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6348` n `68` status `ready` deltaP `9.7922` edge `0.0699` maxDD `-2.916`
- `market_context_high->commodity_4h` score `0.3806` n `48` status `ready` deltaP `8.0284` edge `0.0799` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.2744` n `48` status `ready` deltaP `4.8272` edge `0.0987` maxDD `-5.323`
- `news_risk_high->fx_4h` score `0.1284` n `68` status `ready` deltaP `12.2938` edge `0.0245` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1024` n `68` status `ready` deltaP `5.165` edge `0.0263` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0741` n `68` status `ready` deltaP `6.1818` edge `0.0365` maxDD `-3.1233`
- `market_context_high->fx_24h` score `0.0017` n `48` status `ready` deltaP `8.0264` edge `0.0447` maxDD `-2.506`
- `news_risk_high->fx_1h` score `-0.035` n `68` status `ready` deltaP `3.4167` edge `0.005` maxDD `-0.2475`
- `market_context_high->fx_1h` score `-0.0625` n `48` status `ready` deltaP `6.1128` edge `0.0015` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0949` n `68` status `ready` deltaP `2.0166` edge `0.0067` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.1105` n `48` status `ready` deltaP `2.0958` edge `0.0218` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.159` n `68` status `ready` deltaP `2.1663` edge `0.0055` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2693` n `68` status `ready` deltaP `1.6203` edge `0.0267` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6194` n `68` status `ready` deltaP `3.5664` edge `-0.0252` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
