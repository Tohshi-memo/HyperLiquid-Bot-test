# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T17:43:32.771861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0643` n `12`; crypto_alt avg `-0.0839` n `228`; crypto_major avg `-0.0837` n `8`; equity avg `-0.0431` n `88`; fx avg `0.0057` n `6`; index avg `-0.0006` n `23`; metal avg `-0.0041` n `20`; unknown avg `0.1034` n `764`
- 1h: commodity avg `-0.0534` n `12`; crypto_alt avg `-0.1442` n `228`; crypto_major avg `-0.0839` n `8`; equity avg `-0.0218` n `88`; fx avg `-0.017` n `6`; index avg `-0.0118` n `23`; metal avg `0.0022` n `20`; unknown avg `0.185` n `764`
- 4h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.5028` n `228`; crypto_major avg `-0.7244` n `8`; equity avg `-0.0819` n `88`; fx avg `-0.0159` n `6`; index avg `-0.0228` n `23`; metal avg `-0.0345` n `20`; unknown avg `0.4181` n `764`
- 24h: commodity avg `0.2987` n `12`; crypto_alt avg `-1.0331` n `228`; crypto_major avg `-1.7184` n `8`; equity avg `0.0539` n `88`; fx avg `-0.0194` n `6`; index avg `-0.0444` n `23`; metal avg `-0.0429` n `20`; unknown avg `14.6918` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
