# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T04:22:24.655380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.1836` n `230`; crypto_major avg `-0.1468` n `8`; equity avg `0.2082` n `102`; fx avg `0.0211` n `6`; index avg `0.0234` n `25`; metal avg `0.0202` n `20`; unknown avg `0.1621` n `779`
- 1h: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.2243` n `230`; crypto_major avg `-0.2155` n `8`; equity avg `0.1603` n `102`; fx avg `-0.0034` n `6`; index avg `-0.0157` n `25`; metal avg `0.0655` n `20`; unknown avg `0.2914` n `779`
- 4h: commodity avg `-0.3217` n `12`; crypto_alt avg `-0.4033` n `230`; crypto_major avg `-0.702` n `8`; equity avg `0.217` n `102`; fx avg `0.1237` n `6`; index avg `0.0558` n `25`; metal avg `-0.2324` n `20`; unknown avg `0.4265` n `779`
- 24h: commodity avg `-0.206` n `12`; crypto_alt avg `-0.035` n `230`; crypto_major avg `0.7717` n `8`; equity avg `8.6091` n `102`; fx avg `-0.0854` n `6`; index avg `1.1392` n `25`; metal avg `0.564` n `20`; unknown avg `0.072` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
