# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T16:37:26.818255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3852` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1399` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0527` n `12`; crypto_alt avg `0.4641` n `231`; crypto_major avg `0.553` n `8`; equity avg `0.0943` n `127`; fx avg `0.0032` n `6`; index avg `0.0401` n `26`; metal avg `0.0433` n `20`; unknown avg `0.2905` n `793`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `-2.0361` n `231`; crypto_major avg `-1.579` n `8`; equity avg `-1.092` n `127`; fx avg `-0.0123` n `6`; index avg `-0.1938` n `26`; metal avg `-0.5661` n `20`; unknown avg `3.1767` n `793`
- 4h: commodity avg `0.1687` n `12`; crypto_alt avg `-1.9141` n `231`; crypto_major avg `-1.2702` n `8`; equity avg `-1.4435` n `127`; fx avg `-0.0103` n `6`; index avg `-0.1303` n `26`; metal avg `-0.668` n `20`; unknown avg `-0.5388` n `792`
- 24h: commodity avg `-0.0641` n `12`; crypto_alt avg `-3.982` n `231`; crypto_major avg `-3.2542` n `8`; equity avg `-1.9287` n `127`; fx avg `-0.0878` n `6`; index avg `-0.1275` n `26`; metal avg `-0.148` n `20`; unknown avg `-0.1894` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
