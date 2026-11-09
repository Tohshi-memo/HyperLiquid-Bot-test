# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T14:22:30.985487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1357` n `13`; crypto_alt avg `0.0943` n `239`; crypto_major avg `0.2348` n `8`; equity avg `0.1606` n `158`; fx avg `0.0032` n `6`; index avg `0.0146` n `27`; metal avg `0.0653` n `20`; unknown avg `0.2468` n `1263`
- 1h: commodity avg `-0.1967` n `13`; crypto_alt avg `0.0728` n `239`; crypto_major avg `0.1802` n `8`; equity avg `0.4036` n `158`; fx avg `0.0029` n `6`; index avg `0.0517` n `27`; metal avg `0.0701` n `20`; unknown avg `3.2411` n `1257`
- 4h: commodity avg `-0.4434` n `13`; crypto_alt avg `1.3272` n `239`; crypto_major avg `0.7439` n `8`; equity avg `0.5719` n `158`; fx avg `-0.0241` n `6`; index avg `0.0767` n `27`; metal avg `0.1363` n `20`; unknown avg `35.7597` n `1249`
- 24h: commodity avg `-0.5946` n `13`; crypto_alt avg `0.3305` n `239`; crypto_major avg `-2.841` n `8`; equity avg `0.4485` n `158`; fx avg `-0.1121` n `6`; index avg `0.0766` n `27`; metal avg `0.4441` n `20`; unknown avg `4.2919` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
