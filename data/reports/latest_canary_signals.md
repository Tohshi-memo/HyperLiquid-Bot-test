# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T05:52:19.866051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0508` n `12`; crypto_alt avg `0.2501` n `228`; crypto_major avg `0.0868` n `8`; equity avg `0.0248` n `67`; fx avg `0.0089` n `6`; index avg `0.0879` n `23`; metal avg `-0.0003` n `18`; unknown avg `0.9481` n `386`
- 1h: commodity avg `0.1966` n `12`; crypto_alt avg `0.2919` n `228`; crypto_major avg `0.0692` n `8`; equity avg `0.0668` n `67`; fx avg `0.0154` n `6`; index avg `0.1069` n `23`; metal avg `0.1878` n `18`; unknown avg `1.0531` n `386`
- 4h: commodity avg `0.0722` n `12`; crypto_alt avg `0.8855` n `228`; crypto_major avg `0.1778` n `8`; equity avg `0.3975` n `67`; fx avg `0.0657` n `6`; index avg `0.2191` n `23`; metal avg `0.2239` n `18`; unknown avg `0.3255` n `386`
- 24h: commodity avg `-0.7147` n `12`; crypto_alt avg `2.4449` n `228`; crypto_major avg `0.5275` n `8`; equity avg `1.5248` n `66`; fx avg `0.1182` n `6`; index avg `0.7496` n `23`; metal avg `1.0657` n `18`; unknown avg `3.0047` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0433`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
