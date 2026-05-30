# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T00:37:15.087526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.1497` n `228`; crypto_major avg `0.0943` n `8`; equity avg `0.0422` n `69`; fx avg `0.0018` n `6`; index avg `-0.0188` n `23`; metal avg `-0.0192` n `18`; unknown avg `1.0704` n `419`
- 1h: commodity avg `0.0628` n `12`; crypto_alt avg `0.5257` n `228`; crypto_major avg `0.476` n `8`; equity avg `0.0103` n `69`; fx avg `-0.0063` n `6`; index avg `-0.0605` n `23`; metal avg `0.0099` n `18`; unknown avg `0.7593` n `419`
- 4h: commodity avg `0.2892` n `12`; crypto_alt avg `0.0061` n `228`; crypto_major avg `-0.1674` n `8`; equity avg `-0.0087` n `69`; fx avg `-0.0355` n `6`; index avg `-0.007` n `23`; metal avg `-0.0411` n `18`; unknown avg `0.4452` n `419`
- 24h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.5` n `228`; crypto_major avg `0.718` n `8`; equity avg `0.7985` n `69`; fx avg `0.1031` n `6`; index avg `0.172` n `23`; metal avg `0.1047` n `18`; unknown avg `1.1137` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
