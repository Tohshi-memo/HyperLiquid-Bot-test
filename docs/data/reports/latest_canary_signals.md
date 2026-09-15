# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T05:52:30.235262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1088` n `12`; crypto_alt avg `0.3538` n `233`; crypto_major avg `0.3396` n `8`; equity avg `0.2208` n `136`; fx avg `-0.0071` n `6`; index avg `0.0443` n `27`; metal avg `0.0705` n `20`; unknown avg `5.4428` n `908`
- 1h: commodity avg `-0.0883` n `12`; crypto_alt avg `-0.1128` n `233`; crypto_major avg `-0.005` n `8`; equity avg `0.0756` n `136`; fx avg `0.042` n `6`; index avg `0.0289` n `27`; metal avg `0.0037` n `20`; unknown avg `7.4076` n `906`
- 4h: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.6309` n `233`; crypto_major avg `-0.6508` n `8`; equity avg `-0.3495` n `136`; fx avg `0.0652` n `6`; index avg `-0.068` n `27`; metal avg `0.1149` n `20`; unknown avg `6.5005` n `890`
- 24h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.8044` n `233`; crypto_major avg `0.0732` n `8`; equity avg `-0.2091` n `136`; fx avg `0.1383` n `6`; index avg `-0.0433` n `27`; metal avg `-0.2218` n `20`; unknown avg `5.7826` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
