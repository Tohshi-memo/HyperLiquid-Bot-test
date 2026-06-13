# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T13:37:33.492898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.1234` n `228`; crypto_major avg `-0.0081` n `8`; equity avg `0.0738` n `74`; fx avg `-0.007` n `6`; index avg `0.0393` n `23`; metal avg `-0.0569` n `18`; unknown avg `-0.0764` n `644`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `0.0773` n `228`; crypto_major avg `0.2215` n `8`; equity avg `0.1645` n `74`; fx avg `-0.0258` n `6`; index avg `0.1263` n `23`; metal avg `0.0907` n `18`; unknown avg `-0.0261` n `644`
- 4h: commodity avg `-0.4047` n `12`; crypto_alt avg `0.4123` n `228`; crypto_major avg `0.8063` n `8`; equity avg `0.2719` n `74`; fx avg `0.0176` n `6`; index avg `0.2732` n `23`; metal avg `0.2022` n `18`; unknown avg `0.1591` n `643`
- 24h: commodity avg `-0.9454` n `12`; crypto_alt avg `1.7108` n `228`; crypto_major avg `0.9299` n `8`; equity avg `0.6311` n `74`; fx avg `0.0162` n `6`; index avg `1.0986` n `23`; metal avg `0.8589` n `18`; unknown avg `27.3283` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
