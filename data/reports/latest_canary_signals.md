# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T21:07:13.379135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `0.0064` n `228`; crypto_major avg `0.0698` n `8`; equity avg `0.0619` n `65`; fx avg `0.0` n `5`; index avg `-0.0305` n `23`; metal avg `0.009` n `18`; unknown avg `-0.0275` n `376`
- 1h: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0149` n `228`; crypto_major avg `0.0067` n `8`; equity avg `0.11` n `65`; fx avg `0.0281` n `5`; index avg `0.0078` n `23`; metal avg `0.0436` n `18`; unknown avg `-0.062` n `376`
- 4h: commodity avg `-0.0187` n `12`; crypto_alt avg `0.1702` n `228`; crypto_major avg `0.0602` n `8`; equity avg `0.3156` n `65`; fx avg `0.0172` n `5`; index avg `0.0433` n `23`; metal avg `0.1379` n `18`; unknown avg `0.0012` n `376`
- 24h: commodity avg `0.2514` n `12`; crypto_alt avg `0.4835` n `228`; crypto_major avg `0.5756` n `8`; equity avg `0.9015` n `65`; fx avg `-0.0248` n `5`; index avg `0.4371` n `23`; metal avg `0.037` n `18`; unknown avg `0.1618` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
