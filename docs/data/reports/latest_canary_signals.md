# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T22:37:34.385456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `0.1942` n `235`; crypto_major avg `0.132` n `8`; equity avg `0.0375` n `150`; fx avg `0.0` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0124` n `20`; unknown avg `0.0789` n `1077`
- 1h: commodity avg `0.1419` n `13`; crypto_alt avg `0.5123` n `235`; crypto_major avg `0.2359` n `8`; equity avg `0.0664` n `150`; fx avg `0.0054` n `6`; index avg `0.0263` n `26`; metal avg `-0.0374` n `20`; unknown avg `0.8728` n `1075`
- 4h: commodity avg `0.2993` n `13`; crypto_alt avg `0.6607` n `235`; crypto_major avg `0.0416` n `8`; equity avg `0.0999` n `150`; fx avg `0.0282` n `6`; index avg `0.0163` n `26`; metal avg `-0.0556` n `20`; unknown avg `0.5131` n `999`
- 24h: commodity avg `0.4914` n `13`; crypto_alt avg `-3.7831` n `235`; crypto_major avg `-3.415` n `8`; equity avg `-1.3765` n `150`; fx avg `-0.1429` n `6`; index avg `-0.2013` n `26`; metal avg `-0.6999` n `20`; unknown avg `247.5799` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
