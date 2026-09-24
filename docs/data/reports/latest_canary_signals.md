# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T06:22:31.235808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `0.02` n `234`; crypto_major avg `0.0631` n `8`; equity avg `-0.035` n `141`; fx avg `0.0233` n `6`; index avg `-0.0059` n `26`; metal avg `0.0164` n `20`; unknown avg `0.1197` n `945`
- 1h: commodity avg `0.1345` n `12`; crypto_alt avg `-0.284` n `234`; crypto_major avg `-0.1982` n `8`; equity avg `-0.2826` n `141`; fx avg `0.0365` n `6`; index avg `-0.05` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.0606` n `927`
- 4h: commodity avg `0.1768` n `12`; crypto_alt avg `0.9451` n `234`; crypto_major avg `0.4073` n `8`; equity avg `-0.414` n `141`; fx avg `0.0246` n `6`; index avg `-0.0729` n `26`; metal avg `0.0524` n `20`; unknown avg `1.2847` n `921`
- 24h: commodity avg `0.6619` n `12`; crypto_alt avg `-4.2609` n `234`; crypto_major avg `-3.9255` n `8`; equity avg `-2.0729` n `140`; fx avg `0.0586` n `6`; index avg `-0.42` n `26`; metal avg `-0.5242` n `20`; unknown avg `585.5264` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
