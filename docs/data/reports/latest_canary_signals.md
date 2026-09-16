# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T10:52:29.643563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0322` n `12`; crypto_alt avg `0.0231` n `234`; crypto_major avg `-0.0073` n `8`; equity avg `-0.0093` n `137`; fx avg `0.0008` n `6`; index avg `0.0011` n `27`; metal avg `-0.0013` n `20`; unknown avg `-0.1974` n `919`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0241` n `234`; crypto_major avg `0.0083` n `8`; equity avg `-0.0476` n `137`; fx avg `0.0028` n `6`; index avg `0.0116` n `27`; metal avg `0.083` n `20`; unknown avg `0.8233` n `917`
- 4h: commodity avg `0.0293` n `12`; crypto_alt avg `-0.0323` n `234`; crypto_major avg `0.0425` n `8`; equity avg `0.1251` n `137`; fx avg `-0.0128` n `6`; index avg `0.0141` n `27`; metal avg `0.0316` n `20`; unknown avg `6.669` n `911`
- 24h: commodity avg `0.1779` n `12`; crypto_alt avg `-2.8443` n `234`; crypto_major avg `-2.908` n `8`; equity avg `-0.2274` n `137`; fx avg `0.1181` n `6`; index avg `0.0757` n `27`; metal avg `0.4699` n `20`; unknown avg `18892.7189` n `798`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
