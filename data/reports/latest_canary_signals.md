# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T05:52:27.734473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0451` n `233`; crypto_major avg `-0.0358` n `8`; equity avg `-0.1197` n `134`; fx avg `0.022` n `6`; index avg `-0.0229` n `26`; metal avg `0.0115` n `20`; unknown avg `29.278` n `797`
- 1h: commodity avg `-0.1057` n `12`; crypto_alt avg `0.3397` n `233`; crypto_major avg `0.1077` n `8`; equity avg `0.0472` n `134`; fx avg `0.0352` n `6`; index avg `0.0187` n `26`; metal avg `0.112` n `20`; unknown avg `6.3503` n `795`
- 4h: commodity avg `-0.1497` n `12`; crypto_alt avg `1.0757` n `233`; crypto_major avg `0.7725` n `8`; equity avg `0.4103` n `134`; fx avg `-0.0011` n `6`; index avg `0.1199` n `26`; metal avg `0.1467` n `20`; unknown avg `0.0597` n `789`
- 24h: commodity avg `-0.0147` n `12`; crypto_alt avg `-3.0991` n `233`; crypto_major avg `-1.9759` n `8`; equity avg `-0.8912` n `134`; fx avg `0.0471` n `6`; index avg `-0.1222` n `26`; metal avg `0.3866` n `20`; unknown avg `0.3658` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
