# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T05:37:32.386414+00:00`
- Price records: `672`
- Market context records: `7955`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11845`

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

- `market_context_high->equity_24h` score `16.5251` n `82` status `ready` deltaP `25.6013` edge `1.3406` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2081` n `82` status `ready` deltaP `37.2617` edge `0.4356` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7345` n `91` status `ready` deltaP `24.8681` edge `0.4847` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.7085` n `82` status `ready` deltaP `27.7058` edge `0.2776` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.7881` n `91` status `ready` deltaP `24.9414` edge `0.1283` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6523` n `91` status `ready` deltaP `27.1516` edge `0.076` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7589` n `91` status `ready` deltaP `13.4294` edge `0.1388` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3428` n `82` status `ready` deltaP `27.5787` edge `0.0368` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.222` n `91` status `ready` deltaP `9.0676` edge `0.1531` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.2159` n `82` status `ready` deltaP `9.917` edge `0.1568` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.0508` n `91` status `ready` deltaP `10.9606` edge `0.1863` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9711` n `91` status `ready` deltaP `15.081` edge `0.0234` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6552` n `91` status `ready` deltaP `9.14` edge `0.0315` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5229` n `91` status `ready` deltaP `9.9905` edge `0.0413` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.1424` n `91` status `ready` deltaP `3.4958` edge `0.0382` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3715` n `91` status `ready` deltaP `1.5939` edge `-0.0014` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4153` n `91` status `ready` deltaP `0.1534` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.455` n `91` status `ready` deltaP `4.6879` edge `0.0056` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.4797` n `91` status `ready` deltaP `3.043` edge `0.0162` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.6274` n `91` status `ready` deltaP `10.0382` edge `-0.1602` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
