# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T22:52:25.917906+00:00`
- Price records: `672`
- Market context records: `5500`
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

- `market_context_high->crypto_major_24h` score `3.1608` n `190` status `ready` deltaP `16.2189` edge `0.6093` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.6173` n `193` status `ready` deltaP `14.7984` edge `0.3487` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.6162` n `193` status `ready` deltaP `12.297` edge `0.2999` maxDD `-7.4425`
- `market_context_high->equity_24h` score `2.2917` n `190` status `ready` deltaP `10.7511` edge `0.6272` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `2.1787` n `193` status `ready` deltaP `10.8658` edge `0.2732` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5867` n `193` status `ready` deltaP `9.0325` edge `0.0852` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3416` n `190` status `ready` deltaP `12.584` edge `0.0373` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1835` n `193` status `ready` deltaP `6.9948` edge `0.018` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2496` n `193` status `ready` deltaP `1.4334` edge `0.0658` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.3324` n `193` status `ready` deltaP `3.3221` edge `0.0747` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3626` n `193` status `ready` deltaP `0.3281` edge `0.0002` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.496` n `193` status `ready` deltaP `1.9632` edge `0.0131` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7921` n `193` status `ready` deltaP `3.8236` edge `0.0066` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.8096` n `193` status `ready` deltaP `7.2089` edge `0.0454` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5231` n `193` status `ready` deltaP `-3.4253` edge `-0.0093` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7889` n `190` status `ready` deltaP `14.2708` edge `0.0742` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8175` n `193` status `ready` deltaP `-10.1036` edge `-0.0414` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4606` n `193` status `ready` deltaP `-8.0287` edge `-0.0509` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1294` n `190` status `ready` deltaP `7.2442` edge `0.2273` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2697` n `190` status `ready` deltaP `-4.2379` edge `-0.166` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
