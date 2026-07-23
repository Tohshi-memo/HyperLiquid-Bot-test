# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T01:22:29.550860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.1529` n `230`; crypto_major avg `-0.174` n `8`; equity avg `-0.0159` n `98`; fx avg `-0.0021` n `6`; index avg `-0.0154` n `25`; metal avg `0.1074` n `20`; unknown avg `0.2331` n `773`
- 1h: commodity avg `0.0642` n `12`; crypto_alt avg `-0.1737` n `230`; crypto_major avg `-0.3393` n `8`; equity avg `0.1289` n `98`; fx avg `-0.0517` n `6`; index avg `0.034` n `25`; metal avg `0.1345` n `20`; unknown avg `0.3472` n `773`
- 4h: commodity avg `0.2565` n `12`; crypto_alt avg `-0.1802` n `230`; crypto_major avg `0.1089` n `8`; equity avg `0.2099` n `98`; fx avg `-0.0623` n `6`; index avg `0.0998` n `25`; metal avg `0.1045` n `20`; unknown avg `-0.0547` n `773`
- 24h: commodity avg `0.6811` n `11`; crypto_alt avg `-0.5355` n `230`; crypto_major avg `-0.6699` n `8`; equity avg `-0.9194` n `87`; fx avg `-0.1241` n `5`; index avg `-0.086` n `19`; metal avg `0.0376` n `16`; unknown avg `1.8108` n `722`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.069`, n `666`, weak_sample_signal
