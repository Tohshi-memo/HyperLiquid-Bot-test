# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T21:07:31.971511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.0699` n `230`; crypto_major avg `0.085` n `8`; equity avg `-0.0052` n `102`; fx avg `0.0201` n `6`; index avg `0.0086` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.0084` n `783`
- 1h: commodity avg `0.076` n `12`; crypto_alt avg `0.0738` n `230`; crypto_major avg `0.0792` n `8`; equity avg `0.0228` n `102`; fx avg `0.0218` n `6`; index avg `-0.0075` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.008` n `783`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `0.2376` n `230`; crypto_major avg `0.5519` n `8`; equity avg `0.2078` n `102`; fx avg `0.1172` n `6`; index avg `0.0183` n `25`; metal avg `0.0687` n `20`; unknown avg `0.0865` n `782`
- 24h: commodity avg `-1.1745` n `12`; crypto_alt avg `1.4405` n `230`; crypto_major avg `1.8391` n `8`; equity avg `1.7125` n `102`; fx avg `-0.0188` n `6`; index avg `0.3443` n `25`; metal avg `0.349` n `20`; unknown avg `1.6274` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
