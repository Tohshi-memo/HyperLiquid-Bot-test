# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T22:36:20.030532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `0.2279` n `230`; crypto_major avg `0.0299` n `8`; equity avg `-0.0138` n `121`; fx avg `0.0171` n `6`; index avg `-0.0019` n `25`; metal avg `0.0023` n `20`; unknown avg `0.0327` n `794`
- 1h: commodity avg `0.0182` n `12`; crypto_alt avg `0.6602` n `230`; crypto_major avg `0.4193` n `8`; equity avg `0.0147` n `121`; fx avg `0.0123` n `6`; index avg `0.0015` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.3415` n `794`
- 4h: commodity avg `0.1047` n `12`; crypto_alt avg `-1.1955` n `230`; crypto_major avg `-0.5338` n `8`; equity avg `0.0751` n `121`; fx avg `0.0357` n `6`; index avg `-0.0087` n `25`; metal avg `0.0172` n `20`; unknown avg `0.3376` n `794`
- 24h: commodity avg `0.0644` n `12`; crypto_alt avg `-2.1118` n `230`; crypto_major avg `-0.0876` n `8`; equity avg `-0.4411` n `121`; fx avg `0.0841` n `6`; index avg `-0.0625` n `25`; metal avg `-0.0568` n `20`; unknown avg `1.6937` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
