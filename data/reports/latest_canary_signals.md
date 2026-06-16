# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T13:22:38.377411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `12`; crypto_alt avg `-0.741` n `228`; crypto_major avg `-0.5132` n `8`; equity avg `0.0753` n `77`; fx avg `-0.0024` n `6`; index avg `0.0239` n `23`; metal avg `-0.1896` n `18`; unknown avg `0.0801` n `687`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `-1.0187` n `228`; crypto_major avg `-0.7571` n `8`; equity avg `-0.2711` n `77`; fx avg `0.0087` n `6`; index avg `-0.0565` n `23`; metal avg `0.082` n `18`; unknown avg `0.334` n `687`
- 4h: commodity avg `-0.2377` n `12`; crypto_alt avg `-0.7888` n `228`; crypto_major avg `-0.1143` n `8`; equity avg `-0.6389` n `77`; fx avg `-0.0129` n `6`; index avg `-0.1027` n `23`; metal avg `0.0974` n `18`; unknown avg `0.5988` n `687`
- 24h: commodity avg `-0.4667` n `12`; crypto_alt avg `-1.7089` n `228`; crypto_major avg `0.2317` n `8`; equity avg `1.089` n `76`; fx avg `-0.0779` n `6`; index avg `0.2415` n `23`; metal avg `-0.3322` n `18`; unknown avg `0.7697` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
