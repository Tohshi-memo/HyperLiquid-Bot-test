# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T01:07:31.512729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `0.3939` n `228`; crypto_major avg `0.3968` n `8`; equity avg `0.282` n `88`; fx avg `-0.0024` n `6`; index avg `0.084` n `23`; metal avg `0.0968` n `20`; unknown avg `0.1116` n `764`
- 1h: commodity avg `0.1215` n `12`; crypto_alt avg `0.5342` n `228`; crypto_major avg `0.5678` n `8`; equity avg `-0.1969` n `88`; fx avg `0.0209` n `6`; index avg `-0.0326` n `23`; metal avg `0.1107` n `20`; unknown avg `0.199` n `764`
- 4h: commodity avg `-0.1443` n `12`; crypto_alt avg `0.1005` n `228`; crypto_major avg `0.1221` n `8`; equity avg `-0.3571` n `88`; fx avg `0.0211` n `6`; index avg `-0.1326` n `23`; metal avg `-0.1388` n `20`; unknown avg `1.762` n `762`
- 24h: commodity avg `-0.448` n `12`; crypto_alt avg `-0.0721` n `228`; crypto_major avg `-0.1935` n `8`; equity avg `0.0382` n `88`; fx avg `-0.0295` n `6`; index avg `-0.0128` n `23`; metal avg `-0.1346` n `20`; unknown avg `15.7211` n `690`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
