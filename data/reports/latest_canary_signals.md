# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T19:52:18.945391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0629` n `12`; crypto_alt avg `-0.1451` n `228`; crypto_major avg `-0.0371` n `8`; equity avg `-0.0656` n `66`; fx avg `0.0312` n `6`; index avg `-0.012` n `23`; metal avg `-0.0263` n `18`; unknown avg `-0.1961` n `383`
- 1h: commodity avg `-0.1358` n `12`; crypto_alt avg `-0.2916` n `228`; crypto_major avg `-0.0738` n `8`; equity avg `-0.3828` n `66`; fx avg `0.0351` n `6`; index avg `-0.1557` n `23`; metal avg `-0.23` n `18`; unknown avg `-0.0668` n `383`
- 4h: commodity avg `0.352` n `12`; crypto_alt avg `0.1906` n `228`; crypto_major avg `0.1512` n `8`; equity avg `0.692` n `66`; fx avg `0.0077` n `6`; index avg `0.3649` n `23`; metal avg `-0.1245` n `18`; unknown avg `1.0779` n `383`
- 24h: commodity avg `1.3863` n `12`; crypto_alt avg `-0.3691` n `228`; crypto_major avg `-0.1954` n `8`; equity avg `0.0963` n `66`; fx avg `0.0936` n `6`; index avg `-0.5131` n `23`; metal avg `-2.4421` n `18`; unknown avg `0.959` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
