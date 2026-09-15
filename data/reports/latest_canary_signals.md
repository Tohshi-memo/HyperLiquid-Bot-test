# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T05:22:29.166931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.42` n `233`; crypto_major avg `-0.3425` n `8`; equity avg `-0.181` n `136`; fx avg `0.0328` n `6`; index avg `-0.0356` n `27`; metal avg `-0.0274` n `20`; unknown avg `7.4341` n `908`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `-0.4523` n `233`; crypto_major avg `-0.5416` n `8`; equity avg `-0.4297` n `136`; fx avg `0.0367` n `6`; index avg `-0.081` n `27`; metal avg `-0.055` n `20`; unknown avg `7.2413` n `900`
- 4h: commodity avg `0.1532` n `12`; crypto_alt avg `-1.0689` n `233`; crypto_major avg `-1.0654` n `8`; equity avg `-0.9272` n `136`; fx avg `0.089` n `6`; index avg `-0.1881` n `27`; metal avg `-0.02` n `20`; unknown avg `7.7175` n `890`
- 24h: commodity avg `0.0595` n `12`; crypto_alt avg `-1.1766` n `233`; crypto_major avg `-0.3958` n `8`; equity avg `-0.6235` n `136`; fx avg `0.1666` n `6`; index avg `-0.1239` n `27`; metal avg `-0.3084` n `20`; unknown avg `5.0856` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
