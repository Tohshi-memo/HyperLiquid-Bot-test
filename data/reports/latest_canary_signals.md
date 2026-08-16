# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:07:27.698675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.016` n `230`; crypto_major avg `-0.0076` n `8`; equity avg `0.0104` n `114`; fx avg `0.0137` n `6`; index avg `-0.0027` n `25`; metal avg `0.0016` n `20`; unknown avg `0.022` n `791`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `0.059` n `230`; crypto_major avg `-0.0055` n `8`; equity avg `0.0057` n `114`; fx avg `0.0008` n `6`; index avg `0.0071` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0883` n `791`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.2078` n `230`; crypto_major avg `-0.0756` n `8`; equity avg `0.0588` n `114`; fx avg `0.0004` n `6`; index avg `0.0108` n `25`; metal avg `0.0221` n `20`; unknown avg `-0.1198` n `791`
- 24h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.3131` n `230`; crypto_major avg `-0.0759` n `8`; equity avg `0.2819` n `114`; fx avg `-0.0012` n `6`; index avg `0.0357` n `25`; metal avg `0.0511` n `20`; unknown avg `0.1568` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
