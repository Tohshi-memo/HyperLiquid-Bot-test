# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T19:22:26.844370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.1551` n `233`; crypto_major avg `-0.1538` n `8`; equity avg `-0.0145` n `136`; fx avg `0.0012` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0074` n `20`; unknown avg `0.0449` n `838`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.22` n `233`; crypto_major avg `-0.2165` n `8`; equity avg `-0.024` n `136`; fx avg `0.0106` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0092` n `20`; unknown avg `2.669` n `796`
- 4h: commodity avg `0.0844` n `12`; crypto_alt avg `-0.3793` n `233`; crypto_major avg `-0.5966` n `8`; equity avg `-0.0376` n `136`; fx avg `0.0021` n `6`; index avg `-0.0076` n `26`; metal avg `0.0045` n `20`; unknown avg `0.2856` n `782`
- 24h: commodity avg `-0.2181` n `12`; crypto_alt avg `1.2552` n `233`; crypto_major avg `0.0191` n `8`; equity avg `-0.0285` n `136`; fx avg `-0.0282` n `6`; index avg `0.0272` n `26`; metal avg `0.0021` n `20`; unknown avg `1.0605` n `710`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
