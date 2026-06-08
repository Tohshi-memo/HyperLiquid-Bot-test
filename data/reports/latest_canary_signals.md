# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T21:09:16.349583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0641` n `12`; crypto_alt avg `0.4361` n `228`; crypto_major avg `0.688` n `8`; equity avg `0.1057` n `74`; fx avg `0.0496` n `6`; index avg `0.0814` n `23`; metal avg `0.0801` n `18`; unknown avg `0.1471` n `517`
- 1h: commodity avg `0.2216` n `12`; crypto_alt avg `0.451` n `228`; crypto_major avg `0.568` n `8`; equity avg `0.0805` n `74`; fx avg `0.035` n `6`; index avg `0.238` n `23`; metal avg `0.1379` n `18`; unknown avg `0.0366` n `517`
- 4h: commodity avg `0.1551` n `12`; crypto_alt avg `0.5423` n `228`; crypto_major avg `0.899` n `8`; equity avg `-0.2273` n `74`; fx avg `0.0182` n `6`; index avg `-0.1317` n `23`; metal avg `-0.145` n `18`; unknown avg `-0.1541` n `517`
- 24h: commodity avg `-0.5812` n `12`; crypto_alt avg `3.7551` n `228`; crypto_major avg `4.3515` n `8`; equity avg `2.6166` n `74`; fx avg `-0.2511` n `6`; index avg `1.0143` n `23`; metal avg `0.2556` n `18`; unknown avg `-2.0408` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
