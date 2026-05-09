# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T12:52:12.342551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0593` n `12`; crypto_alt avg `-0.0179` n `228`; crypto_major avg `0.0427` n `8`; equity avg `-0.0173` n `65`; fx avg `0.0` n `5`; index avg `0.0035` n `23`; metal avg `-0.0017` n `18`; unknown avg `0.0394` n `376`
- 1h: commodity avg `0.1014` n `12`; crypto_alt avg `-0.1967` n `228`; crypto_major avg `-0.049` n `8`; equity avg `0.0492` n `65`; fx avg `0.0` n `5`; index avg `-0.004` n `23`; metal avg `0.0072` n `18`; unknown avg `-0.0692` n `376`
- 4h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.5936` n `228`; crypto_major avg `-0.2309` n `8`; equity avg `0.0552` n `65`; fx avg `-0.0036` n `5`; index avg `-0.0578` n `23`; metal avg `-0.0172` n `18`; unknown avg `-0.5787` n `376`
- 24h: commodity avg `-0.1175` n `12`; crypto_alt avg `3.0899` n `228`; crypto_major avg `2.1311` n `8`; equity avg `2.6187` n `65`; fx avg `-0.0027` n `5`; index avg `0.8565` n `23`; metal avg `-0.4343` n `18`; unknown avg `0.2867` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
