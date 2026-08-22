# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T09:22:26.879666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7528` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.602` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.834` n `230`; crypto_major avg `0.7959` n `8`; equity avg `0.0395` n `121`; fx avg `0.0043` n `6`; index avg `-0.0023` n `25`; metal avg `0.0068` n `20`; unknown avg `0.2066` n `794`
- 1h: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.5809` n `230`; crypto_major avg `-0.3749` n `8`; equity avg `-0.0062` n `121`; fx avg `0.0141` n `6`; index avg `-0.0063` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.1343` n `794`
- 4h: commodity avg `0.0191` n `12`; crypto_alt avg `1.2028` n `230`; crypto_major avg `1.8282` n `8`; equity avg `0.2262` n `121`; fx avg `0.0031` n `6`; index avg `-0.0135` n `25`; metal avg `0.0754` n `20`; unknown avg `0.3862` n `778`
- 24h: commodity avg `0.1388` n `12`; crypto_alt avg `4.6286` n `230`; crypto_major avg `4.755` n `8`; equity avg `-0.7142` n `121`; fx avg `0.0449` n `6`; index avg `-0.0899` n `25`; metal avg `-0.2137` n `20`; unknown avg `1.5699` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
