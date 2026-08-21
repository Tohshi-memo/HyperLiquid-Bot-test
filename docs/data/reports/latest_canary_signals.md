# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T04:07:27.765940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `12`; crypto_alt avg `-0.0908` n `230`; crypto_major avg `-0.104` n `8`; equity avg `-0.0249` n `121`; fx avg `-0.0102` n `6`; index avg `0.0202` n `25`; metal avg `0.0413` n `20`; unknown avg `-0.0979` n `793`
- 1h: commodity avg `-0.0636` n `12`; crypto_alt avg `0.3239` n `230`; crypto_major avg `0.6077` n `8`; equity avg `-0.0969` n `121`; fx avg `0.0141` n `6`; index avg `-0.0065` n `25`; metal avg `0.0031` n `20`; unknown avg `0.1665` n `793`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `0.7459` n `230`; crypto_major avg `1.117` n `8`; equity avg `0.6218` n `121`; fx avg `-0.0695` n `6`; index avg `0.1125` n `25`; metal avg `0.2459` n `20`; unknown avg `-0.1272` n `793`
- 24h: commodity avg `0.2784` n `12`; crypto_alt avg `5.7493` n `230`; crypto_major avg `7.0097` n `8`; equity avg `-0.7161` n `121`; fx avg `-0.0189` n `6`; index avg `-0.1189` n `25`; metal avg `0.4863` n `20`; unknown avg `2.6361` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
