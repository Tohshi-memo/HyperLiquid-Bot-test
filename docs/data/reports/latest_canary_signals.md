# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T18:52:51.267166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.0597` n `228`; crypto_major avg `0.093` n `8`; equity avg `-0.0024` n `88`; fx avg `0.0062` n `6`; index avg `-0.0055` n `23`; metal avg `-0.0015` n `20`; unknown avg `0.0667` n `764`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-0.1785` n `228`; crypto_major avg `-0.1436` n `8`; equity avg `-0.0004` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0003` n `23`; metal avg `0.021` n `20`; unknown avg `0.6998` n `764`
- 4h: commodity avg `-0.057` n `12`; crypto_alt avg `-0.9757` n `228`; crypto_major avg `-0.6652` n `8`; equity avg `-0.1059` n `88`; fx avg `-0.033` n `6`; index avg `-0.0302` n `23`; metal avg `0.0093` n `20`; unknown avg `-0.4186` n `764`
- 24h: commodity avg `0.319` n `12`; crypto_alt avg `-0.8775` n `228`; crypto_major avg `-1.3674` n `8`; equity avg `0.0681` n `88`; fx avg `-0.03` n `6`; index avg `-0.0351` n `23`; metal avg `-0.0204` n `20`; unknown avg `15.0406` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
