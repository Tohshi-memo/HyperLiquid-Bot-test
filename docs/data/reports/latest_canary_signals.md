# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T07:01:52.861857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0707` n `230`; crypto_major avg `0.0491` n `8`; equity avg `0.3164` n `120`; fx avg `-0.0024` n `6`; index avg `0.0323` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0148` n `789`
- 1h: commodity avg `-0.0362` n `12`; crypto_alt avg `0.3504` n `230`; crypto_major avg `0.2887` n `8`; equity avg `0.9851` n `120`; fx avg `0.0333` n `6`; index avg `0.1916` n `25`; metal avg `0.1118` n `20`; unknown avg `0.0508` n `789`
- 4h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.3683` n `230`; crypto_major avg `0.2495` n `8`; equity avg `0.1831` n `120`; fx avg `-0.0024` n `6`; index avg `0.09` n `25`; metal avg `-0.0204` n `20`; unknown avg `-0.1012` n `757`
- 24h: commodity avg `0.3118` n `12`; crypto_alt avg `0.4177` n `230`; crypto_major avg `0.0093` n `8`; equity avg `-2.8533` n `120`; fx avg `-0.1402` n `6`; index avg `-0.3728` n `25`; metal avg `-0.6308` n `20`; unknown avg `-0.2783` n `756`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
