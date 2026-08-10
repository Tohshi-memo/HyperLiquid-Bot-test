# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T03:22:29.394504+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.4254` n `162` status `ready` deltaP `15.9873` edge `0.0795` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7527` n `174` status `ready` deltaP `10.0988` edge `0.0297` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5413` n `138` status `ready` deltaP `19.0746` edge `0.023` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.1896` n `174` status `ready` deltaP `3.8492` edge `-0.0008` maxDD `-0.9335`
- `market_context_high->fx_4h` score `-0.192` n `162` status `ready` deltaP `6.3403` edge `0.0049` maxDD `-1.4094`
- `market_context_high->index_24h` score `-0.6199` n `138` status `ready` deltaP `1.9474` edge `0.0885` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.82` n `162` status `ready` deltaP `-2.5463` edge `-0.0099` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8206` n `174` status `ready` deltaP `-4.6648` edge `-0.0105` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8588` n `174` status `ready` deltaP `-2.4571` edge `-0.0067` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.8986` n `174` status `ready` deltaP `-3.3416` edge `-0.0049` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-1.1837` n `138` status `ready` deltaP `-3.3137` edge `0.0339` maxDD `-2.503`
- `market_context_high->equity_24h` score `-1.3265` n `138` status `ready` deltaP `-1.2832` edge `0.204` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5391` n `174` status `ready` deltaP `-8.76` edge `-0.0368` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9217` n `162` status `ready` deltaP `-7.4243` edge `-0.0357` maxDD `-5.8942`
- `market_context_high->equity_4h` score `-2.5721` n `162` status `ready` deltaP `-7.2795` edge `-0.0975` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5608` n `174` status `ready` deltaP `-9.968` edge `-0.0569` maxDD `-10.5372`
- `market_context_high->crypto_alt_24h` score `-4.3636` n `138` status `ready` deltaP `-11.1036` edge `-0.1453` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7845` n `138` status `ready` deltaP `-2.023` edge `-0.1358` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-6.2893` n `162` status `ready` deltaP `-12.7127` edge `-0.1636` maxDD `-15.3937`
- `market_context_high->unknown_1h` score `-7.5271` n `174` status `ready` deltaP `-4.5977` edge `-0.5509` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
