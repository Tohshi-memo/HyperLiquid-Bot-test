# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T03:22:28.179494+00:00`
- Price records: `672`
- Market context records: `5519`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `market_context_high->equity_24h` score `3.3459` n `190` status `ready` deltaP `13.0081` edge `0.7` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.6928` n `190` status `ready` deltaP `16.2189` edge `0.5703` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.5369` n `193` status `ready` deltaP `13.8838` edge `0.3481` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.9281` n `193` status `ready` deltaP `9.189` edge `0.2635` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.9056` n `193` status `ready` deltaP `10.3153` edge `0.2539` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.3958` n `190` status `ready` deltaP `12.9312` edge `0.0395` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2485` n `193` status `ready` deltaP `7.6852` edge `0.066` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0133` n `193` status `ready` deltaP `5.4978` edge `0.0138` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3494` n `193` status `ready` deltaP `0.6275` edge `-0.0001` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3827` n `193` status `ready` deltaP `0.9843` edge `0.0577` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4835` n `193` status `ready` deltaP `2.5736` edge `0.0671` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7117` n `193` status `ready` deltaP `0.3165` edge `0.0061` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9392` n `193` status `ready` deltaP `2.2992` edge `0.0045` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0953` n `193` status `ready` deltaP `5.2272` edge `0.0348` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6285` n `193` status `ready` deltaP `-4.4732` edge `-0.0111` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8287` n `190` status `ready` deltaP `14.2708` edge `0.0691` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0352` n `193` status `ready` deltaP `-12.0853` edge `-0.0561` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5793` n `193` status `ready` deltaP `-8.9433` edge `-0.0547` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.163` n `190` status `ready` deltaP `7.2442` edge `0.2245` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3165` n `190` status `ready` deltaP `-4.2379` edge `-0.172` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
