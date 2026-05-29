# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T15:07:21.625098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4825` n `12`; crypto_alt avg `0.4335` n `228`; crypto_major avg `0.6908` n `8`; equity avg `0.4497` n `69`; fx avg `0.0373` n `6`; index avg `0.0147` n `23`; metal avg `0.3934` n `18`; unknown avg `0.0172` n `418`
- 1h: commodity avg `-0.8415` n `12`; crypto_alt avg `0.7749` n `228`; crypto_major avg `1.089` n `8`; equity avg `-0.0164` n `69`; fx avg `0.0782` n `6`; index avg `-0.2374` n `23`; metal avg `0.4254` n `18`; unknown avg `0.0369` n `417`
- 4h: commodity avg `-0.5391` n `12`; crypto_alt avg `-0.2017` n `228`; crypto_major avg `0.2198` n `8`; equity avg `0.0528` n `69`; fx avg `0.097` n `6`; index avg `-0.2624` n `23`; metal avg `0.5158` n `18`; unknown avg `0.0129` n `417`
- 24h: commodity avg `-0.7063` n `12`; crypto_alt avg `1.6309` n `228`; crypto_major avg `2.0087` n `8`; equity avg `1.7507` n `69`; fx avg `0.2024` n `6`; index avg `0.2076` n `23`; metal avg `1.3579` n `18`; unknown avg `1.0451` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
