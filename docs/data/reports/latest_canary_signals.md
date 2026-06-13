# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T11:52:37.738679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.0871` n `228`; crypto_major avg `-0.0037` n `8`; equity avg `-0.0328` n `74`; fx avg `-0.0039` n `6`; index avg `0.0015` n `23`; metal avg `0.242` n `18`; unknown avg `-0.0206` n `644`
- 1h: commodity avg `-0.1245` n `12`; crypto_alt avg `0.346` n `228`; crypto_major avg `0.2278` n `8`; equity avg `-0.0061` n `74`; fx avg `-0.0048` n `6`; index avg `0.1331` n `23`; metal avg `0.0274` n `18`; unknown avg `0.3833` n `644`
- 4h: commodity avg `-0.2488` n `12`; crypto_alt avg `0.3439` n `228`; crypto_major avg `0.2437` n `8`; equity avg `-0.0792` n `74`; fx avg `-0.0018` n `6`; index avg `0.1113` n `23`; metal avg `0.0938` n `18`; unknown avg `0.4273` n `635`
- 24h: commodity avg `-0.2904` n `12`; crypto_alt avg `1.0889` n `228`; crypto_major avg `0.1815` n `8`; equity avg `-0.9167` n `74`; fx avg `0.0177` n `6`; index avg `0.5881` n `23`; metal avg `0.375` n `18`; unknown avg `30.4672` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
