# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T05:07:27.148703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `-0.0205` n `231`; crypto_major avg `0.0419` n `8`; equity avg `0.0038` n `126`; fx avg `0.0048` n `6`; index avg `0.0022` n `25`; metal avg `-0.0129` n `20`; unknown avg `0.7891` n `793`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.3062` n `231`; crypto_major avg `-0.2034` n `8`; equity avg `-0.156` n `126`; fx avg `0.0202` n `6`; index avg `-0.0342` n `25`; metal avg `-0.0388` n `20`; unknown avg `-0.1938` n `793`
- 4h: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.4585` n `231`; crypto_major avg `-0.1712` n `8`; equity avg `0.1665` n `126`; fx avg `0.0364` n `6`; index avg `0.0212` n `25`; metal avg `-0.0386` n `20`; unknown avg `-0.1387` n `793`
- 24h: commodity avg `0.4309` n `12`; crypto_alt avg `0.3308` n `231`; crypto_major avg `0.5991` n `8`; equity avg `1.0816` n `126`; fx avg `-0.0872` n `6`; index avg `0.1315` n `25`; metal avg `-0.2665` n `20`; unknown avg `0.2595` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
