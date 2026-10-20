# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T17:37:40.441004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.0903` n `237`; crypto_major avg `0.0036` n `8`; equity avg `-0.0289` n `151`; fx avg `-0.0033` n `6`; index avg `0.0049` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.4338` n `1199`
- 1h: commodity avg `0.1099` n `13`; crypto_alt avg `0.2923` n `237`; crypto_major avg `0.2719` n `8`; equity avg `-0.1527` n `151`; fx avg `-0.0161` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0019` n `20`; unknown avg `40.5095` n `1195`
- 4h: commodity avg `-0.2207` n `13`; crypto_alt avg `2.0619` n `237`; crypto_major avg `1.4171` n `8`; equity avg `1.6652` n `151`; fx avg `0.011` n `6`; index avg `0.2352` n `26`; metal avg `0.1023` n `20`; unknown avg `0.77` n `1100`
- 24h: commodity avg `-0.4469` n `13`; crypto_alt avg `2.9731` n `237`; crypto_major avg `1.8298` n `8`; equity avg `0.1508` n `151`; fx avg `0.0097` n `6`; index avg `0.0355` n `26`; metal avg `-0.0026` n `20`; unknown avg `4.0947` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
