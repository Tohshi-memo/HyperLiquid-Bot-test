# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T14:22:33.033342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.3187` n `230`; crypto_major avg `-0.3405` n `8`; equity avg `-0.6031` n `98`; fx avg `-0.0007` n `6`; index avg `-0.0863` n `25`; metal avg `-0.0666` n `20`; unknown avg `-0.002` n `770`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.5745` n `230`; crypto_major avg `-0.7742` n `8`; equity avg `-0.9919` n `98`; fx avg `-0.0129` n `6`; index avg `-0.089` n `25`; metal avg `-0.0981` n `20`; unknown avg `0.2116` n `770`
- 4h: commodity avg `0.0916` n `12`; crypto_alt avg `-0.2546` n `230`; crypto_major avg `-0.3785` n `8`; equity avg `-0.6258` n `98`; fx avg `-0.0474` n `6`; index avg `-0.0094` n `25`; metal avg `-0.1732` n `20`; unknown avg `-0.0688` n `770`
- 24h: commodity avg `-0.4951` n `12`; crypto_alt avg `0.1238` n `230`; crypto_major avg `-0.4494` n `8`; equity avg `-0.1158` n `97`; fx avg `-0.0757` n `6`; index avg `0.1005` n `25`; metal avg `0.057` n `20`; unknown avg `-0.0808` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0785`, n `666`, weak_sample_signal
