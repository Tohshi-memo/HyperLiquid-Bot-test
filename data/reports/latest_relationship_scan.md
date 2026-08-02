# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T17:37:30.671841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4354.1766` n `68` status `ready` deltaP `25.7148` edge `362.7187` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.052` n `40` status `ready` deltaP `56.8403` edge `1.0818` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.977` n `40` status `ready` deltaP `51.3194` edge `0.5854` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.7152` n `68` status `ready` deltaP `17.7456` edge `0.351` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7143` n `68` status `ready` deltaP `16.9835` edge `0.0677` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0885` n `40` status `ready` deltaP `13.9024` edge `0.1315` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6851` n `68` status `ready` deltaP `10.2413` edge `0.0711` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.6665` n `40` status `ready` deltaP `8.5061` edge `0.1193` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6629` n `40` status `ready` deltaP `20.6098` edge `0.0272` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.6287` n `40` status `ready` deltaP `11.7964` edge `0.0394` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4622` n `40` status `ready` deltaP `14.1467` edge `0.0027` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.3342` n `68` status `ready` deltaP `14.5804` edge `0.0264` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1893` n `68` status `ready` deltaP `6.5369` edge `0.0283` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1061` n `68` status `ready` deltaP `6.4812` edge `0.0386` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0443` n `68` status `ready` deltaP `2.9148` edge `0.0072` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0498` n `68` status `ready` deltaP `3.1173` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1154` n `68` status `ready` deltaP `2.9148` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1641` n `68` status `ready` deltaP `3.1173` edge `0.0302` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4019` n `40` status `ready` deltaP `0.5988` edge `0.0072` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6483` n `68` status `ready` deltaP `3.267` edge `-0.0269` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
