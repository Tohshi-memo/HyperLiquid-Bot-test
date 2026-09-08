# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T09:22:26.448350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `0.1083` n `232`; crypto_major avg `-0.0039` n `8`; equity avg `0.1049` n `134`; fx avg `-0.0003` n `6`; index avg `0.0196` n `26`; metal avg `0.0142` n `20`; unknown avg `0.4271` n `797`
- 1h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.4953` n `232`; crypto_major avg `0.12` n `8`; equity avg `0.2423` n `134`; fx avg `0.0175` n `6`; index avg `0.0494` n `26`; metal avg `0.0386` n `20`; unknown avg `1.802` n `787`
- 4h: commodity avg `0.2267` n `12`; crypto_alt avg `-0.107` n `232`; crypto_major avg `-0.1929` n `8`; equity avg `-0.9823` n `134`; fx avg `0.0811` n `6`; index avg `-0.2355` n `26`; metal avg `-0.2316` n `20`; unknown avg `0.9206` n `755`
- 24h: commodity avg `0.5103` n `12`; crypto_alt avg `0.2723` n `232`; crypto_major avg `-1.1124` n `8`; equity avg `-0.4906` n `134`; fx avg `-0.0668` n `6`; index avg `-0.1235` n `26`; metal avg `0.0112` n `20`; unknown avg `7462.974` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
