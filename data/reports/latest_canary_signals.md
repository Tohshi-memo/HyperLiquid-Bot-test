# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T05:22:29.905533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.7283` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `-0.2824` n `228`; crypto_major avg `-0.2787` n `8`; equity avg `-0.0826` n `88`; fx avg `-0.0109` n `6`; index avg `-0.0445` n `23`; metal avg `0.0053` n `20`; unknown avg `-0.1335` n `765`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `-0.1149` n `228`; crypto_major avg `-0.0996` n `8`; equity avg `-0.0091` n `88`; fx avg `-0.0495` n `6`; index avg `-0.0096` n `23`; metal avg `-0.0296` n `20`; unknown avg `-0.2855` n `765`
- 4h: commodity avg `0.0233` n `12`; crypto_alt avg `1.9521` n `228`; crypto_major avg `1.4987` n `8`; equity avg `0.1106` n `88`; fx avg `-0.0555` n `6`; index avg `-0.0334` n `23`; metal avg `-0.2296` n `20`; unknown avg `2.1599` n `763`
- 24h: commodity avg `0.1425` n `12`; crypto_alt avg `-0.1175` n `228`; crypto_major avg `0.1453` n `8`; equity avg `0.3366` n `88`; fx avg `0.1372` n `6`; index avg `-0.0934` n `23`; metal avg `-0.1915` n `20`; unknown avg `-0.732` n `733`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
