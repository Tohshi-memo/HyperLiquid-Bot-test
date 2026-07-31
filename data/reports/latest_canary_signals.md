# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T08:37:26.601081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `-0.019` n `230`; crypto_major avg `0.0019` n `8`; equity avg `0.0865` n `102`; fx avg `0.0313` n `6`; index avg `-0.01` n `25`; metal avg `-0.0342` n `20`; unknown avg `0.0214` n `780`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.155` n `230`; crypto_major avg `0.1108` n `8`; equity avg `0.3842` n `102`; fx avg `-0.0511` n `6`; index avg `-0.0318` n `25`; metal avg `-0.0195` n `20`; unknown avg `0.0497` n `779`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `0.1725` n `230`; crypto_major avg `-0.1979` n `8`; equity avg `0.2089` n `102`; fx avg `-0.1444` n `6`; index avg `0.0214` n `25`; metal avg `-0.125` n `20`; unknown avg `0.0346` n `747`
- 24h: commodity avg `-0.2695` n `12`; crypto_alt avg `-0.044` n `230`; crypto_major avg `0.2325` n `8`; equity avg `8.5041` n `102`; fx avg `-0.21` n `6`; index avg `1.2104` n `25`; metal avg `0.2606` n `20`; unknown avg `0.0143` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
