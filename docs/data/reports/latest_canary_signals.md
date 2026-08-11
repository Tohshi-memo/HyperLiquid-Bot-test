# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T22:22:27.966949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.0267` n `230`; crypto_major avg `-0.0401` n `8`; equity avg `0.0498` n `113`; fx avg `0.004` n `6`; index avg `0.0053` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0314` n `786`
- 1h: commodity avg `0.0765` n `12`; crypto_alt avg `0.2007` n `230`; crypto_major avg `0.261` n `8`; equity avg `-0.0257` n `113`; fx avg `0.0083` n `6`; index avg `-0.0066` n `25`; metal avg `0.0469` n `20`; unknown avg `0.0516` n `786`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `0.4935` n `230`; crypto_major avg `0.879` n `8`; equity avg `0.6694` n `113`; fx avg `0.0069` n `6`; index avg `0.0428` n `25`; metal avg `0.1122` n `20`; unknown avg `0.3979` n `785`
- 24h: commodity avg `0.1701` n `12`; crypto_alt avg `-1.076` n `230`; crypto_major avg `0.8035` n `8`; equity avg `1.2264` n `113`; fx avg `-0.059` n `6`; index avg `0.1129` n `25`; metal avg `-0.1894` n `20`; unknown avg `-0.1138` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2218`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
