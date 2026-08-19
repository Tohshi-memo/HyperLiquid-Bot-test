# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T11:45:26.598096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.0617` n `230`; crypto_major avg `-0.0158` n `8`; equity avg `-0.0834` n `120`; fx avg `0.0011` n `6`; index avg `0.0022` n `25`; metal avg `-0.0384` n `20`; unknown avg `0.0112` n `792`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `0.158` n `230`; crypto_major avg `0.1799` n `8`; equity avg `-0.2428` n `120`; fx avg `0.0073` n `6`; index avg `-0.0139` n `25`; metal avg `-0.01` n `20`; unknown avg `0.1985` n `791`
- 4h: commodity avg `0.1384` n `12`; crypto_alt avg `0.2007` n `230`; crypto_major avg `0.3201` n `8`; equity avg `-0.6999` n `120`; fx avg `-0.0611` n `6`; index avg `-0.0186` n `25`; metal avg `0.0821` n `20`; unknown avg `0.0924` n `789`
- 24h: commodity avg `0.3719` n `12`; crypto_alt avg `0.2881` n `230`; crypto_major avg `0.2678` n `8`; equity avg `-2.3021` n `120`; fx avg `-0.2039` n `6`; index avg `-0.2573` n `25`; metal avg `-0.4272` n `20`; unknown avg `-0.2517` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
