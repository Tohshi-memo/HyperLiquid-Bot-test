# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T08:07:34.586847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0689` n `12`; crypto_alt avg `-0.0203` n `228`; crypto_major avg `0.0709` n `8`; equity avg `-0.1614` n `79`; fx avg `-0.0228` n `6`; index avg `-0.0305` n `23`; metal avg `-0.0479` n `18`; unknown avg `-0.1106` n `701`
- 1h: commodity avg `0.2178` n `12`; crypto_alt avg `0.156` n `228`; crypto_major avg `0.4137` n `8`; equity avg `-0.1535` n `79`; fx avg `-0.0271` n `6`; index avg `-0.0377` n `23`; metal avg `-0.217` n `18`; unknown avg `-0.0158` n `693`
- 4h: commodity avg `0.248` n `12`; crypto_alt avg `0.3026` n `228`; crypto_major avg `0.8639` n `8`; equity avg `0.1895` n `79`; fx avg `-0.0077` n `6`; index avg `-0.0046` n `23`; metal avg `0.1931` n `18`; unknown avg `0.089` n `661`
- 24h: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.162` n `228`; crypto_major avg `0.1712` n `8`; equity avg `-0.4354` n `79`; fx avg `-0.0069` n `6`; index avg `-0.0281` n `23`; metal avg `0.2825` n `18`; unknown avg `-0.0656` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
