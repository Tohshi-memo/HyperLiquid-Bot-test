# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T11:07:30.786315+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0257` n `54` status `ready` deltaP `38.5017` edge `0.3288` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0257` n `54` status `ready` deltaP `38.5017` edge `0.3288` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `5.6928` n `144` status `ready` deltaP `13.8889` edge `0.5332` maxDD `-6.7783`
- `market_context_high->crypto_major_4h` score `5.6734` n `144` status `ready` deltaP `21.9512` edge `0.4586` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `5.5239` n `70` status `ready` deltaP `30.3441` edge `0.3433` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.5239` n `70` status `ready` deltaP `30.3441` edge `0.3433` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `1.7327` n `70` status `ready` deltaP `7.1429` edge `0.2473` maxDD `-6.7091`
- `risk_on_and_context->crypto_alt_4h` score `1.7327` n `70` status `ready` deltaP `7.1429` edge `0.2473` maxDD `-6.7091`
- `market_context_high->crypto_major_1h` score `0.8624` n `156` status `ready` deltaP `6.8594` edge `0.1067` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.5788` n `156` status `ready` deltaP `8.2911` edge `0.1244` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.372` n `144` status `ready` deltaP `13.0251` edge `0.0487` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.1651` n `82` status `ready` deltaP `6.9252` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1651` n `82` status `ready` deltaP `6.9252` edge `0.006` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1495` n `156` status `ready` deltaP `7.6288` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.2574` n `82` status `ready` deltaP `11.9351` edge `0.0286` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2574` n `82` status `ready` deltaP `11.9351` edge `0.0286` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.3165` n `156` status `ready` deltaP `7.7806` edge `0.0087` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.346` n `156` status `ready` deltaP `10.2622` edge `0.0382` maxDD `-7.0778`
- `risk_on_high->fx_1h` score `-0.3472` n `82` status `ready` deltaP `-0.4322` edge `-0.0036` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3472` n `82` status `ready` deltaP `-0.4322` edge `-0.0036` maxDD `-0.376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
