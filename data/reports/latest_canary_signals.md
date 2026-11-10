# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T08:52:39.044408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0949` n `13`; crypto_alt avg `-0.0119` n `239`; crypto_major avg `0.0055` n `8`; equity avg `0.0926` n `160`; fx avg `0.0155` n `6`; index avg `0.0099` n `27`; metal avg `-0.0037` n `20`; unknown avg `0.0117` n `1253`
- 1h: commodity avg `-0.277` n `13`; crypto_alt avg `-0.0809` n `239`; crypto_major avg `-0.4696` n `8`; equity avg `0.2326` n `160`; fx avg `0.021` n `6`; index avg `0.0303` n `27`; metal avg `0.0655` n `20`; unknown avg `0.0308` n `1231`
- 4h: commodity avg `-0.3494` n `13`; crypto_alt avg `0.2175` n `239`; crypto_major avg `-0.1061` n `8`; equity avg `0.4094` n `160`; fx avg `-0.0547` n `6`; index avg `0.0863` n `27`; metal avg `-0.0736` n `20`; unknown avg `1.612` n `1211`
- 24h: commodity avg `-0.7936` n `13`; crypto_alt avg `1.4404` n `239`; crypto_major avg `0.0035` n `8`; equity avg `4.8467` n `160`; fx avg `-0.0507` n `6`; index avg `0.5525` n `27`; metal avg `0.2236` n `20`; unknown avg `171.7355` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
