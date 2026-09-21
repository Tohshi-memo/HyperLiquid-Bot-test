# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T09:22:30.772897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3441` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3252` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `0.2572` n `234`; crypto_major avg `0.0272` n `8`; equity avg `-0.0355` n `140`; fx avg `0.0162` n `6`; index avg `-0.0044` n `26`; metal avg `0.0063` n `20`; unknown avg `0.0167` n `944`
- 1h: commodity avg `0.0946` n `12`; crypto_alt avg `1.3149` n `234`; crypto_major avg `1.4279` n `8`; equity avg `0.3048` n `140`; fx avg `-0.0047` n `6`; index avg `0.0226` n `26`; metal avg `0.0079` n `20`; unknown avg `9.4952` n `942`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `1.936` n `234`; crypto_major avg `2.3653` n `8`; equity avg `0.9291` n `140`; fx avg `-0.0836` n `6`; index avg `0.1394` n `26`; metal avg `0.0401` n `20`; unknown avg `10.1909` n `890`
- 24h: commodity avg `-0.5429` n `12`; crypto_alt avg `5.9244` n `234`; crypto_major avg `5.0819` n `8`; equity avg `1.9884` n `140`; fx avg `-0.0917` n `6`; index avg `0.3634` n `26`; metal avg `0.0351` n `20`; unknown avg `3.1937` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
