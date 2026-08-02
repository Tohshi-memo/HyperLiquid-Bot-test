# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T10:07:29.786556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0529` n `12`; crypto_alt avg `-0.0274` n `230`; crypto_major avg `-0.0233` n `8`; equity avg `-0.0039` n `102`; fx avg `0.012` n `6`; index avg `0.0053` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0104` n `782`
- 1h: commodity avg `0.0678` n `12`; crypto_alt avg `0.1093` n `230`; crypto_major avg `0.1332` n `8`; equity avg `0.101` n `102`; fx avg `0.0277` n `6`; index avg `-0.006` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0961` n `782`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0626` n `230`; crypto_major avg `-0.3054` n `8`; equity avg `0.0971` n `102`; fx avg `-0.0214` n `6`; index avg `0.0081` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0346` n `782`
- 24h: commodity avg `-1.1127` n `12`; crypto_alt avg `0.6974` n `230`; crypto_major avg `0.4803` n `8`; equity avg `1.011` n `102`; fx avg `-0.1559` n `6`; index avg `0.2429` n `25`; metal avg `0.2583` n `20`; unknown avg `0.3055` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
