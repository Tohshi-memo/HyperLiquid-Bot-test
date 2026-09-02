# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T18:52:28.608494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `0.0137` n `232`; crypto_major avg `0.0101` n `8`; equity avg `-0.0049` n `133`; fx avg `0.0076` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.2997` n `792`
- 1h: commodity avg `0.0552` n `12`; crypto_alt avg `0.0465` n `232`; crypto_major avg `-0.012` n `8`; equity avg `0.3403` n `133`; fx avg `0.0097` n `6`; index avg `-0.0043` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.4422` n `790`
- 4h: commodity avg `0.0678` n `12`; crypto_alt avg `0.1979` n `232`; crypto_major avg `0.0644` n `8`; equity avg `0.6542` n `133`; fx avg `-0.0042` n `6`; index avg `0.0408` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.6387` n `789`
- 24h: commodity avg `0.2049` n `12`; crypto_alt avg `0.1218` n `232`; crypto_major avg `-0.0347` n `8`; equity avg `0.8741` n `133`; fx avg `-0.3548` n `6`; index avg `0.172` n `26`; metal avg `0.4123` n `20`; unknown avg `-0.1702` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0429`, n `668`, weak_sample_signal
