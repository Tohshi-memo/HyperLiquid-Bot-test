# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T23:53:26.881122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `0.1161` n `237`; crypto_major avg `0.1222` n `8`; equity avg `0.1751` n `151`; fx avg `-0.0182` n `6`; index avg `0.0273` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.0689` n `1199`
- 1h: commodity avg `0.0303` n `13`; crypto_alt avg `-0.108` n `237`; crypto_major avg `-0.2357` n `8`; equity avg `-0.0333` n `151`; fx avg `-0.0251` n `6`; index avg `0.0015` n `26`; metal avg `-0.0374` n `20`; unknown avg `0.1661` n `1165`
- 4h: commodity avg `0.0085` n `13`; crypto_alt avg `0.4247` n `237`; crypto_major avg `0.3787` n `8`; equity avg `1.4371` n `151`; fx avg `-0.0373` n `6`; index avg `0.1892` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.1834` n `1037`
- 24h: commodity avg `-0.0093` n `13`; crypto_alt avg `2.3594` n `237`; crypto_major avg `1.608` n `8`; equity avg `1.6369` n `151`; fx avg `0.0002` n `6`; index avg `0.1858` n `26`; metal avg `0.0735` n `20`; unknown avg `211.3703` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
