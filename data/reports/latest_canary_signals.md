# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T09:22:26.343308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0574` n `12`; crypto_alt avg `-0.0927` n `233`; crypto_major avg `0.0253` n `8`; equity avg `-0.0613` n `136`; fx avg `0.0045` n `6`; index avg `-0.0157` n `27`; metal avg `-0.0343` n `20`; unknown avg `-0.0461` n `908`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `0.1054` n `233`; crypto_major avg `0.1623` n `8`; equity avg `-0.0762` n `136`; fx avg `0.0128` n `6`; index avg `-0.0346` n `27`; metal avg `-0.0264` n `20`; unknown avg `0.8015` n `900`
- 4h: commodity avg `0.1029` n `12`; crypto_alt avg `-0.3781` n `233`; crypto_major avg `-0.2591` n `8`; equity avg `-0.1837` n `136`; fx avg `0.0798` n `6`; index avg `-0.0531` n `27`; metal avg `-0.2296` n `20`; unknown avg `17.6238` n `876`
- 24h: commodity avg `-0.0534` n `12`; crypto_alt avg `-1.1165` n `233`; crypto_major avg `-0.6584` n `8`; equity avg `0.059` n `136`; fx avg `0.2484` n `6`; index avg `-0.0406` n `27`; metal avg `-0.0782` n `20`; unknown avg `0.2716` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
