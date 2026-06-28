# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T08:22:34.248354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0739` n `228`; crypto_major avg `0.0187` n `8`; equity avg `0.0145` n `88`; fx avg `-0.0119` n `6`; index avg `0.0084` n `23`; metal avg `0.0008` n `20`; unknown avg `5.1247` n `764`
- 1h: commodity avg `-0.0549` n `12`; crypto_alt avg `0.1163` n `228`; crypto_major avg `0.1713` n `8`; equity avg `0.1108` n `88`; fx avg `0.0003` n `6`; index avg `0.0423` n `23`; metal avg `0.0048` n `20`; unknown avg `5.6255` n `756`
- 4h: commodity avg `0.1177` n `12`; crypto_alt avg `-0.1132` n `228`; crypto_major avg `0.0299` n `8`; equity avg `0.1077` n `88`; fx avg `0.0029` n `6`; index avg `0.0327` n `23`; metal avg `-0.0393` n `20`; unknown avg `0.714` n `724`
- 24h: commodity avg `0.2578` n `12`; crypto_alt avg `-0.3077` n `228`; crypto_major avg `-1.0763` n `8`; equity avg `-0.0087` n `88`; fx avg `-0.0311` n `6`; index avg `-0.0872` n `23`; metal avg `-0.0405` n `20`; unknown avg `16.9526` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
