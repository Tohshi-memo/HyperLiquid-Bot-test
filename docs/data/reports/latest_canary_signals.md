# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T19:02:54.542420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.0165` n `230`; crypto_major avg `-0.0069` n `8`; equity avg `-0.0645` n `120`; fx avg `0.009` n `6`; index avg `0.0001` n `25`; metal avg `0.0044` n `20`; unknown avg `0.0094` n `789`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `0.0278` n `230`; crypto_major avg `0.1367` n `8`; equity avg `0.1197` n `120`; fx avg `0.0006` n `6`; index avg `0.0219` n `25`; metal avg `0.0237` n `20`; unknown avg `0.0402` n `789`
- 4h: commodity avg `0.0991` n `12`; crypto_alt avg `0.0045` n `230`; crypto_major avg `0.0457` n `8`; equity avg `-0.1698` n `120`; fx avg `-0.0043` n `6`; index avg `-0.0279` n `25`; metal avg `-0.098` n `20`; unknown avg `3.6222` n `789`
- 24h: commodity avg `0.334` n `12`; crypto_alt avg `-0.505` n `230`; crypto_major avg `0.3539` n `8`; equity avg `-4.4152` n `120`; fx avg `-0.047` n `6`; index avg `-0.6757` n `25`; metal avg `-0.6201` n `20`; unknown avg `-0.175` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
