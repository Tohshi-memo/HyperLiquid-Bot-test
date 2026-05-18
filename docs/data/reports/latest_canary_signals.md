# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T22:37:18.636792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4321` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `-0.0897` n `228`; crypto_major avg `-0.0999` n `8`; equity avg `0.0325` n `66`; fx avg `-0.0078` n `6`; index avg `-0.0117` n `23`; metal avg `0.0503` n `18`; unknown avg `-0.1496` n `383`
- 1h: commodity avg `0.0429` n `12`; crypto_alt avg `0.3418` n `228`; crypto_major avg `0.0485` n `8`; equity avg `0.2026` n `66`; fx avg `0.0067` n `6`; index avg `0.0522` n `23`; metal avg `0.2076` n `18`; unknown avg `-0.2308` n `383`
- 4h: commodity avg `-0.6125` n `12`; crypto_alt avg `2.3121` n `228`; crypto_major avg `1.8196` n `8`; equity avg `1.3373` n `66`; fx avg `0.021` n `6`; index avg `0.6766` n `23`; metal avg `0.9149` n `18`; unknown avg `0.8511` n `383`
- 24h: commodity avg `0.8365` n `12`; crypto_alt avg `-0.5122` n `228`; crypto_major avg `-1.1481` n `8`; equity avg `-0.901` n `66`; fx avg `0.1728` n `6`; index avg `-0.2046` n `23`; metal avg `0.7195` n `18`; unknown avg `-0.0377` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
