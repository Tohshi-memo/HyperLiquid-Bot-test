# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T08:37:27.025091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.1458` n `228`; crypto_major avg `0.1366` n `8`; equity avg `0.0407` n `74`; fx avg `-0.0169` n `6`; index avg `0.0308` n `23`; metal avg `0.002` n `18`; unknown avg `13.0446` n `643`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `0.1297` n `228`; crypto_major avg `0.2055` n `8`; equity avg `0.0548` n `74`; fx avg `-0.0124` n `6`; index avg `0.0251` n `23`; metal avg `0.0365` n `18`; unknown avg `7.3545` n `643`
- 4h: commodity avg `-0.1349` n `12`; crypto_alt avg `0.9069` n `228`; crypto_major avg `0.6269` n `8`; equity avg `0.1819` n `74`; fx avg `-0.0107` n `6`; index avg `0.0655` n `23`; metal avg `0.1216` n `18`; unknown avg `3.4845` n `619`
- 24h: commodity avg `0.4443` n `12`; crypto_alt avg `1.2491` n `228`; crypto_major avg `0.5869` n `8`; equity avg `-0.297` n `74`; fx avg `0.0247` n `6`; index avg `0.8528` n `23`; metal avg `0.2618` n `18`; unknown avg `27.8763` n `619`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
