# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T08:37:28.587506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `13`; crypto_alt avg `-0.0909` n `237`; crypto_major avg `-0.0825` n `8`; equity avg `-0.2647` n `151`; fx avg `0.015` n `6`; index avg `-0.0325` n `26`; metal avg `0.0087` n `20`; unknown avg `0.3094` n `1200`
- 1h: commodity avg `0.0222` n `13`; crypto_alt avg `-0.1548` n `237`; crypto_major avg `0.018` n `8`; equity avg `-0.3778` n `151`; fx avg `0.0265` n `6`; index avg `-0.0636` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.4974` n `1182`
- 4h: commodity avg `-0.0679` n `13`; crypto_alt avg `0.4384` n `237`; crypto_major avg `0.458` n `8`; equity avg `-0.2738` n `151`; fx avg `0.0217` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0304` n `20`; unknown avg `1.4548` n `1158`
- 24h: commodity avg `-0.2404` n `13`; crypto_alt avg `3.4135` n `237`; crypto_major avg `2.5003` n `8`; equity avg `2.1368` n `151`; fx avg `0.0157` n `6`; index avg `0.257` n `26`; metal avg `-0.1852` n `20`; unknown avg `5293.0576` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
