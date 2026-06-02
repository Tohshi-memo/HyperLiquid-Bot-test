# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T20:07:24.163049+00:00`
- Price records: `672`
- Market context records: `2695`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `9.9283` n `111` status `ready` deltaP `16.3523` edge `1.0677` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6635` n `111` status `ready` deltaP `17.652` edge `0.6371` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8664` n `141` status `ready` deltaP `5.876` edge `0.138` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.217` n `141` status `ready` deltaP `11.5897` edge `0.0347` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1247` n `143` status `ready` deltaP `3.0485` edge `0.0421` maxDD `-3.1587`
- `market_context_high->index_1h` score `-0.1394` n `143` status `ready` deltaP `3.35` edge `0.0092` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.433` n `143` status `ready` deltaP `1.9985` edge `0.0065` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4668` n `143` status `ready` deltaP `0.2513` edge `0.0038` maxDD `-0.2164`
- `market_context_high->fx_24h` score `-0.5028` n `111` status `ready` deltaP `7.348` edge `-0.0037` maxDD `-0.6418`
- `market_context_high->crypto_alt_1h` score `-0.5097` n `143` status `ready` deltaP `6.5942` edge `0.0667` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.5386` n `141` status `ready` deltaP `16.4343` edge `0.2783` maxDD `-28.6198`
- `market_context_high->crypto_major_24h` score `-0.6622` n `111` status `ready` deltaP `5.9967` edge `0.6314` maxDD `-44.169`
- `market_context_high->metal_1h` score `-0.7442` n `143` status `ready` deltaP `-1.25` edge `-0.0025` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.771` n `141` status `ready` deltaP `-0.8119` edge `0.0107` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.8159` n `111` status `ready` deltaP `6.7474` edge `0.1598` maxDD `-12.4171`
- `market_context_high->index_24h` score `-0.9182` n `111` status `ready` deltaP `3.6693` edge `-0.0029` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `-0.9877` n `143` status `ready` deltaP `3.4976` edge `0.037` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-0.9988` n `141` status `ready` deltaP `4.7493` edge `0.0323` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2295` n `143` status `ready` deltaP `-4.4857` edge `0.0113` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-2.059` n `141` status `ready` deltaP `-1.5201` edge `-0.021` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
