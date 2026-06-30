# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T03:37:25.554664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.039` n `12`; crypto_alt avg `-0.1267` n `228`; crypto_major avg `-0.2316` n `8`; equity avg `0.0838` n `88`; fx avg `-0.0049` n `6`; index avg `0.0217` n `23`; metal avg `-0.0813` n `20`; unknown avg `0.0631` n `765`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `0.1248` n `228`; crypto_major avg `-0.0216` n `8`; equity avg `0.1796` n `88`; fx avg `-0.0182` n `6`; index avg `0.0538` n `23`; metal avg `0.1282` n `20`; unknown avg `2.379` n `765`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.5562` n `228`; crypto_major avg `-0.9049` n `8`; equity avg `0.0598` n `88`; fx avg `0.0204` n `6`; index avg `0.0224` n `23`; metal avg `-0.5146` n `20`; unknown avg `3.4226` n `763`
- 24h: commodity avg `-0.2302` n `12`; crypto_alt avg `-0.2321` n `228`; crypto_major avg `0.9094` n `8`; equity avg `2.3224` n `88`; fx avg `0.1247` n `6`; index avg `0.3892` n `23`; metal avg `-0.8162` n `20`; unknown avg `4.3723` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
