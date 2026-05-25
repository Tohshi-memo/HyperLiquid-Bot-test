# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T06:07:17.471962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1213` n `12`; crypto_alt avg `0.0357` n `228`; crypto_major avg `0.0151` n `8`; equity avg `-0.0999` n `67`; fx avg `-0.0006` n `6`; index avg `0.019` n `23`; metal avg `-0.0677` n `18`; unknown avg `0.0182` n `387`
- 1h: commodity avg `0.1728` n `12`; crypto_alt avg `0.1099` n `228`; crypto_major avg `-0.0436` n `8`; equity avg `-0.0581` n `67`; fx avg `0.0427` n `6`; index avg `0.0011` n `23`; metal avg `-0.3481` n `18`; unknown avg `0.0014` n `387`
- 4h: commodity avg `-0.4102` n `12`; crypto_alt avg `0.8141` n `228`; crypto_major avg `0.2889` n `8`; equity avg `0.2158` n `67`; fx avg `-0.0077` n `6`; index avg `0.1203` n `23`; metal avg `-0.3639` n `18`; unknown avg `0.1619` n `386`
- 24h: commodity avg `0.1866` n `12`; crypto_alt avg `0.2722` n `228`; crypto_major avg `0.3833` n `8`; equity avg `0.4098` n `67`; fx avg `-0.0364` n `6`; index avg `-0.1435` n `23`; metal avg `0.1368` n `18`; unknown avg `-0.3036` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
