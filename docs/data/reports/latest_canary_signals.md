# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T14:07:35.543162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1101` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `0.0056` n `233`; crypto_major avg `-0.1028` n `8`; equity avg `-0.049` n `135`; fx avg `-0.0119` n `6`; index avg `-0.0195` n `26`; metal avg `-0.0946` n `20`; unknown avg `-0.1565` n `794`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `0.3427` n `233`; crypto_major avg `0.1465` n `8`; equity avg `0.3248` n `135`; fx avg `-0.0063` n `6`; index avg `-0.0572` n `26`; metal avg `0.0391` n `20`; unknown avg `3066.3147` n `794`
- 4h: commodity avg `0.3629` n `12`; crypto_alt avg `-0.7625` n `233`; crypto_major avg `-1.4294` n `8`; equity avg `-1.1174` n `135`; fx avg `-0.0131` n `6`; index avg `-0.3193` n `26`; metal avg `-0.7161` n `20`; unknown avg `0.2151` n `788`
- 24h: commodity avg `0.4543` n `12`; crypto_alt avg `-4.8888` n `233`; crypto_major avg `-4.0179` n `8`; equity avg `-2.5525` n `135`; fx avg `0.0869` n `6`; index avg `-0.4737` n `26`; metal avg `-1.094` n `20`; unknown avg `-0.1955` n `672`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
