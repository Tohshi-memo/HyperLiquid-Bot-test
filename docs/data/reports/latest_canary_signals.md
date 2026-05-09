# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T22:23:55.367560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.093` n `228`; crypto_major avg `0.0088` n `8`; equity avg `0.0471` n `65`; fx avg `0.0` n `5`; index avg `0.0153` n `23`; metal avg `-0.0152` n `18`; unknown avg `-0.1845` n `376`
- 1h: commodity avg `-0.0319` n `12`; crypto_alt avg `0.1139` n `228`; crypto_major avg `0.0595` n `8`; equity avg `0.0799` n `65`; fx avg `0.0` n `5`; index avg `0.0654` n `23`; metal avg `0.0566` n `18`; unknown avg `-0.0834` n `376`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1547` n `228`; crypto_major avg `0.0038` n `8`; equity avg `0.4089` n `65`; fx avg `-0.0083` n `5`; index avg `0.1046` n `23`; metal avg `0.1663` n `18`; unknown avg `-0.2055` n `376`
- 24h: commodity avg `0.5305` n `12`; crypto_alt avg `0.1342` n `228`; crypto_major avg `0.2264` n `8`; equity avg `0.6849` n `65`; fx avg `-0.0291` n `5`; index avg `0.3317` n `23`; metal avg `0.119` n `18`; unknown avg `0.1255` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
