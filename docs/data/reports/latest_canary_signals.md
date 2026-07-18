# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T15:22:26.575945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.0887` n `230`; crypto_major avg `-0.0402` n `8`; equity avg `-0.0039` n `96`; fx avg `-0.0032` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.0339` n `770`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.1802` n `230`; crypto_major avg `0.045` n `8`; equity avg `0.0212` n `96`; fx avg `-0.0139` n `6`; index avg `0.0102` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.0063` n `770`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `0.09` n `230`; crypto_major avg `0.0898` n `8`; equity avg `-0.0962` n `96`; fx avg `-0.0036` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0367` n `20`; unknown avg `-0.0184` n `770`
- 24h: commodity avg `0.5517` n `12`; crypto_alt avg `-0.09` n `230`; crypto_major avg `0.67` n `8`; equity avg `0.277` n `96`; fx avg `-0.0218` n `6`; index avg `0.0746` n `25`; metal avg `0.0758` n `20`; unknown avg `0.1501` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
