# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T06:22:27.228779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `0.1794` n `230`; crypto_major avg `0.0317` n `8`; equity avg `0.3215` n `96`; fx avg `0.0233` n `6`; index avg `0.0411` n `25`; metal avg `0.1075` n `20`; unknown avg `-0.0193` n `768`
- 1h: commodity avg `-0.2144` n `12`; crypto_alt avg `-0.3766` n `230`; crypto_major avg `-0.4467` n `8`; equity avg `0.0845` n `96`; fx avg `0.018` n `6`; index avg `0.0255` n `25`; metal avg `0.1749` n `20`; unknown avg `-0.0495` n `736`
- 4h: commodity avg `-0.2639` n `12`; crypto_alt avg `-0.1504` n `230`; crypto_major avg `-0.8044` n `8`; equity avg `-0.6566` n `94`; fx avg `0.0306` n `6`; index avg `-0.1174` n `25`; metal avg `0.055` n `20`; unknown avg `-0.1044` n `736`
- 24h: commodity avg `-0.2716` n `12`; crypto_alt avg `-2.3066` n `230`; crypto_major avg `-3.9072` n `8`; equity avg `-5.6803` n `94`; fx avg `-0.1145` n `6`; index avg `-0.7703` n `25`; metal avg `-0.6987` n `20`; unknown avg `-0.584` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
