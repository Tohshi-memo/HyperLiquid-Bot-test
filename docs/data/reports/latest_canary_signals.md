# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T20:22:25.479958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.0625` n `230`; crypto_major avg `0.0295` n `8`; equity avg `0.0203` n `92`; fx avg `0.0` n `6`; index avg `-0.0065` n `25`; metal avg `-0.005` n `20`; unknown avg `0.0056` n `765`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.0783` n `230`; crypto_major avg `0.0104` n `8`; equity avg `0.0577` n `92`; fx avg `0.0086` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.1556` n `765`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `0.5736` n `230`; crypto_major avg `0.3359` n `8`; equity avg `0.2203` n `92`; fx avg `0.0223` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.0061` n `765`
- 24h: commodity avg `0.0078` n `12`; crypto_alt avg `1.3174` n `229`; crypto_major avg `0.9529` n `8`; equity avg `0.416` n `92`; fx avg `0.0051` n `6`; index avg `0.0154` n `25`; metal avg `-0.0054` n `20`; unknown avg `2.3893` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
