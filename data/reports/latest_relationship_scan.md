# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T12:07:22.883403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4735`

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

- `market_context_high->unknown_4h` score `81.2176` n `37` status `ready` deltaP `-4.396` edge `6.8422` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.0525` n `37` status `ready` deltaP `15.4139` edge `0.8311` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3512` n `39` status `ready` deltaP `12.4367` edge `0.2423` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1327` n `37` status `ready` deltaP `33.7714` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.5872` n `35` status `ready` deltaP `30.6054` edge `0.0201` maxDD `-0.016`
- `market_context_high->index_4h` score `2.0962` n `37` status `ready` deltaP `27.2701` edge `0.0399` maxDD `-2.4279`
- `news_risk_high->fx_1h` score `1.4405` n `35` status `ready` deltaP `18.148` edge `0.0081` maxDD `-0.0567`
- `market_context_high->crypto_major_1h` score `1.1357` n `39` status `ready` deltaP `12.1181` edge `0.0724` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `1.1345` n `39` status `ready` deltaP `14.2139` edge `0.0813` maxDD `-3.1881`
- `market_context_high->index_24h` score `0.8483` n `37` status `ready` deltaP `10.6982` edge `0.1005` maxDD `-2.7123`
- `market_context_high->commodity_24h` score `0.7539` n `37` status `ready` deltaP `7.2542` edge `0.1678` maxDD `-6.5601`
- `market_context_high->fx_24h` score `0.6734` n `37` status `ready` deltaP `10.9422` edge `-0.008` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.4836` n `39` status `ready` deltaP `7.9649` edge `0.0143` maxDD `-0.1681`
- `news_risk_high->fx_24h` score `0.2549` n `32` status `ready` deltaP `-1.3889` edge `0.0526` maxDD `-0.1014`
- `market_context_high->index_1h` score `0.1927` n `39` status `ready` deltaP `2.1803` edge `0.0372` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0645` n `39` status `ready` deltaP `7.9457` edge `0.0099` maxDD `-1.7019`
- `news_risk_high->equity_4h` score `-0.0247` n `35` status `ready` deltaP `-2.304` edge `0.0872` maxDD `-4.2454`
- `market_context_high->metal_1h` score `-0.0518` n `39` status `ready` deltaP `1.5815` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0599` n `37` status `ready` deltaP `2.2248` edge `0.0229` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.1077` n `35` status `ready` deltaP `5.1839` edge `0.0018` maxDD `-0.2931`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
