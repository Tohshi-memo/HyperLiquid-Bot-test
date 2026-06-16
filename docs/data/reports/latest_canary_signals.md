# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T10:47:15.693190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.043` n `228`; crypto_major avg `0.0071` n `8`; equity avg `-0.0094` n `77`; fx avg `0.0` n `6`; index avg `-0.0182` n `23`; metal avg `0.0376` n `18`; unknown avg `-0.0189` n `687`
- 1h: commodity avg `-0.2826` n `12`; crypto_alt avg `0.2911` n `228`; crypto_major avg `0.4067` n `8`; equity avg `0.0965` n `77`; fx avg `0.0162` n `6`; index avg `0.0355` n `23`; metal avg `0.0158` n `18`; unknown avg `0.1963` n `687`
- 4h: commodity avg `-0.839` n `12`; crypto_alt avg `0.9857` n `228`; crypto_major avg `1.0031` n `8`; equity avg `0.4699` n `77`; fx avg `0.1058` n `6`; index avg `0.1564` n `23`; metal avg `0.9621` n `18`; unknown avg `0.3005` n `687`
- 24h: commodity avg `-0.0421` n `12`; crypto_alt avg `1.3909` n `228`; crypto_major avg `3.2562` n `8`; equity avg `1.8375` n `76`; fx avg `-0.0603` n `6`; index avg `0.4852` n `23`; metal avg `0.2036` n `18`; unknown avg `0.2565` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
