# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T09:37:33.387594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.072` n `13`; crypto_alt avg `-0.275` n `237`; crypto_major avg `-0.2673` n `8`; equity avg `-0.0296` n `151`; fx avg `0.0078` n `6`; index avg `0.0087` n `26`; metal avg `-0.0244` n `20`; unknown avg `0.0103` n `1198`
- 1h: commodity avg `0.1102` n `13`; crypto_alt avg `-0.3822` n `237`; crypto_major avg `-0.3066` n `8`; equity avg `-0.4755` n `151`; fx avg `-0.0113` n `6`; index avg `-0.0884` n `26`; metal avg `-0.0876` n `20`; unknown avg `-0.2477` n `1196`
- 4h: commodity avg `0.3136` n `13`; crypto_alt avg `-0.6416` n `237`; crypto_major avg `-0.5932` n `8`; equity avg `-0.2082` n `151`; fx avg `-0.0098` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0438` n `20`; unknown avg `3.8481` n `1160`
- 24h: commodity avg `0.3467` n `13`; crypto_alt avg `-0.8747` n `237`; crypto_major avg `-1.5585` n `8`; equity avg `-1.7678` n `151`; fx avg `-0.0015` n `6`; index avg `-0.2559` n `26`; metal avg `-0.2598` n `20`; unknown avg `4.0946` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
