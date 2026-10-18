# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T22:52:27.342483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `13`; crypto_alt avg `0.3786` n `237`; crypto_major avg `0.3279` n `8`; equity avg `0.2011` n `151`; fx avg `-0.0129` n `6`; index avg `0.0226` n `26`; metal avg `-0.0147` n `20`; unknown avg `0.1934` n `1194`
- 1h: commodity avg `-0.3317` n `13`; crypto_alt avg `1.6836` n `237`; crypto_major avg `1.3737` n `8`; equity avg `1.0508` n `151`; fx avg `0.031` n `6`; index avg `0.244` n `26`; metal avg `0.2216` n `20`; unknown avg `2.6098` n `1182`
- 4h: commodity avg `-0.3342` n `13`; crypto_alt avg `0.8898` n `237`; crypto_major avg `1.25` n `8`; equity avg `1.3113` n `151`; fx avg `-0.0182` n `6`; index avg `0.2947` n `26`; metal avg `0.1919` n `20`; unknown avg `8.6754` n `1088`
- 24h: commodity avg `-0.3138` n `13`; crypto_alt avg `-1.9724` n `236`; crypto_major avg `0.3353` n `8`; equity avg `1.2618` n `151`; fx avg `-0.0169` n `6`; index avg `0.2654` n `26`; metal avg `0.2073` n `20`; unknown avg `1.4681` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2017`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0715`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
