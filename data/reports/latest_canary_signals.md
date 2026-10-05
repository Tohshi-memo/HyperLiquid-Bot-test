# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T06:22:26.837263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `13`; crypto_alt avg `0.016` n `235`; crypto_major avg `0.0727` n `8`; equity avg `0.0552` n `144`; fx avg `0.0005` n `6`; index avg `0.0063` n `26`; metal avg `0.0581` n `20`; unknown avg `-0.0179` n `1079`
- 1h: commodity avg `0.0009` n `13`; crypto_alt avg `0.5438` n `235`; crypto_major avg `0.5754` n `8`; equity avg `0.1189` n `144`; fx avg `-0.0333` n `6`; index avg `0.0241` n `26`; metal avg `0.1122` n `20`; unknown avg `2.7122` n `1061`
- 4h: commodity avg `-0.0339` n `13`; crypto_alt avg `-0.4859` n `235`; crypto_major avg `-0.5799` n `8`; equity avg `-0.2043` n `144`; fx avg `-0.0545` n `6`; index avg `-0.0761` n `26`; metal avg `-0.0084` n `20`; unknown avg `1.0774` n `970`
- 24h: commodity avg `-0.354` n `13`; crypto_alt avg `0.5456` n `235`; crypto_major avg `1.1002` n `8`; equity avg `0.3109` n `144`; fx avg `-0.0824` n `6`; index avg `-0.0371` n `26`; metal avg `0.1819` n `20`; unknown avg `0.1445` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
