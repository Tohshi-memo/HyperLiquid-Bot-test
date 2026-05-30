# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T05:07:17.492138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.384` n `228`; crypto_major avg `0.3168` n `8`; equity avg `0.0713` n `69`; fx avg `-0.0003` n `6`; index avg `-0.0042` n `23`; metal avg `0.0269` n `18`; unknown avg `1.5067` n `419`
- 1h: commodity avg `-0.1799` n `12`; crypto_alt avg `-0.0323` n `228`; crypto_major avg `-0.0658` n `8`; equity avg `0.1063` n `69`; fx avg `-0.0027` n `6`; index avg `0.0235` n `23`; metal avg `0.0467` n `18`; unknown avg `0.2625` n `419`
- 4h: commodity avg `-0.1868` n `12`; crypto_alt avg `0.3843` n `228`; crypto_major avg `0.3891` n `8`; equity avg `0.2105` n `69`; fx avg `-0.0001` n `6`; index avg `0.0066` n `23`; metal avg `0.0179` n `18`; unknown avg `0.4286` n `419`
- 24h: commodity avg `-0.2742` n `12`; crypto_alt avg `1.6084` n `228`; crypto_major avg `1.6987` n `8`; equity avg `0.803` n `69`; fx avg `0.088` n `6`; index avg `-0.0101` n `23`; metal avg `-0.0943` n `18`; unknown avg `1.5596` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
