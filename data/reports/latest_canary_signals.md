# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T07:07:32.538559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0537` n `12`; crypto_alt avg `-0.0941` n `233`; crypto_major avg `-0.0744` n `8`; equity avg `0.0088` n `136`; fx avg `0.0003` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0203` n `20`; unknown avg `16.4629` n `904`
- 1h: commodity avg `0.0916` n `12`; crypto_alt avg `-0.552` n `233`; crypto_major avg `-0.7138` n `8`; equity avg `-0.1055` n `136`; fx avg `0.0054` n `6`; index avg `-0.022` n `27`; metal avg `-0.0232` n `20`; unknown avg `16.8409` n `904`
- 4h: commodity avg `0.1353` n `12`; crypto_alt avg `-0.8626` n `233`; crypto_major avg `-0.8468` n `8`; equity avg `-0.6483` n `136`; fx avg `0.0532` n `6`; index avg `-0.1324` n `27`; metal avg `-0.1531` n `20`; unknown avg `2.8514` n `868`
- 24h: commodity avg `0.0702` n `12`; crypto_alt avg `-1.5333` n `233`; crypto_major avg `-0.8049` n `8`; equity avg `-0.3513` n `136`; fx avg `0.1668` n `6`; index avg `-0.0579` n `27`; metal avg `-0.2872` n `20`; unknown avg `4.346` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
