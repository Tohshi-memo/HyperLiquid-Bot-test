# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T07:06:34.885375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.061` n `230`; crypto_major avg `-0.0729` n `8`; equity avg `-0.0169` n `94`; fx avg `-0.0025` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0209` n `20`; unknown avg `-0.0025` n `768`
- 1h: commodity avg `-0.0661` n `12`; crypto_alt avg `-0.0879` n `230`; crypto_major avg `-0.1353` n `8`; equity avg `0.0234` n `94`; fx avg `-0.0574` n `6`; index avg `0.0371` n `25`; metal avg `-0.1219` n `20`; unknown avg `0.0175` n `768`
- 4h: commodity avg `-0.1325` n `12`; crypto_alt avg `-0.2807` n `230`; crypto_major avg `0.0881` n `8`; equity avg `-0.362` n `94`; fx avg `-0.0645` n `6`; index avg `-0.0716` n `25`; metal avg `-0.0625` n `20`; unknown avg `-0.1586` n `752`
- 24h: commodity avg `-0.2089` n `12`; crypto_alt avg `0.0985` n `230`; crypto_major avg `0.2463` n `8`; equity avg `-2.4897` n `93`; fx avg `0.0637` n `6`; index avg `-0.4595` n `25`; metal avg `-0.0862` n `20`; unknown avg `-0.0964` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
