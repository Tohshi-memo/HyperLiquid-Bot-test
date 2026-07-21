# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T13:52:25.920678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0556` n `12`; crypto_alt avg `0.1076` n `230`; crypto_major avg `0.0683` n `8`; equity avg `0.2401` n `98`; fx avg `0.0152` n `6`; index avg `-0.0181` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.0318` n `771`
- 1h: commodity avg `0.1092` n `12`; crypto_alt avg `-0.0706` n `230`; crypto_major avg `-0.065` n `8`; equity avg `0.5241` n `98`; fx avg `-0.0043` n `6`; index avg `0.0146` n `25`; metal avg `-0.1372` n `20`; unknown avg `-0.0629` n `771`
- 4h: commodity avg `0.1813` n `12`; crypto_alt avg `-0.1111` n `230`; crypto_major avg `-0.1607` n `8`; equity avg `0.3915` n `98`; fx avg `-0.0244` n `6`; index avg `0.0079` n `25`; metal avg `-0.2033` n `20`; unknown avg `0.0097` n `771`
- 24h: commodity avg `0.6261` n `12`; crypto_alt avg `2.042` n `230`; crypto_major avg `2.3398` n `8`; equity avg `2.0661` n `98`; fx avg `-0.0496` n `6`; index avg `0.1592` n `25`; metal avg `0.4241` n `20`; unknown avg `0.1423` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0594`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
