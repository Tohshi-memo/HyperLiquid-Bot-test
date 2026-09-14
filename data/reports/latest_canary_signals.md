# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T18:07:31.210807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `12`; crypto_alt avg `0.1539` n `233`; crypto_major avg `0.1954` n `8`; equity avg `-0.0256` n `136`; fx avg `-0.0001` n `6`; index avg `-0.01` n `27`; metal avg `-0.0003` n `20`; unknown avg `1.2779` n `906`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `0.5164` n `233`; crypto_major avg `0.639` n `8`; equity avg `0.1899` n `136`; fx avg `0.0016` n `6`; index avg `0.0178` n `27`; metal avg `-0.0284` n `20`; unknown avg `0.3595` n `906`
- 4h: commodity avg `-0.3688` n `12`; crypto_alt avg `1.1947` n `233`; crypto_major avg `1.162` n `8`; equity avg `0.7315` n `136`; fx avg `-0.0084` n `6`; index avg `0.1016` n `27`; metal avg `0.247` n `20`; unknown avg `0.6238` n `864`
- 24h: commodity avg `0.225` n `12`; crypto_alt avg `0.2841` n `233`; crypto_major avg `2.1533` n `8`; equity avg `-0.1018` n `136`; fx avg `0.0694` n `6`; index avg `-0.1149` n `27`; metal avg `-0.3072` n `20`; unknown avg `1.3172` n `688`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
