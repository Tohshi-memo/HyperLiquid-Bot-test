# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T18:37:42.231293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.61` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.7528` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0825` n `12`; crypto_alt avg `-0.186` n `228`; crypto_major avg `0.0051` n `8`; equity avg `-0.0512` n `77`; fx avg `-0.0042` n `6`; index avg `-0.0334` n `23`; metal avg `-0.0503` n `18`; unknown avg `0.0918` n `687`
- 1h: commodity avg `0.1963` n `12`; crypto_alt avg `-0.2625` n `228`; crypto_major avg `0.0304` n `8`; equity avg `-0.0907` n `77`; fx avg `-0.0031` n `6`; index avg `-0.0708` n `23`; metal avg `0.0406` n `18`; unknown avg `-0.023` n `687`
- 4h: commodity avg `0.4978` n `12`; crypto_alt avg `-0.4079` n `228`; crypto_major avg `1.0816` n `8`; equity avg `0.8779` n `77`; fx avg `0.0058` n `6`; index avg `0.263` n `23`; metal avg `-0.6712` n `18`; unknown avg `4.6568` n `687`
- 24h: commodity avg `-0.6088` n `12`; crypto_alt avg `6.0062` n `228`; crypto_major avg `7.5711` n `8`; equity avg `3.1202` n `76`; fx avg `0.0528` n `6`; index avg `1.2795` n `23`; metal avg `2.1727` n `18`; unknown avg `5.5867` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
