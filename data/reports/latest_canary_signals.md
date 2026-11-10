# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T11:37:27.001776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0864` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0188` n `13`; crypto_alt avg `0.0647` n `239`; crypto_major avg `0.173` n `8`; equity avg `0.0161` n `160`; fx avg `-0.0038` n `6`; index avg `-0.0006` n `27`; metal avg `0.0071` n `20`; unknown avg `3.9821` n `1262`
- 1h: commodity avg `0.3153` n `13`; crypto_alt avg `-0.0863` n `239`; crypto_major avg `0.0198` n `8`; equity avg `-0.2042` n `160`; fx avg `-0.0089` n `6`; index avg `0.0044` n `27`; metal avg `-0.0375` n `20`; unknown avg `22.8034` n `1256`
- 4h: commodity avg `0.1094` n `13`; crypto_alt avg `-0.6399` n `239`; crypto_major avg `-1.1154` n `8`; equity avg `-0.2531` n `160`; fx avg `-0.0021` n `6`; index avg `-0.029` n `27`; metal avg `-0.1816` n `20`; unknown avg `21.107` n `1219`
- 24h: commodity avg `-0.0955` n `13`; crypto_alt avg `0.2467` n `239`; crypto_major avg `-0.3728` n `8`; equity avg `3.68` n `160`; fx avg `-0.0099` n `6`; index avg `0.4048` n `27`; metal avg `-0.1193` n `20`; unknown avg `6.7209` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2344`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
