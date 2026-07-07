# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T23:52:28.801082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.1975` n `229`; crypto_major avg `-0.2231` n `8`; equity avg `-0.2048` n `91`; fx avg `0.0552` n `6`; index avg `-0.0561` n `25`; metal avg `-0.0266` n `20`; unknown avg `0.219` n `763`
- 1h: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.2617` n `229`; crypto_major avg `-0.287` n `8`; equity avg `-0.3815` n `91`; fx avg `0.0764` n `6`; index avg `-0.05` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.164` n `763`
- 4h: commodity avg `0.1451` n `12`; crypto_alt avg `-0.8511` n `229`; crypto_major avg `-0.7918` n `8`; equity avg `-0.4645` n `91`; fx avg `0.0855` n `6`; index avg `-0.0587` n `25`; metal avg `-0.1501` n `20`; unknown avg `0.1622` n `763`
- 24h: commodity avg `0.9251` n `12`; crypto_alt avg `-2.7004` n `229`; crypto_major avg `-1.6991` n `8`; equity avg `-3.2983` n `91`; fx avg `-0.1883` n `6`; index avg `-0.5715` n `25`; metal avg `-0.6366` n `20`; unknown avg `-0.0473` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
