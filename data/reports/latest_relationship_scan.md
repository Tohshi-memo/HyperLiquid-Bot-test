# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T02:37:31.972600+00:00`
- Price records: `672`
- Market context records: `5728`
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

- `market_context_high->equity_24h` score `0.9169` n `218` status `ready` deltaP `15.8767` edge `0.5196` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1355` n `278` status `ready` deltaP `7.1932` edge `0.1272` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2381` n `285` status `ready` deltaP `2.4866` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4385` n `285` status `ready` deltaP `1.7849` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.625` n `285` status `ready` deltaP `3.212` edge `0.0272` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.625` n `285` status `ready` deltaP `0.4376` edge `0.0038` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.78` n `285` status `ready` deltaP `-2.0375` edge `-0.0057` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8404` n `285` status `ready` deltaP `2.931` edge `0.0339` maxDD `-5.5448`
- `market_context_high->crypto_major_4h` score `-0.9705` n `278` status `ready` deltaP `8.0595` edge `0.1646` maxDD `-16.9363`
- `market_context_high->crypto_alt_1h` score `-0.9851` n `285` status `ready` deltaP `1.1861` edge `0.0304` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1204` n `218` status `ready` deltaP `10.8611` edge `0.0423` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1496` n `278` status `ready` deltaP `1.5968` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2547` n `278` status `ready` deltaP `2.6946` edge `0.0057` maxDD `-1.4288`
- `market_context_high->crypto_alt_4h` score `-2.3578` n `278` status `ready` deltaP `5.9134` edge `0.1148` maxDD `-19.0564`
- `market_context_high->metal_4h` score `-2.6012` n `278` status `ready` deltaP `-6.9936` edge `-0.0493` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.9369` n `218` status `ready` deltaP `1.4001` edge `0.0286` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8219` n `278` status `ready` deltaP `-3.2911` edge `-0.029` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3833` n `218` status `ready` deltaP `7.0225` edge `0.0336` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6252` n `218` status `ready` deltaP `-7.0814` edge `-0.2419` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.4771` n `218` status `ready` deltaP `-10.4008` edge `-0.0731` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
