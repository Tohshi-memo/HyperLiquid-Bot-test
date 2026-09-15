# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T05:07:26.473625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.0735` n `233`; crypto_major avg `-0.0729` n `8`; equity avg `-0.0941` n `136`; fx avg `0.0155` n `6`; index avg `-0.0159` n `27`; metal avg `-0.0257` n `20`; unknown avg `-0.0591` n `906`
- 1h: commodity avg `0.0562` n `12`; crypto_alt avg `-0.0016` n `233`; crypto_major avg `-0.2778` n `8`; equity avg `-0.3977` n `136`; fx avg `0.0179` n `6`; index avg `-0.0885` n `27`; metal avg `-0.0449` n `20`; unknown avg `0.0516` n `900`
- 4h: commodity avg `0.114` n `12`; crypto_alt avg `-0.5591` n `233`; crypto_major avg `-0.5223` n `8`; equity avg `-0.6565` n `136`; fx avg `0.0616` n `6`; index avg `-0.1311` n `27`; metal avg `0.0773` n `20`; unknown avg `0.4055` n `890`
- 24h: commodity avg `0.0894` n `12`; crypto_alt avg `-0.9124` n `233`; crypto_major avg `-0.096` n `8`; equity avg `-0.5818` n `136`; fx avg `0.133` n `6`; index avg `-0.1058` n `27`; metal avg `-0.3053` n `20`; unknown avg `4.9724` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
