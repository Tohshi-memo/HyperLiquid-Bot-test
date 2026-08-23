# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T09:37:32.371191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-0.1023` n `230`; crypto_major avg `-0.0281` n `8`; equity avg `0.0268` n `121`; fx avg `-0.0071` n `6`; index avg `0.0004` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0634` n `794`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.3107` n `230`; crypto_major avg `-0.1528` n `8`; equity avg `0.0195` n `121`; fx avg `0.0009` n `6`; index avg `0.0049` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.0649` n `794`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `1.9605` n `230`; crypto_major avg `0.7188` n `8`; equity avg `0.1291` n `121`; fx avg `-0.0284` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0279` n `20`; unknown avg `0.4753` n `778`
- 24h: commodity avg `-0.0273` n `12`; crypto_alt avg `-1.9681` n `230`; crypto_major avg `-0.7335` n `8`; equity avg `0.1745` n `121`; fx avg `0.0539` n `6`; index avg `0.0142` n `25`; metal avg `0.0183` n `20`; unknown avg `2.3797` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
