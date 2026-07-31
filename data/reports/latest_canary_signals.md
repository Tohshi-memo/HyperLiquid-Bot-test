# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T13:22:24.703407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0374` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `0.0913` n `8`; equity avg `0.3138` n `102`; fx avg `-0.0467` n `6`; index avg `0.04` n `25`; metal avg `-0.0366` n `20`; unknown avg `0.1488` n `780`
- 1h: commodity avg `-0.0575` n `12`; crypto_alt avg `0.4399` n `230`; crypto_major avg `0.3577` n `8`; equity avg `0.3703` n `102`; fx avg `-0.0309` n `6`; index avg `0.0352` n `25`; metal avg `-0.0921` n `20`; unknown avg `0.5512` n `780`
- 4h: commodity avg `0.3472` n `12`; crypto_alt avg `0.3911` n `230`; crypto_major avg `0.4492` n `8`; equity avg `-0.2179` n `102`; fx avg `0.0533` n `6`; index avg `-0.0783` n `25`; metal avg `-0.1186` n `20`; unknown avg `1.416` n `780`
- 24h: commodity avg `0.5553` n `12`; crypto_alt avg `-0.0803` n `230`; crypto_major avg `0.0987` n `8`; equity avg `5.5675` n `102`; fx avg `-0.0923` n `6`; index avg `0.7933` n `25`; metal avg `-0.0956` n `20`; unknown avg `1.4743` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
