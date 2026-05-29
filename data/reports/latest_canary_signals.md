# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T23:37:19.058581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0129` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `0.0143` n `69`; fx avg `0.0116` n `6`; index avg `0.112` n `23`; metal avg `0.0089` n `18`; unknown avg `-0.0549` n `419`
- 1h: commodity avg `0.1403` n `12`; crypto_alt avg `0.0108` n `228`; crypto_major avg `-0.1669` n `8`; equity avg `-0.0105` n `69`; fx avg `-0.0024` n `6`; index avg `0.055` n `23`; metal avg `0.0024` n `18`; unknown avg `-0.2522` n `419`
- 4h: commodity avg `0.2765` n `12`; crypto_alt avg `-0.1913` n `228`; crypto_major avg `-0.606` n `8`; equity avg `0.2389` n `69`; fx avg `-0.0399` n `6`; index avg `0.0596` n `23`; metal avg `-0.1968` n `18`; unknown avg `-0.6044` n `419`
- 24h: commodity avg `-0.2946` n `12`; crypto_alt avg `0.4685` n `228`; crypto_major avg `0.4138` n `8`; equity avg `0.7629` n `69`; fx avg `0.1702` n `6`; index avg `0.1752` n `23`; metal avg `0.0297` n `18`; unknown avg `0.3393` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
