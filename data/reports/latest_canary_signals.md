# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T14:52:27.044943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0383` n `230`; crypto_major avg `-0.0106` n `8`; equity avg `-0.0103` n `114`; fx avg `-0.0006` n `6`; index avg `-0.006` n `25`; metal avg `-0.0066` n `20`; unknown avg `0.0783` n `791`
- 1h: commodity avg `-0.0116` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.0449` n `8`; equity avg `0.0261` n `114`; fx avg `-0.0007` n `6`; index avg `-0.0119` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0451` n `791`
- 4h: commodity avg `-0.025` n `12`; crypto_alt avg `0.0955` n `230`; crypto_major avg `0.0892` n `8`; equity avg `-0.0505` n `114`; fx avg `-0.0149` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.008` n `791`
- 24h: commodity avg `0.0374` n `12`; crypto_alt avg `-0.0778` n `230`; crypto_major avg `0.0951` n `8`; equity avg `0.2793` n `114`; fx avg `-0.0152` n `6`; index avg `0.0304` n `25`; metal avg `0.0342` n `20`; unknown avg `0.1197` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
