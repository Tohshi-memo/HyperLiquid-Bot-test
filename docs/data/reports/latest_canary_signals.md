# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T19:52:42.401308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8513` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7227` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `0.1206` n `230`; crypto_major avg `0.2252` n `8`; equity avg `0.027` n `121`; fx avg `-0.0003` n `6`; index avg `0.0026` n `25`; metal avg `0.0039` n `20`; unknown avg `0.022` n `794`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.5685` n `230`; crypto_major avg `0.7232` n `8`; equity avg `0.0658` n `121`; fx avg `0.0073` n `6`; index avg `0.002` n `25`; metal avg `0.0108` n `20`; unknown avg `0.1937` n `794`
- 4h: commodity avg `0.0161` n `12`; crypto_alt avg `1.1598` n `230`; crypto_major avg `1.863` n `8`; equity avg `0.1403` n `121`; fx avg `0.0209` n `6`; index avg `-0.0067` n `25`; metal avg `0.0117` n `20`; unknown avg `1.4453` n `794`
- 24h: commodity avg `0.0074` n `12`; crypto_alt avg `1.8618` n `230`; crypto_major avg `4.4253` n `8`; equity avg `-0.3656` n `121`; fx avg `0.0619` n `6`; index avg `-0.0567` n `25`; metal avg `-0.1405` n `20`; unknown avg `2.0573` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
