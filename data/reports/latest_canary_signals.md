# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T09:52:17.930700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.085` n `12`; crypto_alt avg `0.1233` n `228`; crypto_major avg `0.0249` n `8`; equity avg `0.0191` n `66`; fx avg `0.0394` n `6`; index avg `-0.0621` n `23`; metal avg `0.0346` n `18`; unknown avg `-0.0117` n `383`
- 1h: commodity avg `0.1107` n `12`; crypto_alt avg `-0.5214` n `228`; crypto_major avg `-0.574` n `8`; equity avg `-0.6239` n `66`; fx avg `-0.0149` n `6`; index avg `-0.3685` n `23`; metal avg `-0.1262` n `18`; unknown avg `0.5735` n `383`
- 4h: commodity avg `0.0988` n `12`; crypto_alt avg `-0.4889` n `228`; crypto_major avg `-0.384` n `8`; equity avg `-0.3459` n `66`; fx avg `-0.0388` n `6`; index avg `-0.317` n `23`; metal avg `-0.0497` n `18`; unknown avg `0.8562` n `363`
- 24h: commodity avg `0.6377` n `12`; crypto_alt avg `1.3364` n `228`; crypto_major avg `0.7247` n `8`; equity avg `-1.9027` n `66`; fx avg `0.2459` n `6`; index avg `-0.9542` n `23`; metal avg `-0.147` n `18`; unknown avg `1.7686` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
