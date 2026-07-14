# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T10:52:30.718227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1249` n `12`; crypto_alt avg `0.107` n `230`; crypto_major avg `0.2407` n `8`; equity avg `-0.0637` n `92`; fx avg `0.0008` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.0166` n `766`
- 1h: commodity avg `0.0536` n `12`; crypto_alt avg `0.1186` n `230`; crypto_major avg `0.3593` n `8`; equity avg `0.0013` n `92`; fx avg `0.0064` n `6`; index avg `0.0174` n `25`; metal avg `-0.1012` n `20`; unknown avg `0.0001` n `766`
- 4h: commodity avg `0.1962` n `12`; crypto_alt avg `-0.1889` n `230`; crypto_major avg `0.1962` n `8`; equity avg `0.2693` n `92`; fx avg `0.0462` n `6`; index avg `0.036` n `25`; metal avg `-0.137` n `20`; unknown avg `-0.1218` n `766`
- 24h: commodity avg `1.4483` n `12`; crypto_alt avg `-0.9426` n `230`; crypto_major avg `-0.2994` n `8`; equity avg `-0.4883` n `92`; fx avg `-0.0171` n `6`; index avg `-0.0644` n `25`; metal avg `-0.1361` n `20`; unknown avg `-0.2924` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
