# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T16:37:33.720633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0667` n `230`; crypto_major avg `-0.0906` n `8`; equity avg `0.3667` n `102`; fx avg `0.013` n `6`; index avg `0.0466` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.145` n `780`
- 1h: commodity avg `-0.0904` n `12`; crypto_alt avg `0.0241` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `0.3542` n `102`; fx avg `0.0117` n `6`; index avg `0.0974` n `25`; metal avg `-0.0086` n `20`; unknown avg `-0.2655` n `780`
- 4h: commodity avg `-0.2258` n `12`; crypto_alt avg `0.1077` n `230`; crypto_major avg `-0.7604` n `8`; equity avg `-1.6153` n `102`; fx avg `-0.0559` n `6`; index avg `-0.1479` n `25`; metal avg `-0.039` n `20`; unknown avg `0.3411` n `780`
- 24h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.5406` n `230`; crypto_major avg `-1.8438` n `8`; equity avg `0.5172` n `102`; fx avg `0.1415` n `6`; index avg `0.2893` n `25`; metal avg `-0.3482` n `20`; unknown avg `0.6207` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
