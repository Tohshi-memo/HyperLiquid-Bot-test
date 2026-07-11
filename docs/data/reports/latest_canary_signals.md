# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T03:52:28.117500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.0439` n `229`; crypto_major avg `-0.0264` n `8`; equity avg `-0.0144` n `92`; fx avg `0.0006` n `6`; index avg `0.0005` n `25`; metal avg `-0.016` n `20`; unknown avg `-0.0902` n `763`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `0.0104` n `229`; crypto_major avg `0.0543` n `8`; equity avg `0.005` n `92`; fx avg `0.0025` n `6`; index avg `0.0067` n `25`; metal avg `0.015` n `20`; unknown avg `-0.151` n `763`
- 4h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.1847` n `229`; crypto_major avg `-0.0168` n `8`; equity avg `0.03` n `92`; fx avg `0.0048` n `6`; index avg `0.0027` n `25`; metal avg `0.0191` n `20`; unknown avg `3.1375` n `763`
- 24h: commodity avg `-0.3456` n `12`; crypto_alt avg `0.4658` n `229`; crypto_major avg `-0.1981` n `8`; equity avg `-0.7122` n `92`; fx avg `-0.1701` n `6`; index avg `0.0294` n `25`; metal avg `-0.0323` n `20`; unknown avg `3.3574` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
