# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T17:37:38.034056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7819` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.1868` n `228`; crypto_major avg `-0.1018` n `8`; equity avg `-0.0453` n `85`; fx avg `0.0003` n `6`; index avg `-0.0007` n `23`; metal avg `-0.1317` n `20`; unknown avg `0.0171` n `717`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.294` n `228`; crypto_major avg `-0.1524` n `8`; equity avg `0.1655` n `85`; fx avg `-0.0089` n `6`; index avg `0.025` n `23`; metal avg `-0.101` n `20`; unknown avg `-0.1459` n `717`
- 4h: commodity avg `-0.0701` n `12`; crypto_alt avg `-1.5381` n `228`; crypto_major avg `-1.8624` n `8`; equity avg `-1.0858` n `85`; fx avg `-0.058` n `6`; index avg `-0.0805` n `23`; metal avg `-0.374` n `20`; unknown avg `0.988` n `716`
- 24h: commodity avg `-0.8445` n `12`; crypto_alt avg `-0.5861` n `228`; crypto_major avg `-0.2721` n `8`; equity avg `-0.6506` n `85`; fx avg `0.0405` n `6`; index avg `0.1317` n `23`; metal avg `0.082` n `18`; unknown avg `0.9486` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
