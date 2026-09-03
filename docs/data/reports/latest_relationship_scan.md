# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T01:37:25.683005+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11593`

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

- `risk_on_high->equity_24h` score `5.7067` n `107` status `ready` deltaP `25.0909` edge `0.7228` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.7067` n `107` status `ready` deltaP `25.0909` edge `0.7228` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `5.1317` n `107` status `ready` deltaP `18.0861` edge `0.3689` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `5.1317` n `107` status `ready` deltaP `18.0861` edge `0.3689` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `3.2124` n `147` status `ready` deltaP `13.8201` edge `0.2451` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.7068` n `59` status `ready` deltaP `11.0405` edge `0.3987` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.3092` n `107` status `ready` deltaP `21.2568` edge `0.8447` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3092` n `107` status `ready` deltaP `21.2568` edge `0.8447` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2802` n `59` status `ready` deltaP `21.1776` edge `0.4446` maxDD `-19.4761`
- `market_context_high->equity_24h` score `2.0547` n `147` status `ready` deltaP `21.0601` edge `0.6039` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `0.9771` n `59` status `ready` deltaP `14.348` edge `0.4241` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.4828` n `107` status `ready` deltaP `20.6841` edge `0.7984` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4828` n `107` status `ready` deltaP `20.6841` edge `0.7984` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.4559` n `147` status `ready` deltaP `15.2742` edge `0.7065` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.3202` n `147` status `ready` deltaP `23.7104` edge `0.8294` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2103` n `67` status `ready` deltaP `5.3376` edge `0.0273` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1298` n `108` status `ready` deltaP `8.483` edge `0.0046` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1298` n `108` status `ready` deltaP `8.483` edge `0.0046` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.07` n `107` status `ready` deltaP `19.7159` edge `0.0106` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.07` n `107` status `ready` deltaP `19.7159` edge `0.0106` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
