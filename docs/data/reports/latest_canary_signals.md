# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T15:45:33.789717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `-0.006` n `230`; crypto_major avg `0.0224` n `8`; equity avg `0.0167` n `114`; fx avg `-0.0007` n `6`; index avg `-0.0137` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.0291` n `792`
- 1h: commodity avg `0.0944` n `12`; crypto_alt avg `0.081` n `230`; crypto_major avg `0.1189` n `8`; equity avg `0.1843` n `114`; fx avg `0.0045` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0306` n `20`; unknown avg `-0.0412` n `792`
- 4h: commodity avg `0.1191` n `12`; crypto_alt avg `-0.0169` n `230`; crypto_major avg `0.2446` n `8`; equity avg `0.5129` n `114`; fx avg `0.0181` n `6`; index avg `0.0527` n `25`; metal avg `0.1046` n `20`; unknown avg `-0.0207` n `792`
- 24h: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1099` n `230`; crypto_major avg `0.9371` n `8`; equity avg `1.6542` n `114`; fx avg `0.0043` n `6`; index avg `0.2084` n `25`; metal avg `0.2717` n `20`; unknown avg `0.0828` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
