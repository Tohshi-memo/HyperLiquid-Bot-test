# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T05:52:31.126991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1244` n `228`; crypto_major avg `-0.1637` n `8`; equity avg `-0.3115` n `74`; fx avg `-0.0136` n `6`; index avg `-0.1955` n `23`; metal avg `-0.025` n `18`; unknown avg `-0.4362` n `557`
- 1h: commodity avg `-0.0859` n `12`; crypto_alt avg `-0.6561` n `228`; crypto_major avg `-0.5856` n `8`; equity avg `-0.653` n `74`; fx avg `-0.025` n `6`; index avg `-0.4059` n `23`; metal avg `-0.3527` n `18`; unknown avg `-0.6608` n `557`
- 4h: commodity avg `-0.4746` n `12`; crypto_alt avg `-0.1146` n `228`; crypto_major avg `0.0745` n `8`; equity avg `-0.4207` n `74`; fx avg `-0.0006` n `6`; index avg `-0.2649` n `23`; metal avg `-0.2835` n `18`; unknown avg `0.2134` n `557`
- 24h: commodity avg `-2.2445` n `12`; crypto_alt avg `1.4959` n `228`; crypto_major avg `1.902` n `8`; equity avg `3.1204` n `74`; fx avg `-0.0262` n `6`; index avg `1.6045` n `23`; metal avg `2.3457` n `18`; unknown avg `1.6715` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
