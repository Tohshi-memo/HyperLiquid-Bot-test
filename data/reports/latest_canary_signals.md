# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T12:22:36.323889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `0.1145` n `230`; crypto_major avg `-0.1701` n `8`; equity avg `-0.072` n `121`; fx avg `0.0072` n `6`; index avg `-0.0043` n `25`; metal avg `-0.062` n `20`; unknown avg `0.0027` n `793`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.1411` n `230`; crypto_major avg `-0.8955` n `8`; equity avg `-0.136` n `121`; fx avg `0.0186` n `6`; index avg `0.0073` n `25`; metal avg `-0.0931` n `20`; unknown avg `0.0422` n `793`
- 4h: commodity avg `0.1235` n `12`; crypto_alt avg `1.3712` n `230`; crypto_major avg `-0.3035` n `8`; equity avg `0.3618` n `121`; fx avg `0.0458` n `6`; index avg `0.0583` n `25`; metal avg `-0.0094` n `20`; unknown avg `0.4478` n `793`
- 24h: commodity avg `0.0474` n `12`; crypto_alt avg `7.5173` n `230`; crypto_major avg `5.8966` n `8`; equity avg `1.7348` n `121`; fx avg `-0.0804` n `6`; index avg `0.247` n `25`; metal avg `1.0276` n `20`; unknown avg `2.3992` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
