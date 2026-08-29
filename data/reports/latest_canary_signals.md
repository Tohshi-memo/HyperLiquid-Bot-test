# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T12:37:32.481644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.0851` n `231`; crypto_major avg `-0.1275` n `8`; equity avg `-0.0225` n `127`; fx avg `-0.0045` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0055` n `20`; unknown avg `-0.0087` n `791`
- 1h: commodity avg `0.0098` n `12`; crypto_alt avg `0.1067` n `231`; crypto_major avg `-0.0077` n `8`; equity avg `-0.0567` n `127`; fx avg `-0.0049` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.2939` n `779`
- 4h: commodity avg `0.0296` n `12`; crypto_alt avg `0.1209` n `231`; crypto_major avg `0.1278` n `8`; equity avg `-0.0253` n `127`; fx avg `-0.0342` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.4681` n `759`
- 24h: commodity avg `0.2166` n `12`; crypto_alt avg `-2.0576` n `231`; crypto_major avg `-1.8777` n `8`; equity avg `-1.3839` n `127`; fx avg `-0.0681` n `6`; index avg `-0.1379` n `26`; metal avg `-0.7701` n `20`; unknown avg `-0.6106` n `742`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
