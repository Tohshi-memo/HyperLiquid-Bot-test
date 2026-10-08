# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T12:37:28.525780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `13`; crypto_alt avg `-0.1808` n `235`; crypto_major avg `-0.1539` n `8`; equity avg `0.0498` n `150`; fx avg `-0.0027` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0205` n `20`; unknown avg `-0.1292` n `1077`
- 1h: commodity avg `0.0288` n `13`; crypto_alt avg `-0.3018` n `235`; crypto_major avg `-0.2932` n `8`; equity avg `0.0885` n `150`; fx avg `0.0167` n `6`; index avg `0.0221` n `26`; metal avg `0.0076` n `20`; unknown avg `0.0025` n `1069`
- 4h: commodity avg `0.1567` n `13`; crypto_alt avg `-0.4836` n `235`; crypto_major avg `-0.9949` n `8`; equity avg `-0.2862` n `150`; fx avg `0.0464` n `6`; index avg `-0.0405` n `26`; metal avg `-0.1162` n `20`; unknown avg `0.3574` n `1069`
- 24h: commodity avg `0.7529` n `13`; crypto_alt avg `-0.109` n `235`; crypto_major avg `-2.383` n `8`; equity avg `-1.1773` n `150`; fx avg `0.0772` n `6`; index avg `-0.1852` n `26`; metal avg `0.1939` n `20`; unknown avg `416.6687` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
