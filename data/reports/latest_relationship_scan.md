# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T15:52:22.856782+00:00`
- Price records: `672`
- Market context records: `2155`
- Flow alert records: `8101`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6712` n `146` status `ready` deltaP `37.9051` edge `0.9802` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9649` n `146` status `ready` deltaP `41.8601` edge `0.771` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2448` n `146` status `ready` deltaP `24.6617` edge `0.4309` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.6108` n `146` status `ready` deltaP `25.7079` edge `0.3223` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.1118` n `39` status `ready` deltaP `31.3165` edge `0.3855` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.5263` n `146` status `ready` deltaP `13.7391` edge `0.3251` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.4375` n `146` status `ready` deltaP `18.0851` edge `0.2136` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2753` n `146` status `ready` deltaP `24.031` edge `0.1811` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.2345` n `146` status `ready` deltaP `16.2025` edge `0.2479` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.837` n `146` status `ready` deltaP `27.3688` edge `0.586` maxDD `-35.8966`
- `market_context_high->metal_4h` score `2.8198` n `146` status `ready` deltaP `20.7045` edge `0.2357` maxDD `-4.7664`
- `market_context_high->equity_24h` score `2.7776` n `146` status `ready` deltaP `25.5161` edge `0.5512` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.5416` n `39` status `ready` deltaP `31.8441` edge `0.0179` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1815` n `146` status `ready` deltaP `20.5741` edge `1.0011` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4159` n `39` status `ready` deltaP `14.2824` edge `0.0951` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0231` n `43` status `ready` deltaP `18.8692` edge `0.0064` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8009` n `43` status `ready` deltaP `10.6148` edge `0.0999` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7382` n `146` status `ready` deltaP `9.9377` edge `0.0741` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6355` n `146` status `ready` deltaP `9.5029` edge `0.0566` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4753` n `43` status `ready` deltaP `8.2892` edge `0.01` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
