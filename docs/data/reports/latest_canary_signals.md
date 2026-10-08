# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T06:07:29.749539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `0.1903` n `235`; crypto_major avg `0.1539` n `8`; equity avg `-0.0182` n `150`; fx avg `-0.0165` n `6`; index avg `-0.0196` n `26`; metal avg `-0.0117` n `20`; unknown avg `0.0022` n `1043`
- 1h: commodity avg `0.0533` n `13`; crypto_alt avg `0.1621` n `235`; crypto_major avg `0.1801` n `8`; equity avg `-0.2905` n `150`; fx avg `-0.0273` n `6`; index avg `-0.0663` n `26`; metal avg `-0.1535` n `20`; unknown avg `0.2727` n `1043`
- 4h: commodity avg `0.1432` n `13`; crypto_alt avg `-0.6295` n `235`; crypto_major avg `-0.6876` n `8`; equity avg `-0.738` n `150`; fx avg `-0.0015` n `6`; index avg `-0.1113` n `26`; metal avg `-0.205` n `20`; unknown avg `0.3702` n `1037`
- 24h: commodity avg `0.424` n `13`; crypto_alt avg `-1.0431` n `235`; crypto_major avg `-2.2653` n `8`; equity avg `-1.5191` n `150`; fx avg `-0.1365` n `6`; index avg `-0.2477` n `26`; metal avg `-0.2566` n `20`; unknown avg `42.8267` n `970`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
