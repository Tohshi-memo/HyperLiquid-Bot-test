# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T13:37:29.754554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0721` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5317` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0743` n `12`; crypto_alt avg `0.3903` n `229`; crypto_major avg `0.5573` n `8`; equity avg `-0.0709` n `88`; fx avg `-0.0054` n `6`; index avg `0.0067` n `25`; metal avg `0.2323` n `20`; unknown avg `-0.0104` n `763`
- 1h: commodity avg `0.1361` n `12`; crypto_alt avg `0.6032` n `229`; crypto_major avg `0.953` n `8`; equity avg `-0.3252` n `88`; fx avg `0.045` n `6`; index avg `-0.0918` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.3295` n `763`
- 4h: commodity avg `0.1265` n `12`; crypto_alt avg `1.2867` n `229`; crypto_major avg `2.1986` n `8`; equity avg `1.0172` n `88`; fx avg `0.02` n `6`; index avg `0.1907` n `25`; metal avg `0.6669` n `20`; unknown avg `-0.2521` n `763`
- 24h: commodity avg `-0.3776` n `12`; crypto_alt avg `3.8406` n `228`; crypto_major avg `5.0264` n `8`; equity avg `0.0667` n `88`; fx avg `-0.0417` n `6`; index avg `-0.1799` n `25`; metal avg `1.0396` n `20`; unknown avg `1.8615` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
