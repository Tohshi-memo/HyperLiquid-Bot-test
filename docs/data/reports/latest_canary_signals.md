# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T06:37:24.023099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `-0.2554` n `231`; crypto_major avg `-0.1212` n `8`; equity avg `0.0392` n `122`; fx avg `0.0078` n `6`; index avg `0.0031` n `25`; metal avg `0.042` n `20`; unknown avg `-0.04` n `793`
- 1h: commodity avg `-0.0588` n `12`; crypto_alt avg `-0.1135` n `231`; crypto_major avg `0.1009` n `8`; equity avg `-0.0518` n `122`; fx avg `0.045` n `6`; index avg `-0.0208` n `25`; metal avg `0.1828` n `20`; unknown avg `-0.0422` n `777`
- 4h: commodity avg `-0.0666` n `12`; crypto_alt avg `-0.4357` n `231`; crypto_major avg `-0.6418` n `8`; equity avg `-0.8868` n `122`; fx avg `0.0124` n `6`; index avg `-0.1593` n `25`; metal avg `0.0369` n `20`; unknown avg `-0.17` n `777`
- 24h: commodity avg `-0.3626` n `12`; crypto_alt avg `3.6943` n `231`; crypto_major avg `1.4388` n `8`; equity avg `-1.1827` n `122`; fx avg `-0.2141` n `6`; index avg `-0.1198` n `25`; metal avg `0.2687` n `20`; unknown avg `5.5106` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
