# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T07:07:27.694649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0769` n `12`; crypto_alt avg `0.2642` n `228`; crypto_major avg `0.1677` n `8`; equity avg `0.0064` n `88`; fx avg `0.0087` n `6`; index avg `0.0013` n `23`; metal avg `-0.018` n `20`; unknown avg `0.2143` n `764`
- 1h: commodity avg `0.1402` n `12`; crypto_alt avg `0.203` n `228`; crypto_major avg `0.1984` n `8`; equity avg `0.0359` n `88`; fx avg `0.0081` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0072` n `20`; unknown avg `0.0366` n `764`
- 4h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.1109` n `228`; crypto_major avg `-0.1049` n `8`; equity avg `-0.0017` n `88`; fx avg `0.0054` n `6`; index avg `0.0197` n `23`; metal avg `-0.0171` n `20`; unknown avg `-0.4169` n `732`
- 24h: commodity avg `0.3707` n `12`; crypto_alt avg `-0.4435` n `228`; crypto_major avg `-1.2478` n `8`; equity avg `-0.1126` n `88`; fx avg `-0.0175` n `6`; index avg `-0.1392` n `23`; metal avg `-0.0659` n `20`; unknown avg `16.1298` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
