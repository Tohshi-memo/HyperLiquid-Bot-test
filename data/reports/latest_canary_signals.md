# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T10:07:33.944998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `-0.2024` n `230`; crypto_major avg `-0.1529` n `8`; equity avg `-0.0268` n `102`; fx avg `0.0207` n `6`; index avg `-0.0296` n `25`; metal avg `0.0141` n `20`; unknown avg `0.0289` n `780`
- 1h: commodity avg `0.227` n `12`; crypto_alt avg `-0.372` n `230`; crypto_major avg `-0.4528` n `8`; equity avg `-0.4` n `102`; fx avg `0.1471` n `6`; index avg `-0.074` n `25`; metal avg `-0.0306` n `20`; unknown avg `-0.0246` n `780`
- 4h: commodity avg `0.4144` n `12`; crypto_alt avg `-0.5864` n `230`; crypto_major avg `-0.9712` n `8`; equity avg `-0.4514` n `102`; fx avg `-0.0071` n `6`; index avg `-0.1281` n `25`; metal avg `-0.1786` n `20`; unknown avg `0.1081` n `779`
- 24h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.749` n `230`; crypto_major avg `-0.6299` n `8`; equity avg `8.0608` n `102`; fx avg `-0.1572` n `6`; index avg `1.1452` n `25`; metal avg `0.1035` n `20`; unknown avg `-0.0463` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
