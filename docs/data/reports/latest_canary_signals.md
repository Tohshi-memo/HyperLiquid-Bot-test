# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T13:37:34.029260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.0576` n `230`; crypto_major avg `-0.0526` n `8`; equity avg `-0.0077` n `102`; fx avg `-0.024` n `6`; index avg `-0.0052` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0171` n `782`
- 1h: commodity avg `0.0265` n `12`; crypto_alt avg `-0.1659` n `230`; crypto_major avg `-0.0437` n `8`; equity avg `0.0122` n `102`; fx avg `-0.0346` n `6`; index avg `0.0092` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0091` n `782`
- 4h: commodity avg `0.2524` n `12`; crypto_alt avg `-0.393` n `230`; crypto_major avg `-0.4319` n `8`; equity avg `-0.1876` n `102`; fx avg `-0.0313` n `6`; index avg `-0.0449` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.0809` n `782`
- 24h: commodity avg `-1.0537` n `12`; crypto_alt avg `0.0648` n `230`; crypto_major avg `-0.0812` n `8`; equity avg `0.8382` n `102`; fx avg `-0.1272` n `6`; index avg `0.2153` n `25`; metal avg `0.2505` n `20`; unknown avg `0.2793` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
