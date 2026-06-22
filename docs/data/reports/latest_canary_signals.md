# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T07:52:28.899680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0806` n `12`; crypto_alt avg `-0.1171` n `228`; crypto_major avg `-0.1113` n `8`; equity avg `-0.0296` n `79`; fx avg `-0.012` n `6`; index avg `-0.0096` n `23`; metal avg `-0.0584` n `18`; unknown avg `0.0392` n `693`
- 1h: commodity avg `0.1589` n `12`; crypto_alt avg `0.3678` n `228`; crypto_major avg `0.6386` n `8`; equity avg `0.1111` n `79`; fx avg `0.0175` n `6`; index avg `-0.0022` n `23`; metal avg `-0.2536` n `18`; unknown avg `0.084` n `693`
- 4h: commodity avg `0.1571` n `12`; crypto_alt avg `0.2999` n `228`; crypto_major avg `0.7148` n `8`; equity avg `0.287` n `79`; fx avg `-0.005` n `6`; index avg `0.0113` n `23`; metal avg `0.2833` n `18`; unknown avg `0.2053` n `661`
- 24h: commodity avg `-0.0759` n `12`; crypto_alt avg `-0.0015` n `228`; crypto_major avg `-0.0562` n `8`; equity avg `-0.2835` n `79`; fx avg `0.0121` n `6`; index avg `0.0087` n `23`; metal avg `0.3491` n `18`; unknown avg `0.0733` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
