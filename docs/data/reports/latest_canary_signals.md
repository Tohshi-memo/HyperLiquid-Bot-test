# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T09:22:29.950999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0651` n `12`; crypto_alt avg `-0.1104` n `229`; crypto_major avg `0.0646` n `8`; equity avg `0.1746` n `91`; fx avg `0.0138` n `6`; index avg `0.0387` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0002` n `766`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `-0.1021` n `229`; crypto_major avg `0.0011` n `8`; equity avg `0.1441` n `91`; fx avg `-0.0033` n `6`; index avg `0.0408` n `25`; metal avg `-0.0804` n `20`; unknown avg `-0.0659` n `765`
- 4h: commodity avg `-0.2267` n `12`; crypto_alt avg `0.0773` n `229`; crypto_major avg `0.3815` n `8`; equity avg `-0.594` n `91`; fx avg `-0.082` n `6`; index avg `-0.0632` n `25`; metal avg `-0.1799` n `20`; unknown avg `1.167` n `733`
- 24h: commodity avg `-0.9361` n `12`; crypto_alt avg `0.951` n `229`; crypto_major avg `1.5287` n `8`; equity avg `0.2312` n `91`; fx avg `-0.1299` n `6`; index avg `0.2317` n `25`; metal avg `0.0667` n `20`; unknown avg `0.1332` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
