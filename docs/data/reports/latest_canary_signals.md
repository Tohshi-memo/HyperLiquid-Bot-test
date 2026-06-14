# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T13:52:34.498661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0493` n `12`; crypto_alt avg `0.0766` n `228`; crypto_major avg `-0.0062` n `8`; equity avg `0.0221` n `74`; fx avg `0.0088` n `6`; index avg `0.006` n `23`; metal avg `-0.0011` n `18`; unknown avg `-0.0534` n `645`
- 1h: commodity avg `0.1247` n `12`; crypto_alt avg `-0.1526` n `228`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0065` n `74`; fx avg `-0.0089` n `6`; index avg `-0.0132` n `23`; metal avg `-0.0368` n `18`; unknown avg `0.173` n `645`
- 4h: commodity avg `0.348` n `12`; crypto_alt avg `-0.824` n `228`; crypto_major avg `-0.446` n `8`; equity avg `-0.1078` n `74`; fx avg `0.0285` n `6`; index avg `0.166` n `23`; metal avg `-0.1338` n `18`; unknown avg `0.5227` n `645`
- 24h: commodity avg `-0.091` n `12`; crypto_alt avg `-0.7798` n `228`; crypto_major avg `-0.0949` n `8`; equity avg `0.6069` n `74`; fx avg `0.0039` n `6`; index avg `0.1585` n `23`; metal avg `0.1326` n `18`; unknown avg `-1.052` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
