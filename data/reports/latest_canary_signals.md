# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T21:52:32.403447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.0582` n `232`; crypto_major avg `-0.0252` n `8`; equity avg `0.0051` n `133`; fx avg `-0.0086` n `6`; index avg `0.0084` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.1244` n `792`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `-0.1692` n `232`; crypto_major avg `-0.1498` n `8`; equity avg `0.2218` n `133`; fx avg `-0.0171` n `6`; index avg `0.0348` n `26`; metal avg `-0.0375` n `20`; unknown avg `-0.1258` n `784`
- 4h: commodity avg `0.0778` n `12`; crypto_alt avg `0.0634` n `232`; crypto_major avg `0.1382` n `8`; equity avg `0.6564` n `133`; fx avg `-0.0359` n `6`; index avg `0.0213` n `26`; metal avg `0.0326` n `20`; unknown avg `0.0278` n `772`
- 24h: commodity avg `0.1702` n `12`; crypto_alt avg `-0.1389` n `232`; crypto_major avg `-0.1506` n `8`; equity avg `1.0346` n `133`; fx avg `-0.3967` n `6`; index avg `0.1249` n `26`; metal avg `0.4013` n `20`; unknown avg `0.2557` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0443`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
