# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T21:22:29.870825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `12`; crypto_alt avg `0.1358` n `230`; crypto_major avg `0.0818` n `8`; equity avg `-0.0196` n `121`; fx avg `-0.0139` n `6`; index avg `-0.0011` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0032` n `793`
- 1h: commodity avg `-0.0425` n `12`; crypto_alt avg `0.3027` n `230`; crypto_major avg `0.4693` n `8`; equity avg `0.0184` n `121`; fx avg `0.0019` n `6`; index avg `0.0161` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0555` n `792`
- 4h: commodity avg `0.1079` n `12`; crypto_alt avg `-0.3007` n `230`; crypto_major avg `-0.9716` n `8`; equity avg `0.3294` n `121`; fx avg `-0.0114` n `6`; index avg `-0.0216` n `25`; metal avg `0.056` n `20`; unknown avg `-0.3433` n `792`
- 24h: commodity avg `0.3118` n `12`; crypto_alt avg `3.5393` n `230`; crypto_major avg `4.2953` n `8`; equity avg `-0.8542` n `121`; fx avg `0.2183` n `6`; index avg `-0.0742` n `25`; metal avg `0.0478` n `20`; unknown avg `2.7422` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
