# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T21:36:36.937405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.046` n `12`; crypto_alt avg `0.0505` n `228`; crypto_major avg `0.1716` n `8`; equity avg `0.0258` n `88`; fx avg `-0.0041` n `6`; index avg `0.0031` n `23`; metal avg `0.0244` n `20`; unknown avg `-0.0786` n `764`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.3814` n `228`; crypto_major avg `-0.0729` n `8`; equity avg `0.0509` n `88`; fx avg `-0.0118` n `6`; index avg `0.0327` n `23`; metal avg `0.0169` n `20`; unknown avg `-0.7438` n `764`
- 4h: commodity avg `-0.2482` n `12`; crypto_alt avg `-0.3524` n `228`; crypto_major avg `-0.1187` n `8`; equity avg `0.1932` n `88`; fx avg `-0.0641` n `6`; index avg `0.0797` n `23`; metal avg `0.0611` n `20`; unknown avg `0.5624` n `764`
- 24h: commodity avg `-0.0207` n `12`; crypto_alt avg `-0.512` n `228`; crypto_major avg `-0.8295` n `8`; equity avg `0.2222` n `88`; fx avg `-0.087` n `6`; index avg `0.0276` n `23`; metal avg `0.0329` n `20`; unknown avg `15.1235` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
