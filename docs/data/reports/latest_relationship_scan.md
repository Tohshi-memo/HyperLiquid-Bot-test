# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T09:37:27.544960+00:00`
- Price records: `672`
- Market context records: `5758`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8666`

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

- `market_context_high->equity_24h` score `0.7676` n `226` status `ready` deltaP `15.181` edge `0.5051` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1459` n `285` status `ready` deltaP `7.3679` edge `0.1269` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1971` n `295` status `ready` deltaP `3.2599` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4327` n `295` status `ready` deltaP `1.9126` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6508` n `295` status `ready` deltaP `2.9641` edge `0.0267` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6585` n `295` status `ready` deltaP `-0.1918` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7743` n `295` status `ready` deltaP `-1.9436` edge `-0.0056` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.801` n `295` status `ready` deltaP `3.4096` edge `0.034` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.8778` n `295` status `ready` deltaP `2.0623` edge `0.0335` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-0.9207` n `226` status `ready` deltaP `14.5956` edge `0.043` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1457` n `285` status `ready` deltaP `1.6276` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2199` n `285` status `ready` deltaP `3.3189` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6297` n `285` status `ready` deltaP `-7.5412` edge `-0.0493` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.6975` n `285` status `ready` deltaP `7.9119` edge `0.153` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9473` n `226` status `ready` deltaP `1.0816` edge `0.0294` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7285` n `285` status `ready` deltaP `-2.3636` edge `-0.0274` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.8248` n `285` status `ready` deltaP `6.4019` edge `0.1076` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.749` n `226` status `ready` deltaP `6.6065` edge `0.0059` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.8584` n `226` status `ready` deltaP `-10.0802` edge `-0.2518` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.8329` n `226` status `ready` deltaP `-12.9886` edge `-0.0855` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
