# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T10:37:26.029630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0782` n `12`; crypto_alt avg `0.1962` n `229`; crypto_major avg `0.1753` n `8`; equity avg `0.0322` n `88`; fx avg `-0.0037` n `6`; index avg `0.0125` n `25`; metal avg `0.0891` n `20`; unknown avg `0.0478` n `765`
- 1h: commodity avg `-0.0721` n `12`; crypto_alt avg `0.6197` n `229`; crypto_major avg `0.5799` n `8`; equity avg `0.0724` n `88`; fx avg `-0.0053` n `6`; index avg `0.0081` n `25`; metal avg `0.1729` n `20`; unknown avg `0.1412` n `765`
- 4h: commodity avg `-0.1882` n `12`; crypto_alt avg `0.3289` n `229`; crypto_major avg `0.0696` n `8`; equity avg `0.0779` n `88`; fx avg `0.0082` n `6`; index avg `0.0331` n `25`; metal avg `0.1284` n `20`; unknown avg `0.0507` n `765`
- 24h: commodity avg `-0.2172` n `12`; crypto_alt avg `0.414` n `229`; crypto_major avg `1.0194` n `8`; equity avg `-0.5426` n `88`; fx avg `0.0756` n `6`; index avg `0.0047` n `25`; metal avg `-0.1295` n `20`; unknown avg `1.2145` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
