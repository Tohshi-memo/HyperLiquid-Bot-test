# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T15:37:25.212965+00:00`
- Price records: `562`
- Market context records: `659`
- Flow alert records: `1869`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `848`

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

- `market_context_high->crypto_major_24h` score `7.9793` n `146` status `ready` deltaP `20.7508` edge `0.56` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.217` n `146` status `ready` deltaP `8.7572` edge `0.4645` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1447` n `146` status `ready` deltaP `8.2192` edge `0.0138` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.329` n `147` status `ready` deltaP `1.9082` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.3889` n `147` status `ready` deltaP `2.4509` edge `0.0487` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6288` n `147` status `ready` deltaP `0.5747` edge `0.0009` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1933` n `147` status `ready` deltaP `-4.4254` edge `-0.0096` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2138` n `147` status `ready` deltaP `5.5227` edge `-0.0065` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2608` n `147` status `ready` deltaP `-1.9107` edge `-0.0113` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6305` n `147` status `ready` deltaP `5.7787` edge `-0.0021` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9314` n `146` status `ready` deltaP `4.5185` edge `0.0659` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.0132` n `146` status `ready` deltaP `1.2309` edge `-0.0237` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.0851` n `146` status `ready` deltaP `15.1412` edge `0.0959` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.8978` n `146` status `ready` deltaP `-9.251` edge `0.0197` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.0795` n `146` status `ready` deltaP `-4.1298` edge `0.121` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.1907` n `146` status `ready` deltaP `-3.0127` edge `-0.0306` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4803` n `147` status `ready` deltaP `-5.5043` edge `-0.0574` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.6071` n `146` status `ready` deltaP `-6.7307` edge `-0.0286` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7229` n `146` status `ready` deltaP `-11.6705` edge `-0.0553` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8029` n `146` status `ready` deltaP `1.0612` edge `-0.2195` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
