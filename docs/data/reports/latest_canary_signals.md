# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T03:07:31.031338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0535` n `13`; crypto_alt avg `0.0684` n `237`; crypto_major avg `0.0824` n `8`; equity avg `0.0615` n `151`; fx avg `-0.0016` n `6`; index avg `0.0256` n `26`; metal avg `0.0644` n `20`; unknown avg `-0.1498` n `1196`
- 1h: commodity avg `0.0601` n `13`; crypto_alt avg `0.7711` n `237`; crypto_major avg `0.5429` n `8`; equity avg `0.5605` n `151`; fx avg `0.0185` n `6`; index avg `0.0841` n `26`; metal avg `0.1283` n `20`; unknown avg `4.3521` n `1196`
- 4h: commodity avg `0.1206` n `13`; crypto_alt avg `0.2114` n `237`; crypto_major avg `-0.0016` n `8`; equity avg `-0.355` n `151`; fx avg `0.0149` n `6`; index avg `-0.0881` n `26`; metal avg `0.1143` n `20`; unknown avg `-0.3468` n `1190`
- 24h: commodity avg `0.2348` n `13`; crypto_alt avg `0.2043` n `237`; crypto_major avg `-0.3611` n `8`; equity avg `-0.4566` n `151`; fx avg `-0.0017` n `6`; index avg `-0.0462` n `26`; metal avg `-0.1866` n `20`; unknown avg `5.2409` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
