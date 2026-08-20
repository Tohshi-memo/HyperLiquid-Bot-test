# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T10:52:16.775606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5021` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9384` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0344` n `12`; crypto_alt avg `0.0813` n `230`; crypto_major avg `-0.0109` n `8`; equity avg `0.0736` n `121`; fx avg `0.0048` n `6`; index avg `0.0159` n `25`; metal avg `-0.0288` n `20`; unknown avg `-0.0045` n `792`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `0.5906` n `230`; crypto_major avg `0.366` n `8`; equity avg `0.1387` n `121`; fx avg `0.007` n `6`; index avg `0.047` n `25`; metal avg `0.0856` n `20`; unknown avg `0.0681` n `792`
- 4h: commodity avg `0.2839` n `12`; crypto_alt avg `1.8877` n `230`; crypto_major avg `1.9732` n `8`; equity avg `-0.5289` n `121`; fx avg `0.0928` n `6`; index avg `-0.0704` n `25`; metal avg `0.0348` n `20`; unknown avg `0.212` n `792`
- 24h: commodity avg `0.1574` n `12`; crypto_alt avg `7.7765` n `230`; crypto_major avg `12.5412` n `8`; equity avg `0.5807` n `120`; fx avg `0.2249` n `6`; index avg `0.1349` n `25`; metal avg `0.951` n `20`; unknown avg `2.5138` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
