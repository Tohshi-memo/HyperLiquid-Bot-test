# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T15:07:33.350744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0898` n `12`; crypto_alt avg `-0.3687` n `233`; crypto_major avg `-0.1583` n `8`; equity avg `-0.0816` n `136`; fx avg `-0.0021` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0027` n `20`; unknown avg `22.0937` n `836`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.261` n `233`; crypto_major avg `0.1586` n `8`; equity avg `0.0131` n `136`; fx avg `-0.0032` n `6`; index avg `-0.0056` n `27`; metal avg `0.0066` n `20`; unknown avg `2.6413` n `836`
- 4h: commodity avg `0.0922` n `12`; crypto_alt avg `0.4834` n `233`; crypto_major avg `0.4731` n `8`; equity avg `0.0619` n `136`; fx avg `-0.0032` n `6`; index avg `0.0281` n `27`; metal avg `0.0005` n `20`; unknown avg `2.597` n `826`
- 24h: commodity avg `0.2951` n `12`; crypto_alt avg `-0.4318` n `233`; crypto_major avg `-1.6473` n `8`; equity avg `-1.6709` n `136`; fx avg `0.0018` n `6`; index avg `-0.2604` n `26`; metal avg `-0.0747` n `20`; unknown avg `1.9065` n `708`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
