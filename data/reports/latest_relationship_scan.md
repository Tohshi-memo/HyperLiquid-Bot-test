# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T03:37:32.602988+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5356`

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

- `market_context_high->unknown_1h` score `112.6234` n `101` status `ready` deltaP `-0.6981` edge `9.4314` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.6116` n `95` status `ready` deltaP `2.4743` edge `5.9823` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `11.1018` n `58` status `ready` deltaP `30.0707` edge `0.7383` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.6093` n `58` status `ready` deltaP `25.431` edge `0.6932` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.3189` n `65` status `ready` deltaP `32.3992` edge `0.5809` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1206` n `65` status `ready` deltaP `20.2439` edge `0.5095` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.2778` n `65` status `ready` deltaP `15.374` edge `0.264` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.2116` n `95` status `ready` deltaP `17.9862` edge `0.3014` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3913` n `65` status `ready` deltaP `23.6111` edge `0.1252` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8865` n `65` status `ready` deltaP `31.7613` edge `0.055` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.7356` n `65` status `ready` deltaP `20.5769` edge `0.1518` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.542` n `65` status `ready` deltaP `10.3155` edge `0.1786` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0866` n `65` status `ready` deltaP `25.7669` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `2.0129` n `65` status `ready` deltaP `18.4686` edge `0.0862` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `1.8883` n `101` status `ready` deltaP `13.4686` edge `0.1126` maxDD `-2.2692`
- `market_context_high->fx_4h` score `1.5147` n `95` status `ready` deltaP `25.9339` edge `0.029` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.4086` n `58` status `ready` deltaP `18.3908` edge `0.0869` maxDD `-1.703`
- `market_context_high->equity_24h` score `1.408` n `58` status `ready` deltaP `4.2864` edge `0.109` maxDD `-0.6196`
- `news_risk_high->crypto_alt_1h` score `1.2752` n `65` status `ready` deltaP `3.9705` edge `0.1317` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.0004` n `95` status `ready` deltaP `3.4018` edge `0.2396` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
