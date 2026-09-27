# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T14:37:25.360179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.2829` n `234`; crypto_major avg `-0.3638` n `8`; equity avg `-0.0477` n `141`; fx avg `0.0052` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.2526` n `962`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `-0.2215` n `234`; crypto_major avg `-0.4964` n `8`; equity avg `-0.0946` n `141`; fx avg `-0.0016` n `6`; index avg `-0.0248` n `26`; metal avg `-0.0048` n `20`; unknown avg `1.3625` n `960`
- 4h: commodity avg `-0.0262` n `12`; crypto_alt avg `-0.9634` n `234`; crypto_major avg `-0.8203` n `8`; equity avg `-0.1174` n `141`; fx avg `0.0037` n `6`; index avg `-0.0398` n `26`; metal avg `-0.0153` n `20`; unknown avg `7.9788` n `954`
- 24h: commodity avg `-0.0538` n `12`; crypto_alt avg `-0.2589` n `234`; crypto_major avg `-0.0872` n `8`; equity avg `0.2083` n `141`; fx avg `-0.035` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0219` n `20`; unknown avg `245.5927` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
