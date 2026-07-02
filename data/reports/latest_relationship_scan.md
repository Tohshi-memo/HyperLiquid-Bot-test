# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T23:07:26.030715+00:00`
- Price records: `672`
- Market context records: `5501`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->crypto_major_24h` score `3.144` n `190` status `ready` deltaP `16.2189` edge `0.6079` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.5933` n `193` status `ready` deltaP `14.7984` edge `0.3467` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.5548` n `193` status `ready` deltaP `12.1446` edge `0.2958` maxDD `-7.4425`
- `market_context_high->equity_24h` score `2.3373` n `190` status `ready` deltaP `10.7511` edge `0.631` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `2.1317` n `193` status `ready` deltaP `10.7134` edge `0.2703` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.6023` n `193` status `ready` deltaP `9.1822` edge `0.0855` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.344` n `190` status `ready` deltaP `12.584` edge `0.0375` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1955` n `193` status `ready` deltaP `7.1445` edge `0.018` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2304` n `193` status `ready` deltaP `1.5831` edge `0.0664` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.312` n `193` status `ready` deltaP `3.4718` edge `0.0754` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3549` n `193` status `ready` deltaP `0.4778` edge `0.0002` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.5104` n `193` status `ready` deltaP `1.8135` edge `0.0129` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7799` n `193` status `ready` deltaP `3.976` edge `0.0066` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.8326` n `193` status `ready` deltaP `7.0564` edge `0.0445` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5231` n `193` status `ready` deltaP `-3.4253` edge `-0.0093` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.792` n `190` status `ready` deltaP `14.2708` edge `0.0738` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.834` n `193` status `ready` deltaP `-10.256` edge `-0.0425` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4763` n `193` status `ready` deltaP `-8.1811` edge `-0.0512` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1318` n `190` status `ready` deltaP `7.2442` edge `0.2271` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2728` n `190` status `ready` deltaP `-4.2379` edge `-0.1664` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
