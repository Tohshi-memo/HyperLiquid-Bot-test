# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T18:22:28.655688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1193` n `228`; crypto_major avg `-0.1562` n `8`; equity avg `-0.0137` n `88`; fx avg `0.0` n `6`; index avg `0.0127` n `23`; metal avg `0.0055` n `20`; unknown avg `-0.0306` n `764`
- 1h: commodity avg `-0.0994` n `12`; crypto_alt avg `0.0044` n `228`; crypto_major avg `-0.0283` n `8`; equity avg `-0.008` n `88`; fx avg `0.0025` n `6`; index avg `0.0154` n `23`; metal avg `0.0128` n `20`; unknown avg `0.0067` n `764`
- 4h: commodity avg `-0.018` n `12`; crypto_alt avg `-0.8374` n `228`; crypto_major avg `-0.8265` n `8`; equity avg `-0.0779` n `88`; fx avg `-0.0092` n `6`; index avg `-0.0028` n `23`; metal avg `-0.0269` n `20`; unknown avg `0.1432` n `764`
- 24h: commodity avg `0.3104` n `12`; crypto_alt avg `-0.6971` n `228`; crypto_major avg `-1.3175` n `8`; equity avg `0.0892` n `88`; fx avg `-0.0249` n `6`; index avg `-0.0367` n `23`; metal avg `-0.0349` n `20`; unknown avg `14.6899` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
