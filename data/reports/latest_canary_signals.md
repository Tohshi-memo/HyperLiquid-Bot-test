# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T08:52:29.088617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.0455` n `228`; crypto_major avg `0.0644` n `8`; equity avg `-0.2051` n `86`; fx avg `-0.0047` n `6`; index avg `-0.0382` n `23`; metal avg `-0.022` n `20`; unknown avg `0.0265` n `765`
- 1h: commodity avg `-0.0989` n `12`; crypto_alt avg `-0.4196` n `228`; crypto_major avg `-0.554` n `8`; equity avg `-0.3846` n `86`; fx avg `0.0254` n `6`; index avg `-0.0713` n `23`; metal avg `0.038` n `20`; unknown avg `-0.0112` n `765`
- 4h: commodity avg `-0.1386` n `12`; crypto_alt avg `1.0126` n `228`; crypto_major avg `1.2101` n `8`; equity avg `0.5483` n `86`; fx avg `-0.0253` n `6`; index avg `0.1773` n `23`; metal avg `0.6191` n `20`; unknown avg `0.2331` n `733`
- 24h: commodity avg `0.0661` n `12`; crypto_alt avg `-1.7143` n `228`; crypto_major avg `-1.6259` n `8`; equity avg `-3.9759` n `86`; fx avg `0.0246` n `6`; index avg `-0.5866` n `23`; metal avg `0.4097` n `20`; unknown avg `0.4443` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
