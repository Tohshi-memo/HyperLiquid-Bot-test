# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T01:22:25.646165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `13`; crypto_alt avg `-0.0415` n `239`; crypto_major avg `-0.0003` n `8`; equity avg `0.4552` n `168`; fx avg `-0.0079` n `6`; index avg `0.0631` n `27`; metal avg `0.0193` n `20`; unknown avg `0.2634` n `1261`
- 1h: commodity avg `0.0369` n `13`; crypto_alt avg `0.1402` n `239`; crypto_major avg `0.2969` n `8`; equity avg `0.8185` n `168`; fx avg `-0.0398` n `6`; index avg `0.1075` n `27`; metal avg `0.1138` n `20`; unknown avg `11.8519` n `1257`
- 4h: commodity avg `0.1059` n `13`; crypto_alt avg `-0.1173` n `239`; crypto_major avg `-0.249` n `8`; equity avg `0.4348` n `168`; fx avg `-0.0317` n `6`; index avg `0.0787` n `27`; metal avg `0.0678` n `20`; unknown avg `1.8403` n `1205`
- 24h: commodity avg `0.0987` n `13`; crypto_alt avg `0.5786` n `239`; crypto_major avg `0.2902` n `8`; equity avg `0.1918` n `168`; fx avg `-0.0182` n `6`; index avg `0.0171` n `27`; metal avg `0.0015` n `20`; unknown avg `181.2908` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
