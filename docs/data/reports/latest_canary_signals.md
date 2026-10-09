# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T18:07:31.792422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `13`; crypto_alt avg `0.1494` n `235`; crypto_major avg `0.1095` n `8`; equity avg `0.0088` n `150`; fx avg `0.0119` n `6`; index avg `0.009` n `26`; metal avg `0.0173` n `20`; unknown avg `-0.1016` n `1090`
- 1h: commodity avg `0.0505` n `13`; crypto_alt avg `0.1708` n `235`; crypto_major avg `0.1264` n `8`; equity avg `0.1662` n `150`; fx avg `0.0167` n `6`; index avg `0.013` n `26`; metal avg `0.0529` n `20`; unknown avg `-0.0037` n `1090`
- 4h: commodity avg `-0.0488` n `13`; crypto_alt avg `0.8304` n `235`; crypto_major avg `0.1332` n `8`; equity avg `0.3199` n `150`; fx avg `0.0012` n `6`; index avg `0.0257` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.1539` n `1020`
- 24h: commodity avg `-0.1568` n `13`; crypto_alt avg `4.9149` n `235`; crypto_major avg `3.0087` n `8`; equity avg `1.522` n `150`; fx avg `0.0403` n `6`; index avg `0.2437` n `26`; metal avg `0.6471` n `20`; unknown avg `2.3412` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
