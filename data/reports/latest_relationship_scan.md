# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T15:52:26.779008+00:00`
- Price records: `672`
- Market context records: `4948`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9472`

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

- `market_context_high->unknown_1h` score `19.1107` n `96` status `ready` deltaP `9.6619` edge `1.5699` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.2257` n `93` status `ready` deltaP `28.0537` edge `0.8832` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.2801` n `93` status `ready` deltaP `21.1038` edge `0.5884` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.0505` n `93` status `ready` deltaP `21.7299` edge `0.5779` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.7964` n `91` status `ready` deltaP `27.0891` edge `0.3367` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7984` n `93` status `ready` deltaP `14.8374` edge `0.1891` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6774` n `93` status `ready` deltaP `12.7819` edge `0.1208` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9929` n `93` status `ready` deltaP `12.6623` edge `0.0445` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8654` n `96` status `ready` deltaP `7.8842` edge `0.0769` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8606` n `96` status `ready` deltaP `8.8011` edge `0.1555` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.679` n `96` status `ready` deltaP `9.6744` edge `0.1248` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.099` n `96` status `ready` deltaP `4.491` edge `0.0363` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.3733` n `96` status `ready` deltaP `1.6529` edge `0.0071` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4058` n `96` status `ready` deltaP `1.628` edge `0.0126` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9497` n `93` status `ready` deltaP `6.6188` edge `-0.0046` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1567` n `93` status `ready` deltaP `-6.9974` edge `-0.0046` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.3815` n `91` status `ready` deltaP `-0.4349` edge `-0.0112` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.6205` n `96` status `ready` deltaP `-10.242` edge `-0.0055` maxDD `-0.5675`
- `market_context_high->commodity_24h` score `-3.9995` n `91` status `ready` deltaP `19.6485` edge `0.0466` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.8866` n `91` status `ready` deltaP `-8.8199` edge `0.0304` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
