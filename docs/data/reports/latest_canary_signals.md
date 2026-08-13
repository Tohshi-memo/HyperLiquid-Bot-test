# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T21:07:25.683012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `0.0996` n `8`; equity avg `-0.0217` n `113`; fx avg `-0.0065` n `6`; index avg `0.0006` n `25`; metal avg `0.0361` n `20`; unknown avg `0.0051` n `787`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.0393` n `230`; crypto_major avg `0.0482` n `8`; equity avg `0.1099` n `113`; fx avg `-0.0034` n `6`; index avg `0.0186` n `25`; metal avg `0.0402` n `20`; unknown avg `-0.0932` n `787`
- 4h: commodity avg `-0.1858` n `12`; crypto_alt avg `0.2342` n `230`; crypto_major avg `0.4478` n `8`; equity avg `-0.1327` n `113`; fx avg `0.0104` n `6`; index avg `-0.0126` n `25`; metal avg `-0.1774` n `20`; unknown avg `0.2507` n `787`
- 24h: commodity avg `-0.4611` n `12`; crypto_alt avg `-0.2358` n `230`; crypto_major avg `0.3258` n `8`; equity avg `1.5734` n `113`; fx avg `0.0137` n `6`; index avg `0.3294` n `25`; metal avg `-0.4979` n `20`; unknown avg `0.0642` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2429`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
