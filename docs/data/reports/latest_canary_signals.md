# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T21:37:17.922745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.0374` n `228`; crypto_major avg `0.0561` n `8`; equity avg `0.0446` n `69`; fx avg `0.0014` n `6`; index avg `-0.0776` n `23`; metal avg `0.013` n `18`; unknown avg `0.1694` n `421`
- 1h: commodity avg `-0.0645` n `12`; crypto_alt avg `0.3714` n `228`; crypto_major avg `0.4254` n `8`; equity avg `0.0997` n `69`; fx avg `-0.0033` n `6`; index avg `0.0948` n `23`; metal avg `0.0282` n `18`; unknown avg `1.0015` n `421`
- 4h: commodity avg `-0.129` n `12`; crypto_alt avg `0.9047` n `228`; crypto_major avg `0.5325` n `8`; equity avg `0.1153` n `69`; fx avg `-0.0161` n `6`; index avg `0.0991` n `23`; metal avg `0.0117` n `18`; unknown avg `0.4756` n `421`
- 24h: commodity avg `0.405` n `12`; crypto_alt avg `-0.6284` n `228`; crypto_major avg `-0.1796` n `8`; equity avg `0.7681` n `69`; fx avg `-0.034` n `6`; index avg `0.2437` n `23`; metal avg `-0.1261` n `18`; unknown avg `1.8009` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2927`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
