# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T02:02:32.830228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.0446` n `230`; crypto_major avg `0.0296` n `8`; equity avg `0.0124` n `114`; fx avg `-0.0059` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.2063` n `791`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0133` n `230`; crypto_major avg `0.1193` n `8`; equity avg `0.0453` n `114`; fx avg `-0.0079` n `6`; index avg `0.0036` n `25`; metal avg `-0.0295` n `20`; unknown avg `0.1051` n `791`
- 4h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.2039` n `230`; crypto_major avg `0.3037` n `8`; equity avg `0.0013` n `114`; fx avg `-0.0317` n `6`; index avg `-0.0058` n `25`; metal avg `0.0256` n `20`; unknown avg `0.2579` n `791`
- 24h: commodity avg `0.2234` n `12`; crypto_alt avg `-0.184` n `230`; crypto_major avg `-0.7395` n `8`; equity avg `-0.1327` n `114`; fx avg `0.0982` n `6`; index avg `-0.0455` n `25`; metal avg `0.4878` n `20`; unknown avg `-0.1915` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
