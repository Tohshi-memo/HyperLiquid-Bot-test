# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T22:22:27.375209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.1644` n `233`; crypto_major avg `-0.1098` n `8`; equity avg `0.0167` n `136`; fx avg `-0.0066` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0075` n `20`; unknown avg `0.1307` n `900`
- 1h: commodity avg `0.0129` n `12`; crypto_alt avg `-0.4476` n `233`; crypto_major avg `-0.5073` n `8`; equity avg `-0.0154` n `136`; fx avg `-0.0138` n `6`; index avg `-0.0032` n `27`; metal avg `-0.022` n `20`; unknown avg `0.0004` n `894`
- 4h: commodity avg `0.0132` n `12`; crypto_alt avg `-0.6986` n `233`; crypto_major avg `-0.5508` n `8`; equity avg `-0.4315` n `136`; fx avg `-0.0109` n `6`; index avg `-0.0859` n `27`; metal avg `-0.1058` n `20`; unknown avg `0.2344` n `866`
- 24h: commodity avg `-0.1061` n `12`; crypto_alt avg `1.4965` n `233`; crypto_major avg `2.9136` n `8`; equity avg `-0.3108` n `136`; fx avg `0.0183` n `6`; index avg `-0.1249` n `27`; metal avg `-0.2745` n `20`; unknown avg `0.5867` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
