# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T05:31:49.553306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `-0.0188` n `8`; equity avg `0.0039` n `112`; fx avg `0.0001` n `6`; index avg `0.0056` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.078` n `784`
- 1h: commodity avg `-0.0237` n `12`; crypto_alt avg `-0.049` n `230`; crypto_major avg `-0.0819` n `8`; equity avg `-0.0231` n `112`; fx avg `0.0048` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0192` n `20`; unknown avg `-0.1414` n `783`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.3067` n `230`; crypto_major avg `0.3076` n `8`; equity avg `-0.1062` n `112`; fx avg `-0.0018` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0443` n `20`; unknown avg `-0.0042` n `783`
- 24h: commodity avg `-0.2642` n `12`; crypto_alt avg `0.1479` n `230`; crypto_major avg `0.9791` n `8`; equity avg `1.464` n `112`; fx avg `-0.0666` n `6`; index avg `0.1526` n `25`; metal avg `0.2348` n `20`; unknown avg `0.0393` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
