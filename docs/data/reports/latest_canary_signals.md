# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T21:22:27.403407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `0.1643` n `230`; crypto_major avg `0.0929` n `8`; equity avg `0.0185` n `96`; fx avg `0.0` n `6`; index avg `0.0017` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.2394` n `770`
- 1h: commodity avg `0.0329` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `-0.0563` n `8`; equity avg `0.014` n `96`; fx avg `-0.0015` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.2172` n `770`
- 4h: commodity avg `0.1098` n `12`; crypto_alt avg `0.3768` n `230`; crypto_major avg `0.5802` n `8`; equity avg `-0.0054` n `96`; fx avg `-0.0085` n `6`; index avg `-0.0308` n `25`; metal avg `-0.0229` n `20`; unknown avg `0.5955` n `770`
- 24h: commodity avg `0.3384` n `12`; crypto_alt avg `-0.2739` n `230`; crypto_major avg `0.3451` n `8`; equity avg `-0.2326` n `96`; fx avg `-0.0713` n `6`; index avg `0.0302` n `25`; metal avg `0.0044` n `20`; unknown avg `0.1051` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
