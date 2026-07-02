# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T18:52:34.223327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7573` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `0.0614` n `229`; crypto_major avg `0.1159` n `8`; equity avg `0.2076` n `88`; fx avg `-0.0041` n `6`; index avg `0.0482` n `25`; metal avg `-0.0179` n `20`; unknown avg `0.2232` n `765`
- 1h: commodity avg `-0.007` n `12`; crypto_alt avg `0.217` n `229`; crypto_major avg `0.4278` n `8`; equity avg `0.6509` n `88`; fx avg `0.021` n `6`; index avg `0.1585` n `25`; metal avg `0.1691` n `20`; unknown avg `0.0132` n `765`
- 4h: commodity avg `0.2677` n `12`; crypto_alt avg `0.3496` n `229`; crypto_major avg `0.5701` n `8`; equity avg `-1.1872` n `88`; fx avg `-0.0828` n `6`; index avg `-0.2265` n `25`; metal avg `-0.0535` n `20`; unknown avg `-0.0202` n `763`
- 24h: commodity avg `0.0122` n `12`; crypto_alt avg `2.3295` n `228`; crypto_major avg `3.0307` n `8`; equity avg `-2.6768` n `88`; fx avg `-0.1009` n `6`; index avg `-0.5717` n `25`; metal avg `0.7835` n `20`; unknown avg `1.5874` n `739`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
