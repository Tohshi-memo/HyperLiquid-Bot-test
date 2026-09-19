# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T17:37:30.610983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.5194` n `234`; crypto_major avg `-0.4235` n `8`; equity avg `-0.0455` n `140`; fx avg `0.0176` n `6`; index avg `-0.002` n `26`; metal avg `0.0035` n `20`; unknown avg `0.5513` n `943`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `-0.2204` n `234`; crypto_major avg `-0.3306` n `8`; equity avg `-0.0278` n `140`; fx avg `0.0182` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0012` n `20`; unknown avg `18.6044` n `899`
- 4h: commodity avg `-0.1179` n `12`; crypto_alt avg `0.1284` n `234`; crypto_major avg `-0.088` n `8`; equity avg `-0.0004` n `140`; fx avg `0.0091` n `6`; index avg `0.0116` n `26`; metal avg `-0.0085` n `20`; unknown avg `6.1906` n `882`
- 24h: commodity avg `-0.0456` n `12`; crypto_alt avg `2.4946` n `234`; crypto_major avg `1.2475` n `8`; equity avg `0.5076` n `140`; fx avg `0.0411` n `6`; index avg `0.1357` n `26`; metal avg `-0.1281` n `20`; unknown avg `2.2476` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
