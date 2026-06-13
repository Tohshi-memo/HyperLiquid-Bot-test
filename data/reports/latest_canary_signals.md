# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T19:07:31.123265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0813` n `12`; crypto_alt avg `0.0008` n `228`; crypto_major avg `0.0656` n `8`; equity avg `0.0044` n `74`; fx avg `-0.0102` n `6`; index avg `0.0079` n `23`; metal avg `0.0175` n `18`; unknown avg `-0.0197` n `644`
- 1h: commodity avg `0.1167` n `12`; crypto_alt avg `-0.2283` n `228`; crypto_major avg `0.1291` n `8`; equity avg `0.0768` n `74`; fx avg `0.0259` n `6`; index avg `0.0574` n `23`; metal avg `-0.0451` n `18`; unknown avg `-0.1157` n `644`
- 4h: commodity avg `-0.122` n `12`; crypto_alt avg `-0.3145` n `228`; crypto_major avg `-0.3567` n `8`; equity avg `0.0307` n `74`; fx avg `0.0276` n `6`; index avg `-0.0271` n `23`; metal avg `-0.0209` n `18`; unknown avg `-2.2095` n `644`
- 24h: commodity avg `-0.7507` n `12`; crypto_alt avg `1.7726` n `228`; crypto_major avg `0.2828` n `8`; equity avg `0.1655` n `74`; fx avg `0.035` n `6`; index avg `0.4686` n `23`; metal avg `0.2918` n `18`; unknown avg `-1.7386` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
