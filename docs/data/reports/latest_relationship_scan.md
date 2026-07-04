# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T12:37:30.442101+00:00`
- Price records: `672`
- Market context records: `5663`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.2386` n `191` status `ready` deltaP `15.5323` edge `0.5909` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8679` n `241` status `ready` deltaP `11.0212` edge `0.2281` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4622` n `241` status `ready` deltaP `7.5574` edge `0.152` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.2466` n `241` status `ready` deltaP `7.7947` edge `0.1535` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.1202` n `191` status `ready` deltaP `17.3521` edge `0.0536` maxDD `-2.4077`
- `market_context_high->fx_1h` score `-0.2498` n `253` status `ready` deltaP `2.1739` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4487` n `253` status `ready` deltaP `4.7857` edge `0.0314` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5215` n `253` status `ready` deltaP `0.1438` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5309` n `253` status `ready` deltaP `2.1923` edge `0.0373` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7866` n `253` status `ready` deltaP `3.21` edge `0.0376` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8669` n `253` status `ready` deltaP `1.0958` edge `-0.003` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9179` n `253` status `ready` deltaP `0.7728` edge `0.0052` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2246` n `241` status `ready` deltaP `2.9596` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2896` n `241` status `ready` deltaP `-1.0291` edge `0.0087` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3695` n `191` status `ready` deltaP `8.506` edge `0.0382` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0087` n `241` status `ready` deltaP `-13.9004` edge `-0.0547` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.754` n `241` status `ready` deltaP `-1.7819` edge `-0.0334` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8316` n `191` status `ready` deltaP `3.5095` edge `0.028` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.438` n `191` status `ready` deltaP `-14.0398` edge `-0.2521` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.4934` n `191` status `ready` deltaP `-12.8436` edge `-0.0946` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
