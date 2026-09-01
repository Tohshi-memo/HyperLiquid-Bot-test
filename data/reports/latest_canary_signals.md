# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T06:52:30.784312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `-0.1266` n `232`; crypto_major avg `-0.0901` n `8`; equity avg `-0.0252` n `130`; fx avg `0.0075` n `6`; index avg `0.0047` n `26`; metal avg `-0.0219` n `20`; unknown avg `0.1621` n `792`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `-0.3796` n `232`; crypto_major avg `-0.4027` n `8`; equity avg `-0.0852` n `130`; fx avg `0.0218` n `6`; index avg `-0.025` n `26`; metal avg `-0.0924` n `20`; unknown avg `0.0502` n `770`
- 4h: commodity avg `-0.0478` n `12`; crypto_alt avg `0.6592` n `232`; crypto_major avg `0.3871` n `8`; equity avg `0.3616` n `130`; fx avg `0.0159` n `6`; index avg `0.0662` n `26`; metal avg `-0.0184` n `20`; unknown avg `0.1373` n `770`
- 24h: commodity avg `0.3455` n `12`; crypto_alt avg `1.5428` n `232`; crypto_major avg `1.2888` n `8`; equity avg `0.3919` n `130`; fx avg `0.0452` n `6`; index avg `-0.0208` n `26`; metal avg `-0.2166` n `20`; unknown avg `0.263` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
