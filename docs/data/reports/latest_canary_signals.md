# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T13:07:32.019799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0589` n `230`; crypto_major avg `0.0717` n `8`; equity avg `0.0018` n `114`; fx avg `0.0035` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0793` n `791`
- 1h: commodity avg `-0.0035` n `12`; crypto_alt avg `0.1186` n `230`; crypto_major avg `0.0475` n `8`; equity avg `-0.0945` n `114`; fx avg `0.0008` n `6`; index avg `0.0012` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.0161` n `791`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1282` n `230`; crypto_major avg `-0.0743` n `8`; equity avg `-0.158` n `114`; fx avg `-0.0083` n `6`; index avg `-0.0079` n `25`; metal avg `0.0064` n `20`; unknown avg `0.102` n `791`
- 24h: commodity avg `0.0561` n `12`; crypto_alt avg `0.1747` n `230`; crypto_major avg `0.0261` n `8`; equity avg `0.2443` n `114`; fx avg `-0.0083` n `6`; index avg `0.0377` n `25`; metal avg `0.0327` n `20`; unknown avg `0.0894` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2164`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
