# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T07:37:26.068148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `-0.1475` n `237`; crypto_major avg `-0.0986` n `8`; equity avg `-0.0015` n `151`; fx avg `0.0079` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.032` n `1191`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `-0.4411` n `237`; crypto_major avg `-0.2514` n `8`; equity avg `-0.0104` n `151`; fx avg `0.0` n `6`; index avg `0.0137` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.0214` n `1189`
- 4h: commodity avg `-0.048` n `13`; crypto_alt avg `-0.8142` n `237`; crypto_major avg `-0.4871` n `8`; equity avg `0.136` n `151`; fx avg `0.0037` n `6`; index avg `0.0405` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.2101` n `1167`
- 24h: commodity avg `0.0927` n `13`; crypto_alt avg `-2.8051` n `236`; crypto_major avg `-1.107` n `8`; equity avg `-0.846` n `151`; fx avg `-0.0473` n `6`; index avg `-0.0963` n `26`; metal avg `-0.0675` n `20`; unknown avg `3.9603` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1712`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1324`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0838`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
