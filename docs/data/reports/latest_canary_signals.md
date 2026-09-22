# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T04:52:27.467551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.046` n `12`; crypto_alt avg `0.035` n `234`; crypto_major avg `-0.002` n `8`; equity avg `-0.1284` n `140`; fx avg `0.0047` n `6`; index avg `-0.0208` n `26`; metal avg `-0.009` n `20`; unknown avg `0.3626` n `944`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1162` n `234`; crypto_major avg `0.0841` n `8`; equity avg `-0.5578` n `140`; fx avg `-0.0108` n `6`; index avg `-0.063` n `26`; metal avg `0.0002` n `20`; unknown avg `1.4217` n `936`
- 4h: commodity avg `0.1357` n `12`; crypto_alt avg `-0.9009` n `234`; crypto_major avg `-0.9344` n `8`; equity avg `-0.8222` n `140`; fx avg `-0.0096` n `6`; index avg `-0.1045` n `26`; metal avg `-0.1765` n `20`; unknown avg `1.2824` n `936`
- 24h: commodity avg `-0.1218` n `12`; crypto_alt avg `2.5581` n `234`; crypto_major avg `4.1702` n `8`; equity avg `1.748` n `140`; fx avg `-0.2633` n `6`; index avg `0.3954` n `26`; metal avg `-0.0767` n `20`; unknown avg `8.403` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
