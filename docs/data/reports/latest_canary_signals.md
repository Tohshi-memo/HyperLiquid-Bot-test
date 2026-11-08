# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T12:37:24.731299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.1581` n `239`; crypto_major avg `-0.0608` n `8`; equity avg `-0.0068` n `158`; fx avg `0.0043` n `6`; index avg `0.0046` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.0604` n `1262`
- 1h: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.289` n `239`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0376` n `158`; fx avg `-0.0027` n `6`; index avg `-0.0146` n `27`; metal avg `0.0036` n `20`; unknown avg `0.0148` n `1250`
- 4h: commodity avg `-0.1538` n `13`; crypto_alt avg `-0.3092` n `239`; crypto_major avg `0.0922` n `8`; equity avg `0.1405` n `158`; fx avg `0.0053` n `6`; index avg `-0.0324` n `27`; metal avg `0.0041` n `20`; unknown avg `218.8981` n `1170`
- 24h: commodity avg `0.0947` n `13`; crypto_alt avg `-1.3482` n `239`; crypto_major avg `-0.1806` n `8`; equity avg `0.2093` n `158`; fx avg `0.0098` n `6`; index avg `0.0264` n `27`; metal avg `-0.0318` n `20`; unknown avg `5.4883` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
