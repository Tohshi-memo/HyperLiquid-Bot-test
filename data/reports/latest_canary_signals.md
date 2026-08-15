# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T13:52:32.859748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0293` n `230`; crypto_major avg `-0.0314` n `8`; equity avg `0.0205` n `114`; fx avg `0.0082` n `6`; index avg `0.0022` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0104` n `791`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1448` n `230`; crypto_major avg `0.14` n `8`; equity avg `0.0199` n `114`; fx avg `-0.0001` n `6`; index avg `0.0057` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0132` n `791`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `0.026` n `230`; crypto_major avg `0.1195` n `8`; equity avg `0.0222` n `114`; fx avg `-0.0055` n `6`; index avg `0.0271` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0674` n `791`
- 24h: commodity avg `0.0693` n `12`; crypto_alt avg `1.0548` n `230`; crypto_major avg `0.5016` n `8`; equity avg `-0.5383` n `114`; fx avg `0.0894` n `6`; index avg `-0.1042` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.0788` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
