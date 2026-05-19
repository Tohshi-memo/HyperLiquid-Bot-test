# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T07:07:16.885748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.0669` n `228`; crypto_major avg `-0.0002` n `8`; equity avg `0.1093` n `66`; fx avg `0.0018` n `6`; index avg `0.0119` n `23`; metal avg `-0.014` n `18`; unknown avg `0.0091` n `383`
- 1h: commodity avg `0.1719` n `12`; crypto_alt avg `0.1038` n `228`; crypto_major avg `0.0376` n `8`; equity avg `0.379` n `66`; fx avg `-0.0447` n `6`; index avg `0.147` n `23`; metal avg `0.0299` n `18`; unknown avg `0.1755` n `383`
- 4h: commodity avg `0.2893` n `12`; crypto_alt avg `0.5651` n `228`; crypto_major avg `0.4059` n `8`; equity avg `0.3892` n `66`; fx avg `0.0084` n `6`; index avg `0.1303` n `23`; metal avg `-0.0998` n `18`; unknown avg `0.483` n `363`
- 24h: commodity avg `0.625` n `12`; crypto_alt avg `1.6938` n `228`; crypto_major avg `0.8085` n `8`; equity avg `-0.7157` n `66`; fx avg `0.2803` n `6`; index avg `-0.3241` n `23`; metal avg `0.0876` n `18`; unknown avg `0.9192` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
