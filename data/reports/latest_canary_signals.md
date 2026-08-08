# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T08:52:27.430155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.0509` n `230`; crypto_major avg `0.0596` n `8`; equity avg `0.027` n `112`; fx avg `-0.0109` n `6`; index avg `0.0082` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.0734` n `784`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `0.1001` n `230`; crypto_major avg `0.1273` n `8`; equity avg `0.0578` n `112`; fx avg `0.0007` n `6`; index avg `0.0124` n `25`; metal avg `-0.013` n `20`; unknown avg `0.1024` n `784`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `0.188` n `230`; crypto_major avg `0.1519` n `8`; equity avg `0.0082` n `112`; fx avg `-0.0022` n `6`; index avg `-0.0102` n `25`; metal avg `0.0065` n `20`; unknown avg `0.1277` n `751`
- 24h: commodity avg `-0.1784` n `12`; crypto_alt avg `-0.011` n `230`; crypto_major avg `0.4162` n `8`; equity avg `0.749` n `112`; fx avg `-0.0438` n `6`; index avg `0.0548` n `25`; metal avg `-0.1117` n `20`; unknown avg `0.1174` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
