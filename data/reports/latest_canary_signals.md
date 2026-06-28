# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T12:37:25.649953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0426` n `12`; crypto_alt avg `0.1079` n `228`; crypto_major avg `0.1445` n `8`; equity avg `0.0263` n `88`; fx avg `0.0` n `6`; index avg `-0.0008` n `23`; metal avg `0.004` n `20`; unknown avg `0.0494` n `764`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.1927` n `228`; crypto_major avg `0.0503` n `8`; equity avg `-0.0195` n `88`; fx avg `0.0056` n `6`; index avg `0.0007` n `23`; metal avg `0.0043` n `20`; unknown avg `0.1249` n `764`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `0.233` n `228`; crypto_major avg `0.1683` n `8`; equity avg `0.0426` n `88`; fx avg `0.028` n `6`; index avg `0.0129` n `23`; metal avg `0.0167` n `20`; unknown avg `-1.0537` n `750`
- 24h: commodity avg `0.0987` n `12`; crypto_alt avg `-0.0039` n `228`; crypto_major avg `-0.5411` n `8`; equity avg `0.0846` n `88`; fx avg `0.0014` n `6`; index avg `-0.0506` n `23`; metal avg `-0.0081` n `20`; unknown avg `15.6021` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
