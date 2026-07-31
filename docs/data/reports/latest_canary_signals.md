# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T06:22:27.587062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `0.0203` n `230`; crypto_major avg `0.0801` n `8`; equity avg `-0.0713` n `102`; fx avg `-0.0164` n `6`; index avg `0.0255` n `25`; metal avg `0.0393` n `20`; unknown avg `0.0595` n `779`
- 1h: commodity avg `0.0939` n `12`; crypto_alt avg `0.0603` n `230`; crypto_major avg `0.0732` n `8`; equity avg `0.0275` n `102`; fx avg `-0.0364` n `6`; index avg `0.0297` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.0102` n `747`
- 4h: commodity avg `0.0045` n `12`; crypto_alt avg `0.0392` n `230`; crypto_major avg `0.1965` n `8`; equity avg `1.0649` n `102`; fx avg `-0.0166` n `6`; index avg `0.2388` n `25`; metal avg `0.0687` n `20`; unknown avg `0.0097` n `747`
- 24h: commodity avg `-0.5797` n `12`; crypto_alt avg `0.1872` n `230`; crypto_major avg `1.1858` n `8`; equity avg `9.1309` n `102`; fx avg `-0.1391` n `6`; index avg `1.4124` n `25`; metal avg `0.7554` n `20`; unknown avg `0.0806` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
