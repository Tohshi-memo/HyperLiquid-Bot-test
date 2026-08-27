# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T23:07:26.725347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.0014` n `231`; crypto_major avg `0.0503` n `8`; equity avg `-0.0518` n `127`; fx avg `0.0049` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0047` n `20`; unknown avg `-0.0769` n `792`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `-0.1191` n `231`; crypto_major avg `-0.1043` n `8`; equity avg `-0.0229` n `127`; fx avg `0.0101` n `6`; index avg `-0.0063` n `26`; metal avg `0.0374` n `20`; unknown avg `-0.0098` n `792`
- 4h: commodity avg `-0.0729` n `12`; crypto_alt avg `0.0701` n `231`; crypto_major avg `-0.1459` n `8`; equity avg `-0.1798` n `127`; fx avg `0.0069` n `6`; index avg `0.0324` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.1171` n `792`
- 24h: commodity avg `0.3712` n `12`; crypto_alt avg `1.6197` n `231`; crypto_major avg `3.0056` n `8`; equity avg `-0.2744` n `127`; fx avg `-0.0152` n `6`; index avg `-0.1217` n `26`; metal avg `0.1171` n `20`; unknown avg `0.9349` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
