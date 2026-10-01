# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T08:37:29.951067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0999` n `13`; crypto_alt avg `-0.0988` n `234`; crypto_major avg `-0.0319` n `8`; equity avg `-0.0505` n `142`; fx avg `-0.0194` n `6`; index avg `-0.0012` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.0731` n `975`
- 1h: commodity avg `0.0985` n `13`; crypto_alt avg `-0.3855` n `234`; crypto_major avg `-0.2734` n `8`; equity avg `-0.2551` n `142`; fx avg `-0.0377` n `6`; index avg `-0.0617` n `26`; metal avg `-0.1054` n `20`; unknown avg `5.2803` n `957`
- 4h: commodity avg `0.8985` n `13`; crypto_alt avg `-1.0792` n `234`; crypto_major avg `-0.6365` n `8`; equity avg `-0.5205` n `142`; fx avg `-0.0322` n `6`; index avg `-0.172` n `26`; metal avg `-0.3193` n `20`; unknown avg `4.0183` n `930`
- 24h: commodity avg `0.285` n `13`; crypto_alt avg `0.2265` n `234`; crypto_major avg `0.5824` n `8`; equity avg `-0.0172` n `142`; fx avg `0.1277` n `6`; index avg `-0.0086` n `26`; metal avg `-0.5141` n `20`; unknown avg `773.2904` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
