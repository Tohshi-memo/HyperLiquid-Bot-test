# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T02:52:11.609948+00:00`
- Price records: `511`
- Market context records: `606`
- Flow alert records: `1712`
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

- `market_context_high->crypto_alt_24h` score `4.8041` n `146` status `ready` deltaP `7.0259` edge `0.3583` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.0566` n `146` status `ready` deltaP `12.0218` edge `0.2913` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0007` n `146` status `ready` deltaP `10.3577` edge `0.018` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3191` n `146` status `ready` deltaP `1.9785` edge `0.0037` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5871` n `146` status `ready` deltaP `1.6231` edge `0.0377` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6605` n `146` status `ready` deltaP `0.5215` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.0446` n `146` status `ready` deltaP `6.1982` edge `0.0031` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.076` n `146` status `ready` deltaP `-3.5449` edge `-0.0057` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2124` n `146` status `ready` deltaP `-1.6654` edge `-0.0089` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6682` n `146` status `ready` deltaP `5.7428` edge `-0.005` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.7263` n `146` status `ready` deltaP `4.4431` edge `0.0835` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2309` n `146` status `ready` deltaP `0.099` edge `-0.0343` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4747` n `146` status `ready` deltaP `13.736` edge `0.0728` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.5647` n `146` status `ready` deltaP `-7.1576` edge `0.0335` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2012` n `146` status `ready` deltaP `-3.1596` edge `-0.0305` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3201` n `146` status `ready` deltaP `-4.6567` edge `-0.0497` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7753` n `146` status `ready` deltaP `-7.0976` edge `0.0828` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2898` n `146` status `ready` deltaP `-2.8631` edge `-0.0137` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6152` n `146` status `ready` deltaP `-10.7889` edge `-0.0522` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8945` n `146` status `ready` deltaP `1.4764` edge `-0.2299` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
