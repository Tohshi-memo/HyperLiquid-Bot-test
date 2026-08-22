# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T06:37:24.695524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `0.0824` n `230`; crypto_major avg `0.4787` n `8`; equity avg `0.0086` n `121`; fx avg `-0.0007` n `6`; index avg `0.0037` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.0022` n `794`
- 1h: commodity avg `-0.0194` n `12`; crypto_alt avg `0.0906` n `230`; crypto_major avg `0.879` n `8`; equity avg `0.0383` n `121`; fx avg `-0.0042` n `6`; index avg `-0.012` n `25`; metal avg `-0.0202` n `20`; unknown avg `-0.0025` n `778`
- 4h: commodity avg `0.0669` n `12`; crypto_alt avg `-2.4253` n `230`; crypto_major avg `-0.2516` n `8`; equity avg `-0.3976` n `121`; fx avg `0.0167` n `6`; index avg `-0.0448` n `25`; metal avg `-0.132` n `20`; unknown avg `0.009` n `777`
- 24h: commodity avg `0.1574` n `12`; crypto_alt avg `6.1755` n `230`; crypto_major avg `6.8667` n `8`; equity avg `-0.3665` n `121`; fx avg `0.0134` n `6`; index avg `-0.0808` n `25`; metal avg `-0.0489` n `20`; unknown avg `1.1551` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
