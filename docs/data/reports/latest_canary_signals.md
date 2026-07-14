# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T03:22:28.964930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0499` n `12`; crypto_alt avg `-0.3653` n `230`; crypto_major avg `-0.4193` n `8`; equity avg `-0.3867` n `92`; fx avg `0.0035` n `6`; index avg `-0.1008` n `25`; metal avg `-0.0691` n `20`; unknown avg `-0.0914` n `766`
- 1h: commodity avg `0.1548` n `12`; crypto_alt avg `-0.4209` n `230`; crypto_major avg `-0.4232` n `8`; equity avg `-0.694` n `92`; fx avg `-0.0484` n `6`; index avg `-0.169` n `25`; metal avg `-0.0619` n `20`; unknown avg `-0.1988` n `766`
- 4h: commodity avg `0.0978` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `-0.1491` n `8`; equity avg `-0.7326` n `92`; fx avg `-0.0578` n `6`; index avg `-0.2516` n `25`; metal avg `0.0358` n `20`; unknown avg `-0.3569` n `766`
- 24h: commodity avg `1.0667` n `12`; crypto_alt avg `-0.7466` n `230`; crypto_major avg `-1.4025` n `8`; equity avg `-2.1889` n `92`; fx avg `-0.199` n `6`; index avg `-0.5105` n `25`; metal avg `-0.0846` n `20`; unknown avg `-0.3094` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
