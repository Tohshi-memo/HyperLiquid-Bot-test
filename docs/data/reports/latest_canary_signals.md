# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T19:37:25.448818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `0.1166` n `235`; crypto_major avg `-0.0767` n `8`; equity avg `0.0068` n `143`; fx avg `0.001` n `6`; index avg `0.0004` n `26`; metal avg `0.0082` n `20`; unknown avg `-0.2579` n `1076`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `0.0696` n `235`; crypto_major avg `-0.1277` n `8`; equity avg `0.0145` n `143`; fx avg `0.0006` n `6`; index avg `0.0031` n `26`; metal avg `0.01` n `20`; unknown avg `0.4742` n `1068`
- 4h: commodity avg `-0.0263` n `13`; crypto_alt avg `0.2972` n `235`; crypto_major avg `0.229` n `8`; equity avg `0.092` n `143`; fx avg `-0.0157` n `6`; index avg `0.0257` n `26`; metal avg `0.0109` n `20`; unknown avg `0.85` n `1062`
- 24h: commodity avg `0.1743` n `13`; crypto_alt avg `2.5263` n `235`; crypto_major avg `1.3412` n `8`; equity avg `0.0224` n `143`; fx avg `-0.0568` n `6`; index avg `0.0296` n `26`; metal avg `-0.0472` n `20`; unknown avg `-0.1203` n `862`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
