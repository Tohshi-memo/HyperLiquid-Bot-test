# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T15:37:45.013265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7882` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6322` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.6184` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-1.5222` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3567` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1376` n `13`; crypto_alt avg `-1.4842` n `239`; crypto_major avg `-1.5822` n `8`; equity avg `-0.8173` n `160`; fx avg `-0.024` n `6`; index avg `-0.0762` n `27`; metal avg `-0.0697` n `20`; unknown avg `0.6482` n `1260`
- 1h: commodity avg `0.1156` n `13`; crypto_alt avg `-0.8791` n `239`; crypto_major avg `-1.3242` n `8`; equity avg `0.2942` n `160`; fx avg `-0.0515` n `6`; index avg `0.0325` n `27`; metal avg `0.0131` n `20`; unknown avg `0.0413` n `1256`
- 4h: commodity avg `-0.2486` n `13`; crypto_alt avg `-0.4146` n `239`; crypto_major avg `-1.806` n `8`; equity avg `-0.2838` n `160`; fx avg `-0.0641` n `6`; index avg `-0.0178` n `27`; metal avg `-0.1738` n `20`; unknown avg `0.9409` n `1248`
- 24h: commodity avg `-0.7402` n `13`; crypto_alt avg `-1.9219` n `239`; crypto_major avg `-3.575` n `8`; equity avg `-0.5006` n `160`; fx avg `-0.0831` n `6`; index avg `-0.0076` n `27`; metal avg `-0.4002` n `20`; unknown avg `0.7409` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2294`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
