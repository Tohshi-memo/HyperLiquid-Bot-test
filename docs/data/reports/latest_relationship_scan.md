# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T01:52:25.063319+00:00`
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

- `risk_on_high->equity_24h` score `5.6815` n `107` status `ready` deltaP `25.0909` edge `0.7207` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.6815` n `107` status `ready` deltaP `25.0909` edge `0.7207` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `4.8447` n `107` status `ready` deltaP `17.9337` edge `0.346` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `4.8447` n `107` status `ready` deltaP `17.9337` edge `0.346` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `2.9254` n `147` status `ready` deltaP `13.6677` edge `0.2222` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.6816` n `59` status `ready` deltaP `11.0405` edge `0.3966` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.3177` n `107` status `ready` deltaP `21.2568` edge `0.8458` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3177` n `107` status `ready` deltaP `21.2568` edge `0.8458` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2888` n `59` status `ready` deltaP `21.1776` edge `0.4457` maxDD `-19.4761`
- `market_context_high->equity_24h` score `2.0384` n `147` status `ready` deltaP `21.0601` edge `0.6018` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.1719` n `109` status `ready` deltaP `1.7951` edge `0.1434` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.1719` n `109` status `ready` deltaP `1.7951` edge `0.1434` maxDD `-1.95`
- `news_risk_high->crypto_major_24h` score `1.0131` n `59` status `ready` deltaP `14.348` edge `0.4271` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.5062` n `107` status `ready` deltaP `20.6841` edge `0.8014` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.5062` n `107` status `ready` deltaP `20.6841` edge `0.8014` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.4645` n `147` status `ready` deltaP `15.2742` edge `0.7076` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.3436` n `147` status `ready` deltaP `23.7104` edge `0.8324` maxDD `-61.3797`
- `market_context_high->unknown_1h` score `0.2196` n `151` status `ready` deltaP `0.4888` edge `0.0781` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `0.2001` n `67` status `ready` deltaP `5.1852` edge `0.027` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1513` n `109` status `ready` deltaP `8.8653` edge `0.0048` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
