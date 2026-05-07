# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T04:22:19.290123+00:00`
- Price records: `517`
- Market context records: `612`
- Flow alert records: `1731`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.1307` n `146` status `ready` deltaP `7.6286` edge `0.3815` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.5544` n `146` status `ready` deltaP `13.1585` edge `0.3252` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0444` n `146` status `ready` deltaP `9.7283` edge `0.0166` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3405` n `146` status `ready` deltaP `1.643` edge `0.0032` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.634` n `146` status `ready` deltaP `1.1869` edge `0.0367` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6839` n `146` status `ready` deltaP `0.0552` edge `-0.0027` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0145` n `146` status `ready` deltaP `-3.1215` edge `-0.0034` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.0333` n `146` status `ready` deltaP `6.2939` edge `0.0034` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2415` n `146` status `ready` deltaP `-1.9095` edge `-0.0097` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5032` n `146` status `ready` deltaP `5.2511` edge `0.0967` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.619` n `146` status `ready` deltaP `6.1777` edge `-0.0038` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.2659` n `146` status `ready` deltaP `-0.3239` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.269` n `146` status `ready` deltaP `14.4328` edge `0.0853` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.68` n `146` status `ready` deltaP `-7.4587` edge `0.0259` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1644` n `146` status `ready` deltaP `-2.9395` edge `-0.0289` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2796` n `146` status `ready` deltaP `-4.3753` edge `-0.0482` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7234` n `146` status `ready` deltaP `-6.5985` edge `0.0838` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2521` n `146` status `ready` deltaP `-2.408` edge `-0.0119` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6876` n `146` status `ready` deltaP `-10.9884` edge `-0.0569` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.7197` n `146` status `ready` deltaP `2.2216` edge `-0.2203` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
