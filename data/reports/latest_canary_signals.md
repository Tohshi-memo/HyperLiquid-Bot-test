# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T14:22:34.895631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0334` n `12`; crypto_alt avg `0.0513` n `232`; crypto_major avg `-0.0437` n `8`; equity avg `-0.0066` n `134`; fx avg `-0.0314` n `6`; index avg `-0.009` n `26`; metal avg `0.012` n `20`; unknown avg `-0.1059` n `796`
- 1h: commodity avg `0.0427` n `12`; crypto_alt avg `-0.5517` n `232`; crypto_major avg `-0.7865` n `8`; equity avg `-0.0682` n `134`; fx avg `-0.0163` n `6`; index avg `-0.0058` n `26`; metal avg `0.0832` n `20`; unknown avg `0.5171` n `794`
- 4h: commodity avg `0.2393` n `12`; crypto_alt avg `0.7231` n `232`; crypto_major avg `-0.088` n `8`; equity avg `-0.0845` n `134`; fx avg `-0.0027` n `6`; index avg `-0.0198` n `26`; metal avg `0.063` n `20`; unknown avg `6683.8868` n `748`
- 24h: commodity avg `0.178` n `12`; crypto_alt avg `1.3754` n `232`; crypto_major avg `-0.3221` n `8`; equity avg `0.4554` n `134`; fx avg `-0.1062` n `6`; index avg `0.0558` n `26`; metal avg `-0.0333` n `20`; unknown avg `0.6714` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
