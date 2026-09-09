# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T06:20:25.357840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0378` n `12`; crypto_alt avg `0.3481` n `233`; crypto_major avg `0.3422` n `8`; equity avg `0.0906` n `134`; fx avg `0.016` n `6`; index avg `0.0012` n `26`; metal avg `0.0054` n `20`; unknown avg `1.855` n `798`
- 1h: commodity avg `0.0271` n `12`; crypto_alt avg `0.0722` n `233`; crypto_major avg `0.1303` n `8`; equity avg `0.2066` n `134`; fx avg `-0.0063` n `6`; index avg `0.0361` n `26`; metal avg `0.1396` n `20`; unknown avg `1.7404` n `778`
- 4h: commodity avg `-0.0805` n `12`; crypto_alt avg `0.9632` n `233`; crypto_major avg `0.7174` n `8`; equity avg `0.0082` n `134`; fx avg `-0.0698` n `6`; index avg `-0.0153` n `26`; metal avg `0.2023` n `20`; unknown avg `1.6285` n `769`
- 24h: commodity avg `-0.1576` n `12`; crypto_alt avg `0.5489` n `232`; crypto_major avg `1.6387` n `8`; equity avg `1.3447` n `134`; fx avg `-0.1186` n `6`; index avg `0.0423` n `26`; metal avg `0.0059` n `20`; unknown avg `0.7335` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
