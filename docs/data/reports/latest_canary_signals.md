# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T17:37:25.323226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.1634` n `231`; crypto_major avg `0.467` n `8`; equity avg `0.1289` n `122`; fx avg `0.0036` n `6`; index avg `0.0067` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.1581` n `797`
- 1h: commodity avg `-0.0843` n `12`; crypto_alt avg `0.8974` n `231`; crypto_major avg `1.0152` n `8`; equity avg `0.4135` n `122`; fx avg `-0.0012` n `6`; index avg `0.0396` n `25`; metal avg `0.0005` n `20`; unknown avg `0.4709` n `797`
- 4h: commodity avg `0.3538` n `12`; crypto_alt avg `-0.3906` n `231`; crypto_major avg `-0.0772` n `8`; equity avg `-0.1159` n `122`; fx avg `-0.0107` n `6`; index avg `-0.0238` n `25`; metal avg `-0.2098` n `20`; unknown avg `-0.0739` n `797`
- 24h: commodity avg `0.32` n `12`; crypto_alt avg `-1.6306` n `231`; crypto_major avg `-1.43` n `8`; equity avg `-0.0434` n `122`; fx avg `-0.0485` n `6`; index avg `0.0518` n `25`; metal avg `-0.3061` n `20`; unknown avg `0.5211` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
