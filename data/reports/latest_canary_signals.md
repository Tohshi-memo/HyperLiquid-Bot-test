# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T23:14:21.802210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4221` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2142` n `12`; crypto_alt avg `0.0626` n `228`; crypto_major avg `0.1064` n `8`; equity avg `0.0181` n `67`; fx avg `0.0005` n `6`; index avg `0.1207` n `23`; metal avg `0.0521` n `18`; unknown avg `-0.2676` n `396`
- 1h: commodity avg `0.129` n `12`; crypto_alt avg `-0.5399` n `228`; crypto_major avg `-0.2354` n `8`; equity avg `0.0041` n `67`; fx avg `0.0251` n `6`; index avg `-0.093` n `23`; metal avg `0.1291` n `18`; unknown avg `-0.134` n `396`
- 4h: commodity avg `-1.5432` n `12`; crypto_alt avg `0.8617` n `228`; crypto_major avg `0.8789` n `8`; equity avg `0.8105` n `67`; fx avg `0.0729` n `6`; index avg `0.286` n `23`; metal avg `0.5441` n `18`; unknown avg `0.3932` n `396`
- 24h: commodity avg `-2.5992` n `12`; crypto_alt avg `1.4725` n `228`; crypto_major avg `1.215` n `8`; equity avg `1.511` n `67`; fx avg `0.0509` n `6`; index avg `0.6962` n `23`; metal avg `0.7134` n `18`; unknown avg `-0.1127` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
