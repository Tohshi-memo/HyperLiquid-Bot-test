# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T08:22:30.023100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `0.0835` n `8`; equity avg `-0.0076` n `96`; fx avg `-0.0032` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0343` n `769`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.0691` n `230`; crypto_major avg `0.0772` n `8`; equity avg `-0.0314` n `96`; fx avg `0.0008` n `6`; index avg `0.0111` n `25`; metal avg `0.0136` n `20`; unknown avg `-0.0431` n `769`
- 4h: commodity avg `0.0543` n `12`; crypto_alt avg `-0.2224` n `230`; crypto_major avg `-0.0207` n `8`; equity avg `-0.1462` n `96`; fx avg `-0.0002` n `6`; index avg `-0.0158` n `25`; metal avg `0.0145` n `20`; unknown avg `-0.0818` n `737`
- 24h: commodity avg `0.8394` n `12`; crypto_alt avg `0.139` n `230`; crypto_major avg `0.7882` n `8`; equity avg `1.8615` n `96`; fx avg `0.0269` n `6`; index avg `0.2641` n `25`; metal avg `0.3189` n `20`; unknown avg `0.2878` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
