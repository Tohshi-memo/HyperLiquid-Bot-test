# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T12:52:32.405497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0288` n `12`; crypto_alt avg `0.137` n `228`; crypto_major avg `0.1898` n `8`; equity avg `-0.0516` n `79`; fx avg `-0.0` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0179` n `20`; unknown avg `-0.0238` n `722`
- 1h: commodity avg `-0.1703` n `12`; crypto_alt avg `0.3598` n `228`; crypto_major avg `0.3846` n `8`; equity avg `0.1445` n `79`; fx avg `0.0345` n `6`; index avg `0.0233` n `23`; metal avg `-0.0171` n `20`; unknown avg `0.064` n `722`
- 4h: commodity avg `-0.2563` n `12`; crypto_alt avg `1.1731` n `228`; crypto_major avg `1.155` n `8`; equity avg `0.4392` n `79`; fx avg `0.0659` n `6`; index avg `0.1308` n `23`; metal avg `0.0143` n `18`; unknown avg `0.7466` n `701`
- 24h: commodity avg `-0.5899` n `12`; crypto_alt avg `1.1209` n `228`; crypto_major avg `1.478` n `8`; equity avg `0.2058` n `79`; fx avg `0.1637` n `6`; index avg `0.1519` n `23`; metal avg `0.4236` n `18`; unknown avg `0.669` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
