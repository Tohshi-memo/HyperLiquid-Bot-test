# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T05:07:24.729777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `0.1738` n `230`; crypto_major avg `0.1203` n `8`; equity avg `0.0573` n `102`; fx avg `-0.0186` n `6`; index avg `0.007` n `25`; metal avg `-0.0218` n `20`; unknown avg `0.0274` n `774`
- 1h: commodity avg `-0.0543` n `12`; crypto_alt avg `0.1294` n `230`; crypto_major avg `0.0908` n `8`; equity avg `-0.0875` n `102`; fx avg `-0.0183` n `6`; index avg `-0.0312` n `25`; metal avg `-0.042` n `20`; unknown avg `1.9988` n `774`
- 4h: commodity avg `-0.0784` n `12`; crypto_alt avg `0.8497` n `230`; crypto_major avg `0.5963` n `8`; equity avg `-0.4426` n `102`; fx avg `-0.0733` n `6`; index avg `-0.0867` n `25`; metal avg `-0.0986` n `20`; unknown avg `-0.02` n `774`
- 24h: commodity avg `-0.804` n `12`; crypto_alt avg `-3.666` n `230`; crypto_major avg `-3.3269` n `8`; equity avg `-3.4725` n `102`; fx avg `-0.1363` n `6`; index avg `-0.7637` n `25`; metal avg `-0.3457` n `20`; unknown avg `1161.8703` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
