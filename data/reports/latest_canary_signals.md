# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T23:52:28.073136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.1511` n `228`; crypto_major avg `-0.2045` n `8`; equity avg `-0.1087` n `74`; fx avg `0.0138` n `6`; index avg `-0.1249` n `23`; metal avg `-0.143` n `18`; unknown avg `0.0343` n `517`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.5928` n `228`; crypto_major avg `-0.371` n `8`; equity avg `0.0666` n `74`; fx avg `0.0129` n `6`; index avg `-0.0233` n `23`; metal avg `-0.2444` n `18`; unknown avg `0.4044` n `517`
- 4h: commodity avg `-0.0075` n `12`; crypto_alt avg `-1.1679` n `228`; crypto_major avg `-0.421` n `8`; equity avg `0.0471` n `74`; fx avg `0.009` n `6`; index avg `0.092` n `23`; metal avg `-0.2005` n `18`; unknown avg `-0.8236` n `517`
- 24h: commodity avg `-0.5529` n `12`; crypto_alt avg `0.5119` n `228`; crypto_major avg `1.1191` n `8`; equity avg `2.0546` n `74`; fx avg `-0.2613` n `6`; index avg `0.8391` n `23`; metal avg `-0.4943` n `18`; unknown avg `-3.0757` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
