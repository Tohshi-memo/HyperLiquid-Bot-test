# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T10:52:25.359588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0283` n `230`; crypto_major avg `0.0425` n `8`; equity avg `0.0847` n `113`; fx avg `-0.0093` n `6`; index avg `0.0103` n `25`; metal avg `0.0427` n `20`; unknown avg `-0.0052` n `787`
- 1h: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.0874` n `230`; crypto_major avg `-0.2839` n `8`; equity avg `0.0412` n `113`; fx avg `-0.0012` n `6`; index avg `0.0067` n `25`; metal avg `0.1213` n `20`; unknown avg `0.0044` n `787`
- 4h: commodity avg `-0.3174` n `12`; crypto_alt avg `0.0007` n `230`; crypto_major avg `-0.3575` n `8`; equity avg `-0.2401` n `113`; fx avg `-0.0071` n `6`; index avg `-0.0109` n `25`; metal avg `0.0505` n `20`; unknown avg `0.0393` n `787`
- 24h: commodity avg `-0.415` n `12`; crypto_alt avg `-0.6463` n `230`; crypto_major avg `-0.5404` n `8`; equity avg `1.3198` n `113`; fx avg `0.0368` n `6`; index avg `0.1722` n `25`; metal avg `-0.4227` n `20`; unknown avg `0.1261` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2279`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
