# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T19:07:44.312557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0791` n `229`; crypto_major avg `0.0631` n `8`; equity avg `0.0625` n `92`; fx avg `0.0033` n `6`; index avg `0.0139` n `25`; metal avg `0.0199` n `20`; unknown avg `0.0746` n `765`
- 1h: commodity avg `0.1364` n `12`; crypto_alt avg `-0.1986` n `229`; crypto_major avg `-0.2101` n `8`; equity avg `-0.0775` n `92`; fx avg `-0.0055` n `6`; index avg `0.002` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0253` n `765`
- 4h: commodity avg `0.135` n `12`; crypto_alt avg `-0.1128` n `229`; crypto_major avg `-0.1787` n `8`; equity avg `0.443` n `92`; fx avg `-0.052` n `6`; index avg `0.139` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.1571` n `765`
- 24h: commodity avg `-0.1616` n `12`; crypto_alt avg `0.4056` n `229`; crypto_major avg `0.6535` n `8`; equity avg `-0.723` n `92`; fx avg `-0.1628` n `6`; index avg `0.0459` n `25`; metal avg `0.0576` n `20`; unknown avg `-0.167` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
