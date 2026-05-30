# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T00:22:18.402368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.1303` n `228`; crypto_major avg `0.1159` n `8`; equity avg `0.052` n `69`; fx avg `-0.0011` n `6`; index avg `-0.0027` n `23`; metal avg `0.0081` n `18`; unknown avg `-0.4452` n `419`
- 1h: commodity avg `0.0727` n `12`; crypto_alt avg `0.3886` n `228`; crypto_major avg `0.3655` n `8`; equity avg `-0.0178` n `69`; fx avg `0.0035` n `6`; index avg `0.0689` n `23`; metal avg `0.038` n `18`; unknown avg `-0.2265` n `419`
- 4h: commodity avg `0.2932` n `12`; crypto_alt avg `-0.0138` n `228`; crypto_major avg `-0.2373` n `8`; equity avg `-0.0057` n `69`; fx avg `-0.0676` n `6`; index avg `0.0008` n `23`; metal avg `-0.0586` n `18`; unknown avg `-0.3921` n `419`
- 24h: commodity avg `-0.1161` n `12`; crypto_alt avg `0.536` n `228`; crypto_major avg `0.6441` n `8`; equity avg `0.6928` n `69`; fx avg `0.1166` n `6`; index avg `0.1179` n `23`; metal avg `-0.0424` n `18`; unknown avg `0.3105` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
