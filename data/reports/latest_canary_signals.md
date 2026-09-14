# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T15:07:39.010077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1681` n `12`; crypto_alt avg `-0.0439` n `233`; crypto_major avg `0.0792` n `8`; equity avg `0.1955` n `136`; fx avg `-0.0037` n `6`; index avg `0.0374` n `27`; metal avg `0.068` n `20`; unknown avg `-0.1744` n `892`
- 1h: commodity avg `-0.1959` n `12`; crypto_alt avg `-0.235` n `233`; crypto_major avg `-0.1629` n `8`; equity avg `-0.2908` n `136`; fx avg `-0.0232` n `6`; index avg `-0.0859` n `27`; metal avg `0.0853` n `20`; unknown avg `0.2372` n `878`
- 4h: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.3073` n `233`; crypto_major avg `0.1444` n `8`; equity avg `0.0462` n `136`; fx avg `0.0118` n `6`; index avg `-0.0727` n `27`; metal avg `0.0095` n `20`; unknown avg `0.3127` n `872`
- 24h: commodity avg `0.4224` n `12`; crypto_alt avg `-0.7575` n `233`; crypto_major avg `1.2785` n `8`; equity avg `-0.8457` n `136`; fx avg `0.0553` n `6`; index avg `-0.3035` n `27`; metal avg `-0.4546` n `20`; unknown avg `0.9631` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
