# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T18:07:40.674706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.34` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.2357` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `-0.018` n `228`; crypto_major avg `0.0218` n `8`; equity avg `-0.1308` n `77`; fx avg `0.0007` n `6`; index avg `-0.0747` n `23`; metal avg `-0.026` n `18`; unknown avg `-0.0888` n `687`
- 1h: commodity avg `0.0702` n `12`; crypto_alt avg `0.2572` n `228`; crypto_major avg `0.0504` n `8`; equity avg `0.046` n `77`; fx avg `-0.0015` n `6`; index avg `-0.0438` n `23`; metal avg `-0.177` n `18`; unknown avg `1.6091` n `687`
- 4h: commodity avg `0.4081` n `12`; crypto_alt avg `0.1249` n `228`; crypto_major avg `1.1416` n `8`; equity avg `0.9759` n `77`; fx avg `-0.0161` n `6`; index avg `0.1416` n `23`; metal avg `-1.0941` n `18`; unknown avg `4.9989` n `687`
- 24h: commodity avg `-0.6122` n `12`; crypto_alt avg `6.3605` n `228`; crypto_major avg `7.5499` n `8`; equity avg `3.0843` n `76`; fx avg `0.0587` n `6`; index avg `1.2458` n `23`; metal avg `2.0597` n `18`; unknown avg `7.0935` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
