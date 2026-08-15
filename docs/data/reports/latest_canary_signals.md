# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T10:22:28.012779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0331` n `12`; crypto_alt avg `0.0375` n `230`; crypto_major avg `0.0379` n `8`; equity avg `0.0132` n `114`; fx avg `-0.0006` n `6`; index avg `0.0069` n `25`; metal avg `0.003` n `20`; unknown avg `0.0205` n `791`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `0.0631` n `8`; equity avg `0.0211` n `114`; fx avg `-0.0107` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.1092` n `791`
- 4h: commodity avg `-0.2077` n `12`; crypto_alt avg `0.0488` n `230`; crypto_major avg `-0.0993` n `8`; equity avg `0.0592` n `114`; fx avg `-0.0109` n `6`; index avg `0.0067` n `25`; metal avg `0.0184` n `20`; unknown avg `0.0824` n `791`
- 24h: commodity avg `-0.0612` n `12`; crypto_alt avg `1.1725` n `230`; crypto_major avg `0.111` n `8`; equity avg `-0.5527` n `114`; fx avg `0.1297` n `6`; index avg `-0.142` n `25`; metal avg `0.1897` n `20`; unknown avg `-0.0469` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
