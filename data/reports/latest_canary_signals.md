# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T10:52:27.881216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0017` n `234`; crypto_major avg `-0.1119` n `8`; equity avg `-0.0054` n `140`; fx avg `0.0037` n `6`; index avg `-0.0` n `26`; metal avg `0.012` n `20`; unknown avg `-0.1249` n `942`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `0.2809` n `234`; crypto_major avg `0.0495` n `8`; equity avg `-0.011` n `140`; fx avg `0.0055` n `6`; index avg `-0.0055` n `26`; metal avg `0.0279` n `20`; unknown avg `-0.0887` n `940`
- 4h: commodity avg `0.004` n `12`; crypto_alt avg `1.217` n `234`; crypto_major avg `0.0602` n `8`; equity avg `0.0392` n `140`; fx avg `0.0318` n `6`; index avg `0.0338` n `26`; metal avg `0.0231` n `20`; unknown avg `0.3258` n `934`
- 24h: commodity avg `0.2136` n `12`; crypto_alt avg `3.3158` n `234`; crypto_major avg `3.0665` n `8`; equity avg `0.1927` n `140`; fx avg `-0.0027` n `6`; index avg `-0.0332` n `26`; metal avg `-0.1448` n `20`; unknown avg `2.3599` n `803`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
