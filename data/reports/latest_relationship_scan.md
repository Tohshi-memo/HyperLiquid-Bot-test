# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T01:37:27.237967+00:00`
- Price records: `672`
- Market context records: `5724`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.9748` n `218` status `ready` deltaP `16.5711` edge `0.5224` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.2917` n `274` status `ready` deltaP `8.9627` edge `0.183` maxDD `-11.8085`
- `market_context_high->equity_4h` score `0.1724` n `274` status `ready` deltaP `7.3093` edge `0.1295` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2139` n `285` status `ready` deltaP `2.9357` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4549` n `285` status `ready` deltaP `1.4855` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6118` n `285` status `ready` deltaP `3.3617` edge `0.0273` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7411` n `285` status `ready` deltaP `-1.4387` edge `-0.0047` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8932` n `285` status `ready` deltaP `2.6316` edge `0.0315` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-1.039` n `285` status `ready` deltaP `0.8867` edge `0.0279` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1309` n `218` status `ready` deltaP `10.6875` edge `0.0421` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1542` n `274` status `ready` deltaP `1.4788` edge `0.0109` maxDD `-3.165`
- `market_context_high->crypto_alt_4h` score `-1.2138` n `274` status `ready` deltaP `6.8008` edge `0.1291` maxDD `-14.3804`
- `market_context_high->fx_4h` score `-1.2574` n `274` status `ready` deltaP `2.6426` edge `0.0057` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.586` n `274` status `ready` deltaP `-6.6706` edge `-0.0495` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8962` n `218` status `ready` deltaP `2.0945` edge `0.0292` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8403` n `274` status `ready` deltaP `-3.5951` edge `-0.0285` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3605` n `218` status `ready` deltaP `7.0225` edge `0.0355` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5704` n `218` status `ready` deltaP `-6.387` edge `-0.2395` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.3771` n `218` status `ready` deltaP `-9.7063` edge `-0.0694` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
