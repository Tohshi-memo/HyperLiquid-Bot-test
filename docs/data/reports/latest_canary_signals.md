# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T13:52:14.321607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.0282` n `228`; crypto_major avg `-0.0193` n `8`; equity avg `-0.0547` n `65`; fx avg `0.0` n `5`; index avg `0.0745` n `23`; metal avg `0.0485` n `18`; unknown avg `-0.0217` n `383`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `-0.1147` n `228`; crypto_major avg `-0.3377` n `8`; equity avg `-0.0978` n `65`; fx avg `-0.0009` n `5`; index avg `0.0453` n `23`; metal avg `0.0254` n `18`; unknown avg `-0.1292` n `383`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `-0.38` n `228`; crypto_major avg `-0.0062` n `8`; equity avg `0.1395` n `65`; fx avg `-0.0167` n `5`; index avg `0.1395` n `23`; metal avg `0.0226` n `18`; unknown avg `-0.2394` n `383`
- 24h: commodity avg `1.798` n `12`; crypto_alt avg `-9.135` n `228`; crypto_major avg `-2.4168` n `8`; equity avg `-2.6234` n `65`; fx avg `-0.1861` n `5`; index avg `-1.6007` n `23`; metal avg `-5.8179` n `18`; unknown avg `550.0519` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
