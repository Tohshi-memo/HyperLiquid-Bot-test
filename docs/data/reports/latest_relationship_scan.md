# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T08:37:24.315710+00:00`
- Price records: `672`
- Market context records: `3161`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8854`

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

- `market_context_high->commodity_24h` score `13.8365` n `104` status `ready` deltaP `47.1554` edge `0.8815` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.1182` n `104` status `ready` deltaP `15.438` edge `2.4483` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.7738` n `104` status `ready` deltaP `21.0069` edge `0.8899` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.332` n `104` status `ready` deltaP `30.0213` edge `0.8671` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.855` n `104` status `ready` deltaP `13.6885` edge `1.3728` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9379` n `137` status `ready` deltaP `18.6043` edge `0.1666` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.5226` n `104` status `ready` deltaP `11.4316` edge `0.0026` maxDD `-0.4876`
- `market_context_high->commodity_1h` score `0.1896` n `137` status `ready` deltaP `4.1643` edge `0.0303` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.374` n `137` status `ready` deltaP `6.0918` edge `0.1244` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.4401` n `137` status `ready` deltaP `4.9128` edge `0.0171` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.8566` n `137` status `ready` deltaP `9.4112` edge `0.0881` maxDD `-14.7778`
- `market_context_high->equity_1h` score `-0.8889` n `137` status `ready` deltaP `3.3032` edge `0.0126` maxDD `-8.8863`
- `market_context_high->index_4h` score `-1.0254` n `137` status `ready` deltaP `14.1368` edge `0.0652` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0379` n `137` status `ready` deltaP `2.7033` edge `0.0752` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1134` n `137` status `ready` deltaP `-10.3785` edge `-0.0053` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.3999` n `137` status `ready` deltaP `-12.5245` edge `-0.0075` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.095` n `137` status `ready` deltaP `-4.1272` edge `-0.0077` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.9329` n `137` status `ready` deltaP `13.8085` edge `0.0625` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.996` n `137` status `ready` deltaP `19.3375` edge `0.4259` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.2642` n `137` status `ready` deltaP `1.7134` edge `-0.0808` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
