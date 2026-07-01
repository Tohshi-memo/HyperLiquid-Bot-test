# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T07:37:31.241385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `0.0164` n `228`; crypto_major avg `-0.0831` n `8`; equity avg `-0.0018` n `88`; fx avg `0.0021` n `6`; index avg `0.0059` n `23`; metal avg `0.0032` n `20`; unknown avg `0.0136` n `765`
- 1h: commodity avg `0.0855` n `12`; crypto_alt avg `-0.0221` n `228`; crypto_major avg `0.1204` n `8`; equity avg `-0.078` n `88`; fx avg `-0.0239` n `6`; index avg `-0.0074` n `23`; metal avg `0.0625` n `20`; unknown avg `0.0223` n `763`
- 4h: commodity avg `-0.0757` n `12`; crypto_alt avg `-0.5142` n `228`; crypto_major avg `-0.8954` n `8`; equity avg `-0.3432` n `88`; fx avg `-0.0439` n `6`; index avg `-0.0599` n `23`; metal avg `-0.17` n `20`; unknown avg `0.1576` n `743`
- 24h: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.8823` n `228`; crypto_major avg `-0.7627` n `8`; equity avg `0.2019` n `88`; fx avg `0.0846` n `6`; index avg `-0.0623` n `23`; metal avg `-0.8683` n `20`; unknown avg `-0.2832` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
