# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T17:37:28.787240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.1059` n `230`; crypto_major avg `0.026` n `8`; equity avg `-0.0443` n `94`; fx avg `-0.0078` n `6`; index avg `0.0332` n `25`; metal avg `-0.056` n `20`; unknown avg `0.3605` n `768`
- 1h: commodity avg `-0.073` n `12`; crypto_alt avg `-0.3988` n `230`; crypto_major avg `-0.7143` n `8`; equity avg `-0.2352` n `94`; fx avg `0.0031` n `6`; index avg `-0.0323` n `25`; metal avg `-0.1539` n `20`; unknown avg `0.084` n `768`
- 4h: commodity avg `-0.4842` n `12`; crypto_alt avg `-0.3611` n `230`; crypto_major avg `-1.0112` n `8`; equity avg `-1.5634` n `94`; fx avg `-0.0651` n `6`; index avg `-0.1242` n `25`; metal avg `-0.2211` n `20`; unknown avg `-0.2283` n `768`
- 24h: commodity avg `-0.2106` n `12`; crypto_alt avg `-0.7728` n `230`; crypto_major avg `-2.0303` n `8`; equity avg `-3.2857` n `94`; fx avg `-0.1637` n `6`; index avg `-0.3743` n `25`; metal avg `-0.582` n `20`; unknown avg `-0.2837` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
