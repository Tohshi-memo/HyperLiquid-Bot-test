# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T03:52:37.329320+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4160`

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

- `news_risk_high->equity_4h` score `1.0213` n `68` status `ready` deltaP `8.1151` edge `0.1549` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6875` n `68` status `ready` deltaP `12.6255` edge `0.0209` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2445` n `68` status `ready` deltaP `8.1087` edge `0.1441` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0168` n `68` status `ready` deltaP `6.6573` edge `0.0031` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `-0.0752` n `68` status `ready` deltaP `-2.4918` edge `0.0546` maxDD `-0.2073`
- `news_risk_high->fx_4h` score `-0.1368` n `68` status `ready` deltaP `3.533` edge `0.0035` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.1961` n `68` status `ready` deltaP `-2.2191` edge `0.0446` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.292` n `68` status `ready` deltaP `-0.0792` edge `0.0017` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.5017` n `68` status `ready` deltaP `-3.267` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.241` n `68` status `ready` deltaP `-4.2234` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.7165` n `68` status `ready` deltaP `-7.1467` edge `-0.012` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1133` n `68` status `ready` deltaP `-14.1335` edge `-0.0033` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3393` n `68` status `ready` deltaP `-9.5192` edge `-0.0376` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.4863` n `68` status `ready` deltaP `-5.6798` edge `-0.0518` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.8198` n `68` status `ready` deltaP `-7.4515` edge `-0.0498` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5087` n `68` status `ready` deltaP `-2.3897` edge `-0.2443` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.7975` n `68` status `ready` deltaP `23.366` edge `0.516` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5823` n `68` status `ready` deltaP `-31.6894` edge `-0.0108` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.3225` n `68` status `ready` deltaP `-29.5343` edge `-0.0954` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.4468` n `68` status `ready` deltaP `-29.136` edge `-0.076` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
