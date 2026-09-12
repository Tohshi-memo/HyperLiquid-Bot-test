# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T22:07:31.098575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `0.0719` n `233`; crypto_major avg `0.0232` n `8`; equity avg `-0.0072` n `136`; fx avg `0.0033` n `6`; index avg `0.0001` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.2079` n `818`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `-0.1167` n `233`; crypto_major avg `-0.0886` n `8`; equity avg `-0.0021` n `136`; fx avg `0.0033` n `6`; index avg `0.003` n `26`; metal avg `-0.001` n `20`; unknown avg `17.3916` n `810`
- 4h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.291` n `233`; crypto_major avg `-0.2512` n `8`; equity avg `-0.2921` n `136`; fx avg `0.005` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0237` n `20`; unknown avg `0.5769` n `764`
- 24h: commodity avg `-0.0561` n `12`; crypto_alt avg `1.5921` n `233`; crypto_major avg `0.1947` n `8`; equity avg `-0.2416` n `136`; fx avg `-0.0053` n `6`; index avg `0.0037` n `26`; metal avg `-0.0153` n `20`; unknown avg `3.2637` n `720`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
