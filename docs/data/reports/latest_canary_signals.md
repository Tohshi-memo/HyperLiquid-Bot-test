# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T23:52:29.802190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0378` n `230`; crypto_major avg `-0.0161` n `8`; equity avg `0.0067` n `113`; fx avg `-0.0064` n `6`; index avg `0.0073` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.166` n `787`
- 1h: commodity avg `0.0555` n `12`; crypto_alt avg `-0.002` n `230`; crypto_major avg `-0.1088` n `8`; equity avg `-0.0349` n `113`; fx avg `-0.0055` n `6`; index avg `0.0188` n `25`; metal avg `0.0424` n `20`; unknown avg `-0.1984` n `787`
- 4h: commodity avg `0.0418` n `12`; crypto_alt avg `0.3101` n `230`; crypto_major avg `-0.0099` n `8`; equity avg `0.3339` n `113`; fx avg `-0.001` n `6`; index avg `0.0745` n `25`; metal avg `0.0763` n `20`; unknown avg `0.0122` n `787`
- 24h: commodity avg `-0.4194` n `12`; crypto_alt avg `0.5281` n `230`; crypto_major avg `0.594` n `8`; equity avg `1.6047` n `113`; fx avg `0.0118` n `6`; index avg `0.363` n `25`; metal avg `-0.4468` n `20`; unknown avg `0.1531` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
