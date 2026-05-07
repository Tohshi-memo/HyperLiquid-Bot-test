# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T16:52:14.170332+00:00`
- Price records: `567`
- Market context records: `664`
- Flow alert records: `1885`
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

- `market_context_high->crypto_major_24h` score `8.4057` n `146` status `ready` deltaP `21.5048` edge `0.5905` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4107` n `146` status `ready` deltaP `8.8692` edge `0.4799` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1739` n `146` status `ready` deltaP `7.7622` edge `0.0131` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.353` n `147` status `ready` deltaP `1.5078` edge `0.0025` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5297` n `147` status `ready` deltaP `1.9666` edge `0.0402` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5679` n `147` status `ready` deltaP `1.1172` edge `0.0051` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1201` n `147` status `ready` deltaP `-1.352` edge `-0.0033` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1563` n `147` status `ready` deltaP `-4.1287` edge `-0.0085` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2089` n `147` status `ready` deltaP `5.5087` edge `-0.006` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5662` n `147` status `ready` deltaP `6.253` edge `0.0001` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.7337` n `146` status `ready` deltaP `5.1301` edge `0.0783` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-1.8699` n `146` status `ready` deltaP `15.6565` edge `0.1104` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.8801` n `146` status `ready` deltaP `1.8144` edge `-0.0165` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.7386` n `146` status `ready` deltaP `-8.5961` edge `0.0286` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.9801` n `146` status `ready` deltaP `-2.3904` edge `-0.0172` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.3034` n `146` status `ready` deltaP `-4.6931` edge `0.1061` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.3456` n `147` status `ready` deltaP `-4.9902` edge `-0.0496` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-4.5023` n `146` status `ready` deltaP `-10.953` edge `-0.0417` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6625` n `146` status `ready` deltaP `-7.4213` edge `-0.0311` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7` n `146` status `ready` deltaP `1.4481` edge `-0.2135` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
