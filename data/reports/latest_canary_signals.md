# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T23:36:51.687522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `-0.1007` n `8`; equity avg `-0.0286` n `94`; fx avg `0.0024` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.0099` n `768`
- 1h: commodity avg `-0.0614` n `12`; crypto_alt avg `-0.111` n `230`; crypto_major avg `-0.1253` n `8`; equity avg `0.1264` n `94`; fx avg `-0.0194` n `6`; index avg `0.0301` n `25`; metal avg `-0.0165` n `20`; unknown avg `0.5492` n `768`
- 4h: commodity avg `-0.1239` n `12`; crypto_alt avg `0.1985` n `230`; crypto_major avg `0.0813` n `8`; equity avg `-0.0292` n `94`; fx avg `-0.0122` n `6`; index avg `0.0277` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.0526` n `768`
- 24h: commodity avg `0.0751` n `12`; crypto_alt avg `0.2599` n `230`; crypto_major avg `0.4114` n `8`; equity avg `-0.9298` n `93`; fx avg `0.2253` n `6`; index avg `-0.204` n `25`; metal avg `0.1074` n `20`; unknown avg `0.0882` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
