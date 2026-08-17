# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T12:22:24.087458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.0101` n `230`; crypto_major avg `-0.0469` n `8`; equity avg `-0.0352` n `114`; fx avg `0.0016` n `6`; index avg `0.0005` n `25`; metal avg `-0.0123` n `20`; unknown avg `0.0055` n `792`
- 1h: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.0774` n `230`; crypto_major avg `-0.1704` n `8`; equity avg `-0.1541` n `114`; fx avg `0.0022` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0893` n `20`; unknown avg `0.0189` n `792`
- 4h: commodity avg `0.0651` n `12`; crypto_alt avg `0.1006` n `230`; crypto_major avg `0.1819` n `8`; equity avg `-0.2232` n `114`; fx avg `0.0` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0975` n `20`; unknown avg `0.0651` n `792`
- 24h: commodity avg `-0.1273` n `12`; crypto_alt avg `-0.0347` n `230`; crypto_major avg `0.8022` n `8`; equity avg `1.0534` n `114`; fx avg `-0.0112` n `6`; index avg `0.1305` n `25`; metal avg `0.1103` n `20`; unknown avg `0.0963` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
