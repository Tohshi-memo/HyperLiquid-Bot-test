# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T08:52:32.182305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.0677` n `228`; crypto_major avg `-0.0358` n `8`; equity avg `-0.0935` n `74`; fx avg `0.0054` n `6`; index avg `-0.0087` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.1541` n `645`
- 1h: commodity avg `0.0257` n `12`; crypto_alt avg `0.1874` n `228`; crypto_major avg `0.0893` n `8`; equity avg `0.0269` n `74`; fx avg `0.0033` n `6`; index avg `0.0145` n `23`; metal avg `0.0266` n `18`; unknown avg `2.6264` n `645`
- 4h: commodity avg `-0.2846` n `12`; crypto_alt avg `0.2008` n `228`; crypto_major avg `-0.0492` n `8`; equity avg `0.1722` n `74`; fx avg `-0.0014` n `6`; index avg `0.0116` n `23`; metal avg `0.0301` n `18`; unknown avg `2.3451` n `625`
- 24h: commodity avg `-0.9198` n `12`; crypto_alt avg `0.5247` n `228`; crypto_major avg `0.7714` n `8`; equity avg `0.6702` n `74`; fx avg `0.0431` n `6`; index avg `0.2575` n `23`; metal avg `0.2575` n `18`; unknown avg `-0.2797` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
