# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T06:07:32.396315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0702` n `12`; crypto_alt avg `-0.1252` n `230`; crypto_major avg `-0.0994` n `8`; equity avg `-0.3836` n `102`; fx avg `0.0116` n `6`; index avg `-0.086` n `25`; metal avg `0.0136` n `20`; unknown avg `0.0086` n `761`
- 1h: commodity avg `0.1` n `12`; crypto_alt avg `0.0581` n `230`; crypto_major avg `0.1409` n `8`; equity avg `0.0044` n `102`; fx avg `0.0563` n `6`; index avg `0.0175` n `25`; metal avg `0.0931` n `20`; unknown avg `0.0871` n `761`
- 4h: commodity avg `-0.0657` n `12`; crypto_alt avg `-0.7524` n `230`; crypto_major avg `0.3253` n `8`; equity avg `-0.43` n `102`; fx avg `-0.0563` n `6`; index avg `-0.2222` n `25`; metal avg `0.1066` n `20`; unknown avg `0.1007` n `761`
- 24h: commodity avg `-0.2064` n `12`; crypto_alt avg `-1.3265` n `230`; crypto_major avg `0.9876` n `8`; equity avg `-1.957` n `102`; fx avg `-0.1107` n `6`; index avg `-0.4184` n `25`; metal avg `0.0207` n `20`; unknown avg `0.6643` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
