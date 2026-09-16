# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T23:07:27.093336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0244` n `234`; crypto_major avg `0.0718` n `8`; equity avg `0.0495` n `137`; fx avg `-0.0046` n `6`; index avg `-0.003` n `27`; metal avg `-0.0272` n `20`; unknown avg `0.7878` n `909`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `0.1035` n `234`; crypto_major avg `0.0122` n `8`; equity avg `0.2956` n `137`; fx avg `0.003` n `6`; index avg `0.0551` n `27`; metal avg `-0.0021` n `20`; unknown avg `-0.0718` n `821`
- 4h: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.0112` n `234`; crypto_major avg `-0.5765` n `8`; equity avg `0.8834` n `137`; fx avg `0.0463` n `6`; index avg `0.1234` n `27`; metal avg `0.0063` n `20`; unknown avg `0.6919` n `773`
- 24h: commodity avg `-0.6015` n `12`; crypto_alt avg `-0.104` n `234`; crypto_major avg `0.099` n `8`; equity avg `1.2309` n `137`; fx avg `0.0668` n `6`; index avg `0.0811` n `27`; metal avg `-0.3028` n `20`; unknown avg `-0.8788` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
