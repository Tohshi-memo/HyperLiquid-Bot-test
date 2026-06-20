# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T12:37:28.611763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.2248` n `228`; crypto_major avg `-0.2002` n `8`; equity avg `-0.0407` n `78`; fx avg `-0.0027` n `6`; index avg `-0.0015` n `23`; metal avg `0.0103` n `18`; unknown avg `-0.1115` n `701`
- 1h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.1248` n `228`; crypto_major avg `-0.0799` n `8`; equity avg `0.034` n `78`; fx avg `0.0043` n `6`; index avg `0.0022` n `23`; metal avg `0.0107` n `18`; unknown avg `0.0136` n `573`
- 4h: commodity avg `-0.1043` n `12`; crypto_alt avg `0.0422` n `228`; crypto_major avg `0.1625` n `8`; equity avg `-0.1579` n `78`; fx avg `0.0326` n `6`; index avg `-0.0097` n `23`; metal avg `0.0038` n `18`; unknown avg `-0.3436` n `573`
- 24h: commodity avg `0.417` n `12`; crypto_alt avg `-3.194` n `228`; crypto_major avg `-3.4215` n `8`; equity avg `1.1423` n `78`; fx avg `-0.0677` n `6`; index avg `0.296` n `23`; metal avg `-4.0921` n `18`; unknown avg `-0.1623` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
