# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T08:22:28.658902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0573` n `12`; crypto_alt avg `0.2028` n `234`; crypto_major avg `0.2576` n `8`; equity avg `0.0802` n `140`; fx avg `-0.0037` n `6`; index avg `0.0097` n `26`; metal avg `0.0732` n `20`; unknown avg `18.4294` n `944`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.394` n `234`; crypto_major avg `0.5794` n `8`; equity avg `0.3164` n `140`; fx avg `-0.0457` n `6`; index avg `0.0505` n `26`; metal avg `0.0555` n `20`; unknown avg `19.0602` n `936`
- 4h: commodity avg `-0.0066` n `12`; crypto_alt avg `0.6858` n `234`; crypto_major avg `1.1499` n `8`; equity avg `0.4807` n `140`; fx avg `-0.0661` n `6`; index avg `0.0931` n `26`; metal avg `-0.0154` n `20`; unknown avg `0.6335` n `890`
- 24h: commodity avg `-0.6581` n `12`; crypto_alt avg `4.606` n `234`; crypto_major avg `3.6694` n `8`; equity avg `1.6309` n `140`; fx avg `-0.0819` n `6`; index avg `0.3327` n `26`; metal avg `0.0403` n `20`; unknown avg `9.2821` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
