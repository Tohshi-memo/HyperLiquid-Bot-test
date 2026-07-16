# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T08:07:27.889385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0835` n `230`; crypto_major avg `-0.0535` n `8`; equity avg `-0.1672` n `94`; fx avg `-0.0217` n `6`; index avg `-0.0284` n `25`; metal avg `0.0278` n `20`; unknown avg `0.0129` n `768`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `-0.6284` n `230`; crypto_major avg `-0.8041` n `8`; equity avg `-0.6109` n `94`; fx avg `-0.0155` n `6`; index avg `-0.0992` n `25`; metal avg `-0.0402` n `20`; unknown avg `-0.0616` n `768`
- 4h: commodity avg `-0.065` n `12`; crypto_alt avg `-0.698` n `230`; crypto_major avg `-0.4886` n `8`; equity avg `-0.8779` n `94`; fx avg `-0.0727` n `6`; index avg `-0.1636` n `25`; metal avg `-0.1466` n `20`; unknown avg `0.0537` n `752`
- 24h: commodity avg `-0.2393` n `12`; crypto_alt avg `-0.1488` n `230`; crypto_major avg `-0.1981` n `8`; equity avg `-2.7558` n `93`; fx avg `0.0386` n `6`; index avg `-0.4927` n `25`; metal avg `-0.0617` n `20`; unknown avg `-0.1404` n `749`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
