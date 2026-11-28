# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T13:22:35.315098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.81` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.0883` n `239`; crypto_major avg `-0.0889` n `8`; equity avg `-0.004` n `168`; fx avg `-0.0064` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0029` n `20`; unknown avg `0.0343` n `1265`
- 1h: commodity avg `0.0043` n `13`; crypto_alt avg `-0.4629` n `239`; crypto_major avg `-0.2814` n `8`; equity avg `-0.1101` n `168`; fx avg `-0.0271` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0123` n `20`; unknown avg `-0.1402` n `1257`
- 4h: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.7368` n `239`; crypto_major avg `-0.4695` n `8`; equity avg `-0.1288` n `168`; fx avg `-0.0269` n `6`; index avg `-0.007` n `27`; metal avg `0.0201` n `20`; unknown avg `622.0017` n `1247`
- 24h: commodity avg `-0.2907` n `13`; crypto_alt avg `-3.7062` n `239`; crypto_major avg `-3.291` n `8`; equity avg `-0.1632` n `168`; fx avg `-0.0857` n `6`; index avg `-0.0041` n `27`; metal avg `0.1689` n `20`; unknown avg `191.3736` n `1092`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
