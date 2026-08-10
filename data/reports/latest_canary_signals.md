# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T01:22:24.741106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.042` n `230`; crypto_major avg `0.1482` n `8`; equity avg `0.2995` n `112`; fx avg `0.0152` n `6`; index avg `0.0486` n `25`; metal avg `0.0417` n `20`; unknown avg `-0.0762` n `785`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `-0.0044` n `8`; equity avg `-0.1104` n `112`; fx avg `0.043` n `6`; index avg `0.0069` n `25`; metal avg `-0.1171` n `20`; unknown avg `-0.1637` n `785`
- 4h: commodity avg `0.2277` n `12`; crypto_alt avg `-0.663` n `230`; crypto_major avg `-0.5546` n `8`; equity avg `-0.2239` n `112`; fx avg `0.1072` n `6`; index avg `-0.0057` n `25`; metal avg `-0.2646` n `20`; unknown avg `0.0973` n `785`
- 24h: commodity avg `0.4503` n `12`; crypto_alt avg `0.7013` n `230`; crypto_major avg `-0.2273` n `8`; equity avg `-0.0492` n `112`; fx avg `0.0974` n `6`; index avg `0.0132` n `25`; metal avg `-0.2255` n `20`; unknown avg `-0.3624` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
