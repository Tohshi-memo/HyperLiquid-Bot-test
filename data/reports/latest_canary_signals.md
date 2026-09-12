# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T21:52:27.184731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `-0.0817` n `233`; crypto_major avg `-0.0676` n `8`; equity avg `-0.0032` n `136`; fx avg `-0.0006` n `6`; index avg `0.0063` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.3429` n `838`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `-0.1468` n `233`; crypto_major avg `-0.0351` n `8`; equity avg `-0.006` n `136`; fx avg `-0.0005` n `6`; index avg `0.0027` n `26`; metal avg `-0.0153` n `20`; unknown avg `21.7183` n `828`
- 4h: commodity avg `0.0188` n `12`; crypto_alt avg `-0.4071` n `233`; crypto_major avg `-0.3611` n `8`; equity avg `-0.2824` n `136`; fx avg `-0.0045` n `6`; index avg `-0.0293` n `26`; metal avg `-0.0206` n `20`; unknown avg `1.2483` n `782`
- 24h: commodity avg `-0.0738` n `12`; crypto_alt avg `1.3544` n `233`; crypto_major avg `-0.0348` n `8`; equity avg `-0.256` n `136`; fx avg `-0.0169` n `6`; index avg `0.0063` n `26`; metal avg `-0.0404` n `20`; unknown avg `6.7056` n `736`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
