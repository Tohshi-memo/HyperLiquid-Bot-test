# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T21:22:18.594216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1024` n `12`; crypto_alt avg `-0.073` n `228`; crypto_major avg `-0.1261` n `8`; equity avg `-0.0337` n `69`; fx avg `-0.0058` n `6`; index avg `-0.0107` n `23`; metal avg `0.0314` n `18`; unknown avg `0.1852` n `419`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `-0.0557` n `228`; crypto_major avg `-0.2035` n `8`; equity avg `0.0159` n `69`; fx avg `-0.0516` n `6`; index avg `-0.0634` n `23`; metal avg `-0.1502` n `18`; unknown avg `0.1308` n `419`
- 4h: commodity avg `0.0963` n `12`; crypto_alt avg `-0.8087` n `228`; crypto_major avg `-0.9097` n `8`; equity avg `-0.0166` n `69`; fx avg `-0.0134` n `6`; index avg `-0.0827` n `23`; metal avg `-0.1642` n `18`; unknown avg `-0.1748` n `419`
- 24h: commodity avg `-0.3111` n `12`; crypto_alt avg `0.2323` n `228`; crypto_major avg `0.5466` n `8`; equity avg `1.213` n `69`; fx avg `0.1766` n `6`; index avg `0.1165` n `23`; metal avg `0.0067` n `18`; unknown avg `0.4975` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
