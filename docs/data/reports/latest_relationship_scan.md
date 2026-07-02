# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T14:26:08.323846+00:00`
- Price records: `672`
- Market context records: `5463`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11460`

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

- `market_context_high->crypto_major_24h` score `3.7416` n `195` status `ready` deltaP `16.8937` edge `0.6532` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4326` n `198` status `ready` deltaP `14.5602` edge `0.3349` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9857` n `198` status `ready` deltaP `11.6454` edge `0.2517` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8709` n `198` status `ready` deltaP `9.6437` edge `0.2557` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.248` n `198` status `ready` deltaP `7.8737` edge `0.0647` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1021` n `198` status `ready` deltaP `6.4719` edge `0.0147` maxDD `-0.9472`
- `market_context_high->equity_24h` score `0.061` n `195` status `ready` deltaP `8.4722` edge `0.4565` maxDD `-31.6316`
- `market_context_high->fx_24h` score `0.0414` n `195` status `ready` deltaP `9.7916` edge `0.0309` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3492` n `198` status `ready` deltaP `0.617` edge `0.0` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3731` n `198` status `ready` deltaP `3.2738` edge `0.0146` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5561` n `198` status `ready` deltaP `0.4673` edge `0.0467` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7424` n `198` status `ready` deltaP `1.6467` edge `0.0517` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.9421` n `198` status `ready` deltaP `6.6319` edge `0.0382` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0357` n `198` status `ready` deltaP `1.7261` edge `0.0047` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3998` n `198` status `ready` deltaP `-2.3937` edge `-0.0059` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9805` n `195` status `ready` deltaP `12.4759` edge `0.0616` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.9978` n `198` status `ready` deltaP `-7.8144` edge `-0.0286` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1546` n `198` status `ready` deltaP `-5.2907` edge `-0.0395` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-6.9974` n `195` status `ready` deltaP `-2.7804` edge `-0.1408` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.0193` n `195` status `ready` deltaP `8.2158` edge `0.23` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
