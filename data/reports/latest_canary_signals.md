# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T12:37:27.216190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4743` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6945` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0647` n `12`; crypto_alt avg `0.1877` n `229`; crypto_major avg `0.2398` n `8`; equity avg `0.7455` n `88`; fx avg `0.0007` n `6`; index avg `0.1737` n `25`; metal avg `0.7516` n `20`; unknown avg `0.1023` n `763`
- 1h: commodity avg `0.1242` n `12`; crypto_alt avg `0.3051` n `229`; crypto_major avg `0.3461` n `8`; equity avg `1.2592` n `88`; fx avg `-0.0231` n `6`; index avg `0.2933` n `25`; metal avg `0.6874` n `20`; unknown avg `0.0749` n `763`
- 4h: commodity avg `-0.1265` n `12`; crypto_alt avg `1.3856` n `228`; crypto_major avg `2.3478` n `8`; equity avg `1.6265` n `88`; fx avg `-0.0381` n `6`; index avg `0.2862` n `25`; metal avg `0.6533` n `20`; unknown avg `0.159` n `763`
- 24h: commodity avg `-0.4056` n `12`; crypto_alt avg `3.6602` n `228`; crypto_major avg `4.8967` n `8`; equity avg `-0.0918` n `88`; fx avg `-0.1097` n `6`; index avg `-0.217` n `25`; metal avg `1.4247` n `20`; unknown avg `2.0379` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
