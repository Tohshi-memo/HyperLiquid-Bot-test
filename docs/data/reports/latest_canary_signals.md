# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T15:52:22.754120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0743` n `12`; crypto_alt avg `-0.0492` n `228`; crypto_major avg `-0.0606` n `8`; equity avg `0.0659` n `66`; fx avg `-0.0093` n `6`; index avg `0.0904` n `23`; metal avg `-0.1059` n `18`; unknown avg `0.2445` n `383`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `0.1757` n `228`; crypto_major avg `0.3746` n `8`; equity avg `0.8305` n `66`; fx avg `-0.0149` n `6`; index avg `0.3992` n `23`; metal avg `0.1036` n `18`; unknown avg `0.3692` n `383`
- 4h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.2851` n `228`; crypto_major avg `-0.0875` n `8`; equity avg `0.1383` n `66`; fx avg `-0.0171` n `6`; index avg `-0.3419` n `23`; metal avg `-1.3572` n `18`; unknown avg `-0.2624` n `383`
- 24h: commodity avg `0.7399` n `12`; crypto_alt avg `0.5855` n `228`; crypto_major avg `0.9666` n `8`; equity avg `-0.2925` n `66`; fx avg `0.061` n `6`; index avg `-0.7458` n `23`; metal avg `-1.8696` n `18`; unknown avg `-0.1977` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
