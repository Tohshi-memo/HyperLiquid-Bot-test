# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T00:37:29.402930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1133` n `12`; crypto_alt avg `-0.1897` n `232`; crypto_major avg `-0.2355` n `8`; equity avg `-0.0423` n `132`; fx avg `0.0027` n `6`; index avg `-0.0219` n `26`; metal avg `-0.0352` n `20`; unknown avg `0.3209` n `792`
- 1h: commodity avg `0.1716` n `12`; crypto_alt avg `-0.0671` n `232`; crypto_major avg `-0.2393` n `8`; equity avg `0.2161` n `132`; fx avg `-0.0475` n `6`; index avg `0.0406` n `26`; metal avg `-0.0517` n `20`; unknown avg `2.6447` n `790`
- 4h: commodity avg `0.1408` n `12`; crypto_alt avg `-0.1255` n `232`; crypto_major avg `-0.1891` n `8`; equity avg `-0.032` n `132`; fx avg `-0.0469` n `6`; index avg `0.0225` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.3144` n `784`
- 24h: commodity avg `0.9735` n `12`; crypto_alt avg `-0.8848` n `232`; crypto_major avg `-1.9406` n `8`; equity avg `-1.9452` n `130`; fx avg `-0.0315` n `6`; index avg `-0.3299` n `26`; metal avg `-1.0034` n `20`; unknown avg `0.2194` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0414`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.031`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0304`, n `668`, weak_sample_signal
