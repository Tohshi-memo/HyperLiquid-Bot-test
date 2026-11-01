# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T16:52:32.092400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6601`

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

- `market_context_high->unknown_24h` score `7154.4079` n `55` status `ready` deltaP `1.3889` edge `596.1914` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.105` n `55` status `ready` deltaP `6.2611` edge `31.638` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `75.029` n `55` status `ready` deltaP `4.2107` edge `6.2354` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.0928` n `55` status `ready` deltaP `42.7999` edge `1.496` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1856` n `94` status `ready` deltaP `30.9619` edge `1.028` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.651` n `55` status `ready` deltaP `53.9931` edge `0.1943` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3014` n `55` status `ready` deltaP `44.4003` edge `0.2602` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1714` n `55` status `ready` deltaP `24.5122` edge `0.3803` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.7095` n `55` status `ready` deltaP `31.5023` edge `0.2994` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5213` n `55` status `ready` deltaP `6.3525` edge `0.3213` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3272` n `55` status `ready` deltaP `31.2195` edge `0.0942` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `3.0929` n `121` status `ready` deltaP `13.1072` edge `0.309` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3939` n `55` status `ready` deltaP `10.5114` edge `0.3045` maxDD `-3.0799`
- `news_risk_high->unknown_1h` score `2.2694` n `126` status `ready` deltaP `-7.1024` edge `0.2651` maxDD `-0.9571`
- `market_context_high->crypto_alt_24h` score `1.881` n `55` status `ready` deltaP `-4.2992` edge `0.4216` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6628` n `55` status `ready` deltaP `19.4179` edge `0.0516` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5632` n `55` status `ready` deltaP `3.3261` edge `0.1606` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.483` n `55` status `ready` deltaP `4.5237` edge `0.1605` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4731` n `55` status `ready` deltaP `8.6309` edge `0.1262` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9882` n `55` status `ready` deltaP `12.2237` edge `0.0257` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
