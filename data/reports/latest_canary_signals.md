# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T22:55:59.092261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0824` n `230`; crypto_major avg `-0.0089` n `8`; equity avg `-0.0232` n `114`; fx avg `0.0042` n `6`; index avg `0.0047` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.0305` n `791`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.1524` n `230`; crypto_major avg `-0.0846` n `8`; equity avg `-0.0325` n `114`; fx avg `-0.0019` n `6`; index avg `0.0046` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.1357` n `791`
- 4h: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.1314` n `230`; crypto_major avg `0.063` n `8`; equity avg `0.0169` n `114`; fx avg `0.0045` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0136` n `791`
- 24h: commodity avg `-0.0873` n `12`; crypto_alt avg `0.6966` n `230`; crypto_major avg `0.5324` n `8`; equity avg `0.1448` n `114`; fx avg `0.0199` n `6`; index avg `-0.005` n `25`; metal avg `0.0139` n `20`; unknown avg `0.0775` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
