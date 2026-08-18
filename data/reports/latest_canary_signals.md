# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T18:23:02.424778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `0.0291` n `230`; crypto_major avg `0.1047` n `8`; equity avg `0.1477` n `120`; fx avg `-0.0006` n `6`; index avg `0.0355` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.0952` n `789`
- 1h: commodity avg `0.024` n `12`; crypto_alt avg `-0.095` n `230`; crypto_major avg `0.0765` n `8`; equity avg `-0.2462` n `120`; fx avg `0.014` n `6`; index avg `-0.0149` n `25`; metal avg `-0.0822` n `20`; unknown avg `-0.088` n `789`
- 4h: commodity avg `0.1687` n `12`; crypto_alt avg `0.072` n `230`; crypto_major avg `0.1906` n `8`; equity avg `-0.998` n `120`; fx avg `0.0021` n `6`; index avg `-0.1339` n `25`; metal avg `-0.3051` n `20`; unknown avg `2.0223` n `789`
- 24h: commodity avg `0.2669` n `12`; crypto_alt avg `-0.5064` n `230`; crypto_major avg `0.1623` n `8`; equity avg `-4.4924` n `120`; fx avg `-0.0432` n `6`; index avg `-0.6898` n `25`; metal avg `-0.6908` n `20`; unknown avg `-0.2728` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
