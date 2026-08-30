# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T19:52:23.118292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.107` n `12`; crypto_alt avg `-0.1342` n `231`; crypto_major avg `-0.1201` n `8`; equity avg `-0.0376` n `128`; fx avg `-0.0006` n `6`; index avg `0.0083` n `26`; metal avg `-0.0118` n `20`; unknown avg `0.1158` n `789`
- 1h: commodity avg `0.255` n `12`; crypto_alt avg `-0.5233` n `231`; crypto_major avg `-0.5719` n `8`; equity avg `-0.0752` n `128`; fx avg `-0.0103` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.5009` n `789`
- 4h: commodity avg `0.3121` n `12`; crypto_alt avg `0.4857` n `231`; crypto_major avg `0.1614` n `8`; equity avg `0.049` n `128`; fx avg `-0.003` n `6`; index avg `0.0038` n `26`; metal avg `0.0088` n `20`; unknown avg `0.2883` n `789`
- 24h: commodity avg `0.3116` n `12`; crypto_alt avg `1.368` n `231`; crypto_major avg `0.6542` n `8`; equity avg `0.1868` n `128`; fx avg `0.0353` n `6`; index avg `0.054` n `26`; metal avg `0.0938` n `20`; unknown avg `0.1754` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
