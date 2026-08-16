# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T17:37:24.619537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `-0.0227` n `230`; crypto_major avg `-0.0437` n `8`; equity avg `-0.0224` n `114`; fx avg `0.0036` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0313` n `791`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.1646` n `230`; crypto_major avg `-0.0943` n `8`; equity avg `-0.0104` n `114`; fx avg `-0.0001` n `6`; index avg `-0.0076` n `25`; metal avg `0.011` n `20`; unknown avg `0.2502` n `791`
- 4h: commodity avg `0.025` n `12`; crypto_alt avg `0.0329` n `230`; crypto_major avg `0.253` n `8`; equity avg `0.1162` n `114`; fx avg `0.0129` n `6`; index avg `-0.0085` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.0258` n `791`
- 24h: commodity avg `0.0409` n `12`; crypto_alt avg `-0.289` n `230`; crypto_major avg `0.1249` n `8`; equity avg `0.3072` n `114`; fx avg `0.0039` n `6`; index avg `0.0233` n `25`; metal avg `0.0588` n `20`; unknown avg `0.1421` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
