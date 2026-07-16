# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T11:21:04.707205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0305` n `230`; crypto_major avg `0.006` n `8`; equity avg `-0.0765` n `94`; fx avg `0.0025` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0104` n `20`; unknown avg `0.7405` n `768`
- 1h: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.0761` n `230`; crypto_major avg `-0.1314` n `8`; equity avg `-0.2371` n `94`; fx avg `-0.0208` n `6`; index avg `-0.0511` n `25`; metal avg `-0.0751` n `20`; unknown avg `0.638` n `768`
- 4h: commodity avg `0.0668` n `12`; crypto_alt avg `-0.7374` n `230`; crypto_major avg `-1.0444` n `8`; equity avg `-0.9052` n `94`; fx avg `-0.0346` n `6`; index avg `-0.1411` n `25`; metal avg `-0.0613` n `20`; unknown avg `0.4879` n `762`
- 24h: commodity avg `-0.0688` n `12`; crypto_alt avg `-0.7203` n `230`; crypto_major avg `-0.8758` n `8`; equity avg `-3.1134` n `93`; fx avg `0.0178` n `6`; index avg `-0.5297` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.714` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
