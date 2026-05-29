# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T23:52:17.235186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `0.2072` n `228`; crypto_major avg `0.2272` n `8`; equity avg `0.0121` n `69`; fx avg `-0.0078` n `6`; index avg `-0.0734` n `23`; metal avg `0.0195` n `18`; unknown avg `0.0738` n `419`
- 1h: commodity avg `0.1041` n `12`; crypto_alt avg `0.2637` n `228`; crypto_major avg `0.1597` n `8`; equity avg `0.0181` n `69`; fx avg `-0.0133` n `6`; index avg `0.0115` n `23`; metal avg `0.0166` n `18`; unknown avg `-0.2363` n `419`
- 4h: commodity avg `0.1616` n `12`; crypto_alt avg `0.0284` n `228`; crypto_major avg `-0.3222` n `8`; equity avg `0.1093` n `69`; fx avg `-0.046` n `6`; index avg `0.0109` n `23`; metal avg `-0.0732` n `18`; unknown avg `-0.5876` n `419`
- 24h: commodity avg `-0.3419` n `12`; crypto_alt avg `0.7705` n `228`; crypto_major avg `0.8511` n `8`; equity avg `0.8034` n `69`; fx avg `0.152` n `6`; index avg `0.11` n `23`; metal avg `0.1067` n `18`; unknown avg `0.497` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
