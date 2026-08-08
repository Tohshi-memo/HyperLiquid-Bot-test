# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T03:37:30.248345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `0.162` n `230`; crypto_major avg `0.1934` n `8`; equity avg `-0.0709` n `112`; fx avg `0.0011` n `6`; index avg `-0.0018` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0418` n `783`
- 1h: commodity avg `0.008` n `12`; crypto_alt avg `0.2561` n `230`; crypto_major avg `0.3378` n `8`; equity avg `-0.0516` n `112`; fx avg `0.0055` n `6`; index avg `-0.0028` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0443` n `783`
- 4h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.4944` n `230`; crypto_major avg `0.5322` n `8`; equity avg `0.0424` n `112`; fx avg `0.0027` n `6`; index avg `0.0103` n `25`; metal avg `0.0181` n `20`; unknown avg `-0.175` n `783`
- 24h: commodity avg `-0.1732` n `12`; crypto_alt avg `-0.0962` n `230`; crypto_major avg `0.5132` n `8`; equity avg `1.6234` n `112`; fx avg `-0.0879` n `6`; index avg `0.2047` n `25`; metal avg `0.3476` n `20`; unknown avg `-0.0167` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
