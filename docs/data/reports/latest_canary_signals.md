# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T03:52:27.904195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0663` n `12`; crypto_alt avg `0.1633` n `230`; crypto_major avg `0.1733` n `8`; equity avg `0.0761` n `93`; fx avg `0.0045` n `6`; index avg `0.0332` n `25`; metal avg `-0.0227` n `20`; unknown avg `0.2228` n `767`
- 1h: commodity avg `-0.1116` n `12`; crypto_alt avg `0.417` n `230`; crypto_major avg `0.5824` n `8`; equity avg `0.1975` n `93`; fx avg `0.0205` n `6`; index avg `0.0703` n `25`; metal avg `-0.0436` n `20`; unknown avg `0.1941` n `767`
- 4h: commodity avg `0.0413` n `12`; crypto_alt avg `0.0643` n `230`; crypto_major avg `0.0836` n `8`; equity avg `1.101` n `93`; fx avg `0.0767` n `6`; index avg `0.1271` n `25`; metal avg `-0.066` n `20`; unknown avg `-0.4951` n `767`
- 24h: commodity avg `0.0948` n `12`; crypto_alt avg `2.1661` n `230`; crypto_major avg `3.5478` n `8`; equity avg `3.0005` n `92`; fx avg `0.158` n `6`; index avg `0.7937` n `25`; metal avg `0.4193` n `20`; unknown avg `0.299` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
