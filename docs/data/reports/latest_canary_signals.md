# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T06:07:25.868707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `0.0871` n `239`; crypto_major avg `0.0438` n `8`; equity avg `-0.0307` n `168`; fx avg `0.0224` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0385` n `20`; unknown avg `0.1723` n `1233`
- 1h: commodity avg `0.0258` n `13`; crypto_alt avg `0.099` n `239`; crypto_major avg `0.0963` n `8`; equity avg `0.4035` n `168`; fx avg `0.0234` n `6`; index avg `-0.0051` n `27`; metal avg `0.1202` n `20`; unknown avg `-0.0035` n `1235`
- 4h: commodity avg `0.091` n `13`; crypto_alt avg `0.9069` n `239`; crypto_major avg `1.3869` n `8`; equity avg `2.262` n `168`; fx avg `0.001` n `6`; index avg `0.1517` n `27`; metal avg `0.3038` n `20`; unknown avg `63.9539` n `1231`
- 24h: commodity avg `0.3794` n `13`; crypto_alt avg `2.0484` n `239`; crypto_major avg `2.6406` n `8`; equity avg `3.9122` n `168`; fx avg `0.0463` n `6`; index avg `0.3202` n `27`; metal avg `1.0074` n `20`; unknown avg `215.022` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
