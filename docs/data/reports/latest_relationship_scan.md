# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T12:07:32.870278+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `market_context_high->unknown_24h` score `273.0808` n `117` status `ready` deltaP `10.9129` edge `22.722` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.5474` n `62` status `ready` deltaP `34.1611` edge `0.5882` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6411` n `62` status `ready` deltaP `20.1908` edge `0.4699` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.4558` n `62` status `ready` deltaP `10.7305` edge `0.2264` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2124` n `62` status `ready` deltaP `22.6804` edge `0.1165` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.8026` n `117` status `ready` deltaP `14.0205` edge `0.2365` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5513` n `62` status `ready` deltaP `28.8012` edge `0.0468` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9348` n `62` status `ready` deltaP `7.3305` edge `0.1479` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.7923` n `62` status `ready` deltaP `22.9284` edge `0.0115` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7054` n `62` status `ready` deltaP `16.8618` edge `0.0895` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1933` n `117` status `ready` deltaP `16.2967` edge `0.0608` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1718` n `62` status `ready` deltaP `17.1321` edge `0.0776` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.0736` n `117` status `ready` deltaP `21.4848` edge `0.0219` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7527` n `117` status `ready` deltaP `12.8423` edge `0.0055` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.7499` n `62` status `ready` deltaP `27.0092` edge `0.0727` maxDD `-8.196`
- `market_context_high->commodity_1h` score `0.707` n `117` status `ready` deltaP `11.6063` edge `0.0212` maxDD `-0.5059`
- `news_risk_high->crypto_alt_1h` score `0.6992` n `62` status `ready` deltaP `2.26` edge `0.0951` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.5163` n `117` status `ready` deltaP `-0.7218` edge `0.2202` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0899` n `62` status `ready` deltaP `4.5055` edge `0.0043` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.1809` n `117` status `ready` deltaP `6.917` edge `0.0277` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
