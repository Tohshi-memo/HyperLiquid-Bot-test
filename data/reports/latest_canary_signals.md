# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T20:22:27.776929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `-0.0594` n `239`; crypto_major avg `0.0158` n `8`; equity avg `0.0648` n `162`; fx avg `0.006` n `6`; index avg `0.0049` n `27`; metal avg `-0.0008` n `20`; unknown avg `5.6603` n `1260`
- 1h: commodity avg `0.0571` n `13`; crypto_alt avg `0.1623` n `239`; crypto_major avg `0.1689` n `8`; equity avg `-0.0347` n `162`; fx avg `-0.0023` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0368` n `20`; unknown avg `0.9636` n `1246`
- 4h: commodity avg `-0.1212` n `13`; crypto_alt avg `0.6519` n `239`; crypto_major avg `1.0674` n `8`; equity avg `1.5451` n `162`; fx avg `-0.0492` n `6`; index avg `0.1708` n `27`; metal avg `-0.0813` n `20`; unknown avg `7.1946` n `1246`
- 24h: commodity avg `-0.3076` n `13`; crypto_alt avg `0.2586` n `239`; crypto_major avg `-1.2345` n `8`; equity avg `-2.1321` n `162`; fx avg `-0.0648` n `6`; index avg `-0.1645` n `27`; metal avg `-0.3296` n `20`; unknown avg `1.7125` n `1085`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
