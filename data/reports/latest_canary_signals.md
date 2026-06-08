# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T20:52:23.303581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1592` n `12`; crypto_alt avg `0.163` n `228`; crypto_major avg `0.0499` n `8`; equity avg `-0.0013` n `74`; fx avg `-0.0033` n `6`; index avg `0.0261` n `23`; metal avg `0.0816` n `18`; unknown avg `0.0102` n `517`
- 1h: commodity avg `0.1228` n `12`; crypto_alt avg `-0.0536` n `228`; crypto_major avg `-0.0422` n `8`; equity avg `0.1058` n `74`; fx avg `-0.0021` n `6`; index avg `0.1824` n `23`; metal avg `0.0627` n `18`; unknown avg `-0.1572` n `517`
- 4h: commodity avg `0.0623` n `12`; crypto_alt avg `0.0905` n `228`; crypto_major avg `0.0158` n `8`; equity avg `-0.5857` n `74`; fx avg `-0.0316` n `6`; index avg `-0.3211` n `23`; metal avg `-0.3026` n `18`; unknown avg `-0.2669` n `517`
- 24h: commodity avg `-0.6011` n `12`; crypto_alt avg `3.084` n `228`; crypto_major avg `3.3631` n `8`; equity avg `2.5085` n `74`; fx avg `-0.2846` n `6`; index avg `1.0459` n `23`; metal avg `0.1849` n `18`; unknown avg `-2.1399` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
