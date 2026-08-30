# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T00:37:23.599831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `-0.051` n `231`; crypto_major avg `-0.0039` n `8`; equity avg `0.0127` n `128`; fx avg `-0.0025` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0132` n `20`; unknown avg `4.0304` n `793`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `0.0175` n `231`; crypto_major avg `0.0515` n `8`; equity avg `0.0062` n `128`; fx avg `0.0123` n `6`; index avg `0.0104` n `26`; metal avg `-0.0022` n `20`; unknown avg `4.0045` n `793`
- 4h: commodity avg `0.0067` n `12`; crypto_alt avg `0.0396` n `231`; crypto_major avg `0.1712` n `8`; equity avg `0.032` n `128`; fx avg `0.0132` n `6`; index avg `0.0235` n `26`; metal avg `-0.0046` n `20`; unknown avg `3.8901` n `774`
- 24h: commodity avg `0.0232` n `12`; crypto_alt avg `0.1828` n `231`; crypto_major avg `0.9066` n `8`; equity avg `0.4039` n `128`; fx avg `-0.0062` n `6`; index avg `0.1073` n `26`; metal avg `0.0878` n `20`; unknown avg `0.1855` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
