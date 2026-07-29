# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T17:55:14.773887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0539` n `12`; crypto_alt avg `0.3611` n `230`; crypto_major avg `0.4209` n `8`; equity avg `0.2297` n `102`; fx avg `-0.007` n `6`; index avg `-0.0124` n `25`; metal avg `0.0671` n `18`; unknown avg `-0.0021` n `763`
- 1h: commodity avg `-0.0053` n `12`; crypto_alt avg `0.5275` n `230`; crypto_major avg `0.5543` n `8`; equity avg `0.739` n `102`; fx avg `0.0198` n `6`; index avg `0.1091` n `25`; metal avg `0.2167` n `18`; unknown avg `-0.0024` n `763`
- 4h: commodity avg `0.0831` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.028` n `8`; equity avg `-0.4576` n `102`; fx avg `-0.0186` n `6`; index avg `-0.0786` n `25`; metal avg `0.294` n `18`; unknown avg `-0.1479` n `762`
- 24h: commodity avg `1.2166` n `12`; crypto_alt avg `-1.4622` n `230`; crypto_major avg `0.526` n `8`; equity avg `-1.2226` n `102`; fx avg `-0.0438` n `6`; index avg `-0.3226` n `25`; metal avg `0.0446` n `18`; unknown avg `-0.2102` n `743`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
