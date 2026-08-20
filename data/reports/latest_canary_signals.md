# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T18:52:43.443566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.7844` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7434` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.7388` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.5695` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `0.183` n `230`; crypto_major avg `0.141` n `8`; equity avg `0.168` n `121`; fx avg `-0.0052` n `6`; index avg `0.0135` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0274` n `792`
- 1h: commodity avg `0.1267` n `12`; crypto_alt avg `-0.9256` n `230`; crypto_major avg `-1.8017` n `8`; equity avg `-0.2322` n `121`; fx avg `0.0097` n `6`; index avg `-0.0629` n `25`; metal avg `-0.0173` n `20`; unknown avg `0.1891` n `792`
- 4h: commodity avg `0.2049` n `12`; crypto_alt avg `0.7903` n `230`; crypto_major avg `1.2101` n `8`; equity avg `-0.5333` n `121`; fx avg `0.0405` n `6`; index avg `-0.1202` n `25`; metal avg `0.1005` n `20`; unknown avg `1.8617` n `792`
- 24h: commodity avg `0.4157` n `12`; crypto_alt avg `5.794` n `230`; crypto_major avg `9.0846` n `8`; equity avg `-0.361` n `121`; fx avg `0.205` n `6`; index avg `-0.0706` n `25`; metal avg `0.2329` n `20`; unknown avg `3.6242` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
