# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T00:22:22.171443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0529` n `228`; crypto_major avg `-0.1299` n `8`; equity avg `-0.0717` n `74`; fx avg `0.0156` n `6`; index avg `-0.109` n `23`; metal avg `-0.0941` n `18`; unknown avg `-0.0354` n `517`
- 1h: commodity avg `-0.0773` n `12`; crypto_alt avg `-0.5059` n `228`; crypto_major avg `-0.4659` n `8`; equity avg `-0.3599` n `74`; fx avg `0.0477` n `6`; index avg `-0.3225` n `23`; metal avg `-0.3241` n `18`; unknown avg `0.0664` n `517`
- 4h: commodity avg `-0.0887` n `12`; crypto_alt avg `-1.0095` n `228`; crypto_major avg `-0.4862` n `8`; equity avg `-0.2676` n `74`; fx avg `0.0368` n `6`; index avg `-0.2848` n `23`; metal avg `-0.1525` n `18`; unknown avg `-0.9084` n `517`
- 24h: commodity avg `-0.6296` n `12`; crypto_alt avg `0.2877` n `228`; crypto_major avg `0.6723` n `8`; equity avg `0.8695` n `74`; fx avg `-0.2348` n `6`; index avg `0.2581` n `23`; metal avg `-0.7679` n `18`; unknown avg `-3.1265` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
