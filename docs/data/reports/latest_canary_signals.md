# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T14:07:28.828714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0698` n `12`; crypto_alt avg `0.1089` n `230`; crypto_major avg `0.1712` n `8`; equity avg `0.3936` n `94`; fx avg `0.005` n `6`; index avg `0.0877` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.0193` n `768`
- 1h: commodity avg `-0.1014` n `12`; crypto_alt avg `0.5154` n `230`; crypto_major avg `0.5896` n `8`; equity avg `-0.4469` n `94`; fx avg `0.0064` n `6`; index avg `0.0507` n `25`; metal avg `0.0772` n `20`; unknown avg `0.1624` n `768`
- 4h: commodity avg `0.1258` n `12`; crypto_alt avg `0.5394` n `230`; crypto_major avg `0.1823` n `8`; equity avg `-0.9787` n `94`; fx avg `0.0345` n `6`; index avg `-0.0776` n `25`; metal avg `-0.315` n `20`; unknown avg `0.1115` n `768`
- 24h: commodity avg `0.1977` n `12`; crypto_alt avg `-1.0739` n `230`; crypto_major avg `-1.7163` n `8`; equity avg `-3.5866` n `93`; fx avg `0.0203` n `6`; index avg `-0.459` n `25`; metal avg `-0.5758` n `20`; unknown avg `-0.1357` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
