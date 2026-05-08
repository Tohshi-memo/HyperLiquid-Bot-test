# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T09:22:20.061558+00:00`
- Correlation status: `ready`
- Asset price records: `633`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0563` n `12`; crypto_alt avg `0.3712` n `228`; crypto_major avg `0.2229` n `8`; equity avg `0.0589` n `65`; fx avg `-0.0053` n `5`; index avg `0.0149` n `23`; metal avg `0.0804` n `18`; unknown avg `0.335` n `375`
- 1h: commodity avg `-0.2159` n `12`; crypto_alt avg `0.588` n `228`; crypto_major avg `0.3699` n `8`; equity avg `0.2604` n `65`; fx avg `0.0192` n `5`; index avg `0.1019` n `23`; metal avg `0.06` n `18`; unknown avg `0.4801` n `375`
- 4h: commodity avg `-0.358` n `12`; crypto_alt avg `0.6408` n `228`; crypto_major avg `0.5377` n `8`; equity avg `0.9058` n `65`; fx avg `0.0838` n `5`; index avg `0.2903` n `23`; metal avg `0.3677` n `18`; unknown avg `0.8216` n `355`
- 24h: commodity avg `1.039` n `12`; crypto_alt avg `1.1346` n `228`; crypto_major avg `-1.3735` n `8`; equity avg `-0.4982` n `65`; fx avg `0.2343` n `5`; index avg `-0.4642` n `23`; metal avg `-0.2406` n `18`; unknown avg `0.3897` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1355`, n `625`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1347`, n `625`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `629`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `629`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `629`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `629`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0869`, n `625`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0843`, n `625`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `629`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `629`, weak_sample_signal
