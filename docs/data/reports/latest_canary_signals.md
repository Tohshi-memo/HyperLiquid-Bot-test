# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T06:37:20.620524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1775` n `12`; crypto_alt avg `-0.0856` n `228`; crypto_major avg `-0.1478` n `8`; equity avg `-0.0715` n `66`; fx avg `-0.0164` n `6`; index avg `-0.0538` n `23`; metal avg `-0.3349` n `18`; unknown avg `-0.0076` n `385`
- 1h: commodity avg `0.1003` n `12`; crypto_alt avg `-0.0502` n `228`; crypto_major avg `-0.1425` n `8`; equity avg `-0.2039` n `66`; fx avg `-0.0054` n `6`; index avg `-0.1099` n `23`; metal avg `-0.0191` n `18`; unknown avg `0.1565` n `374`
- 4h: commodity avg `0.2371` n `12`; crypto_alt avg `-0.3688` n `228`; crypto_major avg `-0.1501` n `8`; equity avg `0.0042` n `66`; fx avg `0.049` n `6`; index avg `0.0401` n `23`; metal avg `-0.5524` n `18`; unknown avg `0.9454` n `374`
- 24h: commodity avg `-1.9132` n `12`; crypto_alt avg `2.3796` n `228`; crypto_major avg `2.8307` n `8`; equity avg `2.059` n `66`; fx avg `0.0906` n `6`; index avg `1.5229` n `23`; metal avg `0.5599` n `18`; unknown avg `5.8215` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
