# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T17:52:34.580980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `0.171` n `230`; crypto_major avg `0.1928` n `8`; equity avg `0.2394` n `102`; fx avg `0.0` n `6`; index avg `-0.0067` n `25`; metal avg `0.0687` n `20`; unknown avg `-0.0381` n `778`
- 1h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.337` n `230`; crypto_major avg `0.3259` n `8`; equity avg `0.7492` n `102`; fx avg `0.0268` n `6`; index avg `0.1149` n `25`; metal avg `0.2033` n `20`; unknown avg `-0.0444` n `778`
- 4h: commodity avg `0.0692` n `12`; crypto_alt avg `-0.1887` n `230`; crypto_major avg `-0.199` n `8`; equity avg `-0.448` n `102`; fx avg `-0.0116` n `6`; index avg `-0.0728` n `25`; metal avg `0.2729` n `20`; unknown avg `-0.1447` n `777`
- 24h: commodity avg `1.2026` n `12`; crypto_alt avg `-1.6467` n `230`; crypto_major avg `0.2978` n `8`; equity avg `-1.2144` n `102`; fx avg `-0.0368` n `6`; index avg `-0.3169` n `25`; metal avg `0.0484` n `20`; unknown avg `-0.2068` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
