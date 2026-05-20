# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T05:37:14.017639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `0.1934` n `228`; crypto_major avg `0.1997` n `8`; equity avg `0.1098` n `66`; fx avg `-0.0149` n `6`; index avg `0.0705` n `23`; metal avg `0.2359` n `18`; unknown avg `-0.668` n `384`
- 1h: commodity avg `0.0803` n `12`; crypto_alt avg `0.9522` n `228`; crypto_major avg `0.6796` n `8`; equity avg `0.1059` n `66`; fx avg `0.0041` n `6`; index avg `0.1286` n `23`; metal avg `0.4778` n `18`; unknown avg `0.3453` n `384`
- 4h: commodity avg `-0.1905` n `12`; crypto_alt avg `1.3426` n `228`; crypto_major avg `1.0551` n `8`; equity avg `0.3326` n `66`; fx avg `-0.0208` n `6`; index avg `0.1676` n `23`; metal avg `0.6153` n `18`; unknown avg `0.5062` n `384`
- 24h: commodity avg `0.5415` n `12`; crypto_alt avg `-0.2344` n `228`; crypto_major avg `-0.1368` n `8`; equity avg `0.3208` n `66`; fx avg `-0.1455` n `6`; index avg `-0.4703` n `23`; metal avg `-1.497` n `18`; unknown avg `1.1192` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
