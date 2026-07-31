# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T00:37:28.948054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `0.0332` n `8`; equity avg `0.3428` n `102`; fx avg `0.0187` n `6`; index avg `0.1131` n `25`; metal avg `-0.0498` n `20`; unknown avg `4.7073` n `779`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.2655` n `230`; crypto_major avg `-0.431` n `8`; equity avg `0.7511` n `102`; fx avg `0.1107` n `6`; index avg `0.3011` n `25`; metal avg `-0.0512` n `20`; unknown avg `0.6709` n `779`
- 4h: commodity avg `0.0491` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `0.0935` n `8`; equity avg `1.4742` n `102`; fx avg `0.1488` n `6`; index avg `0.3554` n `25`; metal avg `-0.041` n `20`; unknown avg `0.0542` n `779`
- 24h: commodity avg `0.0673` n `12`; crypto_alt avg `0.9409` n `230`; crypto_major avg `1.6095` n `8`; equity avg `8.131` n `102`; fx avg `-0.2001` n `6`; index avg `1.209` n `25`; metal avg `0.575` n `20`; unknown avg `0.1242` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
