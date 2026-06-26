# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T11:07:33.037796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7034` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3014` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.042` n `12`; crypto_alt avg `0.1764` n `228`; crypto_major avg `0.2121` n `8`; equity avg `0.1751` n `86`; fx avg `-0.0057` n `6`; index avg `0.0137` n `23`; metal avg `0.0613` n `20`; unknown avg `0.0668` n `765`
- 1h: commodity avg `0.1216` n `12`; crypto_alt avg `-0.2125` n `228`; crypto_major avg `-0.2412` n `8`; equity avg `0.0856` n `86`; fx avg `0.007` n `6`; index avg `0.0135` n `23`; metal avg `0.1322` n `20`; unknown avg `-0.0048` n `765`
- 4h: commodity avg `-0.1665` n `12`; crypto_alt avg `-1.0029` n `228`; crypto_major avg `-1.3521` n `8`; equity avg `-0.2508` n `86`; fx avg `0.0382` n `6`; index avg `-0.0507` n `23`; metal avg `0.3513` n `20`; unknown avg `-0.0477` n `765`
- 24h: commodity avg `0.1335` n `12`; crypto_alt avg `-1.7493` n `228`; crypto_major avg `-1.5788` n `8`; equity avg `-4.1059` n `86`; fx avg `0.0603` n `6`; index avg `-0.6289` n `23`; metal avg `0.7305` n `20`; unknown avg `0.8145` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.272`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
