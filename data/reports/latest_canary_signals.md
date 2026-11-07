# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T09:37:26.450776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `-0.1181` n `239`; crypto_major avg `-0.1305` n `8`; equity avg `-0.0364` n `158`; fx avg `-0.0005` n `6`; index avg `-0.0029` n `27`; metal avg `-0.0055` n `20`; unknown avg `-0.0779` n `1261`
- 1h: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.2384` n `239`; crypto_major avg `-0.2607` n `8`; equity avg `0.0489` n `158`; fx avg `0.0117` n `6`; index avg `0.0024` n `27`; metal avg `-0.015` n `20`; unknown avg `131.8561` n `1225`
- 4h: commodity avg `0.0346` n `13`; crypto_alt avg `-0.3299` n `239`; crypto_major avg `-0.0231` n `8`; equity avg `0.0901` n `158`; fx avg `-0.0236` n `6`; index avg `0.0215` n `27`; metal avg `-0.0212` n `20`; unknown avg `137.043` n `1177`
- 24h: commodity avg `0.1604` n `13`; crypto_alt avg `-0.5715` n `239`; crypto_major avg `-0.3763` n `8`; equity avg `-0.4743` n `158`; fx avg `0.0346` n `6`; index avg `-0.0387` n `27`; metal avg `-0.041` n `20`; unknown avg `7.9326` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
