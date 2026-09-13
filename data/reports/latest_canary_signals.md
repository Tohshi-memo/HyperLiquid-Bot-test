# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T21:52:30.866701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.135` n `12`; crypto_alt avg `-0.1394` n `233`; crypto_major avg `-0.0677` n `8`; equity avg `0.0385` n `136`; fx avg `0.003` n `6`; index avg `0.0172` n `27`; metal avg `0.0095` n `20`; unknown avg `0.3896` n `840`
- 1h: commodity avg `-0.1678` n `12`; crypto_alt avg `-0.1834` n `233`; crypto_major avg `-0.1343` n `8`; equity avg `0.1451` n `136`; fx avg `0.0351` n `6`; index avg `0.0347` n `27`; metal avg `0.0312` n `20`; unknown avg `2.3822` n `838`
- 4h: commodity avg `-0.0574` n `12`; crypto_alt avg `-0.2506` n `233`; crypto_major avg `0.0173` n `8`; equity avg `0.0915` n `136`; fx avg `0.0387` n `6`; index avg `0.0403` n `27`; metal avg `0.0044` n `20`; unknown avg `8.512` n `794`
- 24h: commodity avg `0.1917` n `12`; crypto_alt avg `0.1869` n `233`; crypto_major avg `-0.4621` n `8`; equity avg `-1.0292` n `136`; fx avg `0.0534` n `6`; index avg `-0.2032` n `26`; metal avg `-0.0402` n `20`; unknown avg `2.5739` n `698`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
