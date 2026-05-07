# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T20:37:23.594821+00:00`
- Correlation status: `ready`
- Asset price records: `582`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4819` n `12`; crypto_alt avg `-0.3042` n `228`; crypto_major avg `-0.1541` n `8`; equity avg `0.0909` n `65`; fx avg `-0.0085` n `5`; index avg `-0.0978` n `23`; metal avg `-0.2795` n `18`; unknown avg `0.7443` n `365`
- 1h: commodity avg `0.4049` n `12`; crypto_alt avg `-0.1272` n `228`; crypto_major avg `-0.0919` n `8`; equity avg `0.3359` n `65`; fx avg `-0.0083` n `5`; index avg `-0.0475` n `23`; metal avg `-0.0605` n `18`; unknown avg `0.9041` n `365`
- 4h: commodity avg `0.7548` n `12`; crypto_alt avg `0.8269` n `228`; crypto_major avg `0.0503` n `8`; equity avg `-0.1801` n `65`; fx avg `-0.0204` n `5`; index avg `-0.379` n `23`; metal avg `-0.5175` n `18`; unknown avg `0.4509` n `365`
- 24h: commodity avg `0.7348` n `12`; crypto_alt avg `1.313` n `228`; crypto_major avg `-1.8335` n `8`; equity avg `-1.2508` n `65`; fx avg `0.1728` n `5`; index avg `-0.9212` n `23`; metal avg `0.1181` n `18`; unknown avg `0.4114` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `578`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `578`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `578`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `578`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `574`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `574`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0932`, n `574`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0887`, n `574`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0828`, n `574`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0783`, n `574`, weak_sample_signal
