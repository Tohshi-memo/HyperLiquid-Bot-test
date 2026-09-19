# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T08:07:26.326386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.231` n `234`; crypto_major avg `0.1271` n `8`; equity avg `-0.0077` n `140`; fx avg `0.0006` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.0075` n `934`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `0.1489` n `234`; crypto_major avg `-0.0444` n `8`; equity avg `0.0024` n `140`; fx avg `-0.0157` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.0148` n `934`
- 4h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.7729` n `234`; crypto_major avg `-0.3912` n `8`; equity avg `-0.0947` n `140`; fx avg `0.0013` n `6`; index avg `-0.03` n `26`; metal avg `-0.0178` n `20`; unknown avg `0.288` n `898`
- 24h: commodity avg `0.2906` n `12`; crypto_alt avg `3.0254` n `234`; crypto_major avg `3.981` n `8`; equity avg `0.0893` n `140`; fx avg `-0.0128` n `6`; index avg `-0.1027` n `26`; metal avg `-0.2746` n `20`; unknown avg `2.1678` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
