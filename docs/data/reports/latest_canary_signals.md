# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T20:07:36.319543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0412` n `12`; crypto_alt avg `-0.0908` n `232`; crypto_major avg `-0.0328` n `8`; equity avg `-0.0553` n `131`; fx avg `0.0003` n `6`; index avg `0.0012` n `26`; metal avg `0.0138` n `20`; unknown avg `0.1518` n `791`
- 1h: commodity avg `0.0899` n `12`; crypto_alt avg `0.1866` n `232`; crypto_major avg `0.0601` n `8`; equity avg `0.0044` n `131`; fx avg `0.0129` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0135` n `20`; unknown avg `0.1593` n `791`
- 4h: commodity avg `0.6256` n `12`; crypto_alt avg `-0.7654` n `232`; crypto_major avg `-1.0194` n `8`; equity avg `-0.7831` n `131`; fx avg `0.0218` n `6`; index avg `-0.2` n `26`; metal avg `-0.4078` n `20`; unknown avg `2.3787` n `791`
- 24h: commodity avg `0.9354` n `12`; crypto_alt avg `-0.2564` n `232`; crypto_major avg `-2.1236` n `8`; equity avg `-1.9601` n `130`; fx avg `0.0421` n `6`; index avg `-0.3557` n `26`; metal avg `-0.9242` n `20`; unknown avg `0.1935` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0383`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0379`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0316`, n `668`, weak_sample_signal
