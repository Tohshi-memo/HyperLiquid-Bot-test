# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T23:37:31.318839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.2482` n `228`; crypto_major avg `-0.215` n `8`; equity avg `-0.0767` n `88`; fx avg `0.0031` n `6`; index avg `-0.0015` n `25`; metal avg `0.0281` n `20`; unknown avg `0.0558` n `763`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.8141` n `228`; crypto_major avg `-0.6519` n `8`; equity avg `-0.3686` n `88`; fx avg `-0.0028` n `6`; index avg `-0.0366` n `25`; metal avg `-0.033` n `20`; unknown avg `140.9958` n `763`
- 4h: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.0724` n `228`; crypto_major avg `-0.4452` n `8`; equity avg `-0.6054` n `88`; fx avg `0.0457` n `6`; index avg `-0.1004` n `25`; metal avg `-0.1494` n `20`; unknown avg `143.2985` n `763`
- 24h: commodity avg `-0.6393` n `12`; crypto_alt avg `1.7861` n `228`; crypto_major avg `1.3042` n `8`; equity avg `-1.9016` n `88`; fx avg `0.0497` n `6`; index avg `-0.5423` n `25`; metal avg `0.272` n `20`; unknown avg `147.8487` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
