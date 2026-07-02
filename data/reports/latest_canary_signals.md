# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T01:52:31.410240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0396` n `228`; crypto_major avg `-0.1189` n `8`; equity avg `0.0357` n `88`; fx avg `0.0201` n `6`; index avg `0.0166` n `25`; metal avg `0.0506` n `20`; unknown avg `-0.1094` n `761`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `0.8989` n `228`; crypto_major avg `0.7209` n `8`; equity avg `0.6509` n `88`; fx avg `0.0089` n `6`; index avg `0.2586` n `25`; metal avg `0.1674` n `20`; unknown avg `-0.4385` n `761`
- 4h: commodity avg `-0.1396` n `12`; crypto_alt avg `-0.4062` n `228`; crypto_major avg `-0.8809` n `8`; equity avg `-0.0215` n `88`; fx avg `0.0574` n `6`; index avg `0.0853` n `25`; metal avg `0.3206` n `20`; unknown avg `23.6115` n `761`
- 24h: commodity avg `-0.6168` n `12`; crypto_alt avg `2.4738` n `228`; crypto_major avg `1.4024` n `8`; equity avg `-0.8281` n `88`; fx avg `-0.0192` n `6`; index avg `-0.223` n `25`; metal avg `0.9869` n `20`; unknown avg `25.1526` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
