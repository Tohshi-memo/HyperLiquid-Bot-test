# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T14:37:15.846440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1424` n `12`; crypto_alt avg `0.2125` n `228`; crypto_major avg `0.089` n `8`; equity avg `0.0878` n `65`; fx avg `0.0215` n `5`; index avg `-0.0156` n `23`; metal avg `-0.0316` n `18`; unknown avg `0.0203` n `383`
- 1h: commodity avg `-0.1069` n `12`; crypto_alt avg `-0.2898` n `228`; crypto_major avg `-0.265` n `8`; equity avg `-0.0574` n `65`; fx avg `0.0215` n `5`; index avg `0.0253` n `23`; metal avg `-0.0015` n `18`; unknown avg `0.0635` n `383`
- 4h: commodity avg `-0.0404` n `12`; crypto_alt avg `-0.8553` n `228`; crypto_major avg `-0.6291` n `8`; equity avg `0.0253` n `65`; fx avg `0.004` n `5`; index avg `0.0209` n `23`; metal avg `-0.0356` n `18`; unknown avg `-0.1329` n `383`
- 24h: commodity avg `1.7115` n `12`; crypto_alt avg `-9.4123` n `228`; crypto_major avg `-2.6494` n `8`; equity avg `-2.6186` n `65`; fx avg `-0.1649` n `5`; index avg `-1.6489` n `23`; metal avg `-5.8644` n `18`; unknown avg `549.9671` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
