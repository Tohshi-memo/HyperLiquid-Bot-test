# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T08:52:33.778773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.1656` n `228`; crypto_major avg `-0.0916` n `8`; equity avg `-0.0246` n `74`; fx avg `-0.0484` n `6`; index avg `-0.0248` n `23`; metal avg `-0.012` n `18`; unknown avg `-0.1436` n `643`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.0988` n `228`; crypto_major avg `0.0509` n `8`; equity avg `-0.0018` n `74`; fx avg `-0.0576` n `6`; index avg `0.021` n `23`; metal avg `0.0041` n `18`; unknown avg `-0.2475` n `643`
- 4h: commodity avg `-0.1149` n `12`; crypto_alt avg `0.7479` n `228`; crypto_major avg `0.5777` n `8`; equity avg `0.1521` n `74`; fx avg `-0.0597` n `6`; index avg `0.0329` n `23`; metal avg `0.083` n `18`; unknown avg `-0.1945` n `627`
- 24h: commodity avg `0.4024` n `12`; crypto_alt avg `1.0312` n `228`; crypto_major avg `0.3865` n `8`; equity avg `-0.3648` n `74`; fx avg `-0.0242` n `6`; index avg `0.7976` n `23`; metal avg `0.3216` n `18`; unknown avg `27.7257` n `619`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
