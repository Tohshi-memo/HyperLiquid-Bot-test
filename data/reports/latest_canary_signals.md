# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T11:22:33.335417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0888` n `12`; crypto_alt avg `0.0847` n `228`; crypto_major avg `-0.0392` n `8`; equity avg `-0.0411` n `79`; fx avg `0.0014` n `6`; index avg `-0.0025` n `23`; metal avg `-0.0818` n `20`; unknown avg `0.1249` n `722`
- 1h: commodity avg `-0.074` n `12`; crypto_alt avg `0.4542` n `228`; crypto_major avg `0.2504` n `8`; equity avg `0.0588` n `79`; fx avg `-0.0172` n `6`; index avg `0.0289` n `23`; metal avg `-0.0294` n `18`; unknown avg `0.5562` n `701`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `0.345` n `228`; crypto_major avg `0.2199` n `8`; equity avg `0.1366` n `79`; fx avg `-0.0025` n `6`; index avg `0.0814` n `23`; metal avg `-0.0483` n `18`; unknown avg `0.3937` n `693`
- 24h: commodity avg `-0.2043` n `12`; crypto_alt avg `0.352` n `228`; crypto_major avg `0.463` n `8`; equity avg `0.0511` n `79`; fx avg `0.0301` n `6`; index avg `0.0933` n `23`; metal avg `0.5422` n `18`; unknown avg `0.7081` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
