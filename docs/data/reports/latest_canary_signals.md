# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T13:22:30.968165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `0.022` n `230`; crypto_major avg `-0.0112` n `8`; equity avg `-0.1736` n `114`; fx avg `0.004` n `6`; index avg `-0.0242` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.0337` n `786`
- 1h: commodity avg `-0.1447` n `12`; crypto_alt avg `0.1861` n `230`; crypto_major avg `-0.1325` n `8`; equity avg `0.0437` n `114`; fx avg `0.0035` n `6`; index avg `0.0117` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0704` n `786`
- 4h: commodity avg `-0.1517` n `12`; crypto_alt avg `-0.1354` n `230`; crypto_major avg `-0.509` n `8`; equity avg `0.1257` n `114`; fx avg `0.0271` n `6`; index avg `0.0153` n `25`; metal avg `0.1308` n `20`; unknown avg `4.1435` n `786`
- 24h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.6414` n `230`; crypto_major avg `-1.1363` n `8`; equity avg `1.6027` n `114`; fx avg `-0.0375` n `6`; index avg `0.2857` n `25`; metal avg `-0.0492` n `20`; unknown avg `0.9242` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
