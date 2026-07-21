# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T11:58:59.216209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.0123` n `230`; crypto_major avg `0.0381` n `8`; equity avg `0.0165` n `98`; fx avg `-0.0006` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0222` n `20`; unknown avg `0.006` n `771`
- 1h: commodity avg `0.0693` n `12`; crypto_alt avg `0.0091` n `230`; crypto_major avg `0.171` n `8`; equity avg `-0.091` n `98`; fx avg `0.0009` n `6`; index avg `-0.028` n `25`; metal avg `-0.0595` n `20`; unknown avg `-0.0672` n `771`
- 4h: commodity avg `0.3358` n `12`; crypto_alt avg `-0.1614` n `230`; crypto_major avg `0.0383` n `8`; equity avg `0.234` n `98`; fx avg `0.0007` n `6`; index avg `0.0433` n `25`; metal avg `-0.0718` n `20`; unknown avg `0.0526` n `771`
- 24h: commodity avg `0.753` n `12`; crypto_alt avg `1.6358` n `230`; crypto_major avg `1.6826` n `8`; equity avg `0.894` n `98`; fx avg `-0.0744` n `6`; index avg `0.1171` n `25`; metal avg `0.4551` n `20`; unknown avg `0.1141` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0871`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0647`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
