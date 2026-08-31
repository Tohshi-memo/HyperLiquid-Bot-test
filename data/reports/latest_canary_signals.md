# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T18:52:32.405098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `-0.0302` n `232`; crypto_major avg `-0.0992` n `8`; equity avg `-0.0016` n `129`; fx avg `0.0079` n `6`; index avg `-0.0125` n `26`; metal avg `0.038` n `20`; unknown avg `-0.0664` n `793`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `0.0948` n `232`; crypto_major avg `0.1081` n `8`; equity avg `-0.12` n `129`; fx avg `0.0148` n `6`; index avg `-0.0446` n `26`; metal avg `-0.0456` n `20`; unknown avg `0.107` n `791`
- 4h: commodity avg `0.1009` n `12`; crypto_alt avg `0.5969` n `232`; crypto_major avg `0.8809` n `8`; equity avg `0.1288` n `129`; fx avg `0.0008` n `6`; index avg `-0.0686` n `26`; metal avg `-0.0405` n `20`; unknown avg `-0.4834` n `791`
- 24h: commodity avg `0.5682` n `12`; crypto_alt avg `-1.1442` n `231`; crypto_major avg `-1.2699` n `8`; equity avg `-0.5751` n `129`; fx avg `-0.0913` n `6`; index avg `-0.2563` n `26`; metal avg `-0.5704` n `20`; unknown avg `0.168` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
