# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T09:07:47.746046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0971` n `12`; crypto_alt avg `0.0046` n `230`; crypto_major avg `0.0611` n `8`; equity avg `0.1125` n `102`; fx avg `-0.0148` n `6`; index avg `-0.0049` n `25`; metal avg `0.0594` n `20`; unknown avg `0.0326` n `771`
- 1h: commodity avg `-0.0163` n `12`; crypto_alt avg `0.2964` n `230`; crypto_major avg `0.4618` n `8`; equity avg `0.5521` n `102`; fx avg `0.0117` n `6`; index avg `0.0829` n `25`; metal avg `0.1596` n `20`; unknown avg `0.0719` n `771`
- 4h: commodity avg `0.0417` n `12`; crypto_alt avg `0.4582` n `230`; crypto_major avg `0.6025` n `8`; equity avg `0.7561` n `102`; fx avg `0.0136` n `6`; index avg `0.0271` n `25`; metal avg `0.3068` n `20`; unknown avg `0.045` n `739`
- 24h: commodity avg `0.7006` n `12`; crypto_alt avg `-0.2523` n `230`; crypto_major avg `-0.278` n `8`; equity avg `-3.2281` n `102`; fx avg `-0.0119` n `6`; index avg `-0.476` n `25`; metal avg `0.2331` n `20`; unknown avg `-0.0783` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
