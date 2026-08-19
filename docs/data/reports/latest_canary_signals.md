# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T08:26:49.074934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `0.0128` n `230`; crypto_major avg `0.0443` n `8`; equity avg `-0.1984` n `120`; fx avg `0.0202` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0141` n `20`; unknown avg `0.0225` n `789`
- 1h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.11` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `0.4605` n `120`; fx avg `-0.0422` n `6`; index avg `0.0807` n `25`; metal avg `0.049` n `20`; unknown avg `0.0285` n `789`
- 4h: commodity avg `-0.0318` n `12`; crypto_alt avg `0.1993` n `230`; crypto_major avg `0.0051` n `8`; equity avg `1.0089` n `120`; fx avg `-0.0392` n `6`; index avg `0.1991` n `25`; metal avg `0.0363` n `20`; unknown avg `-0.0144` n `757`
- 24h: commodity avg `0.2399` n `12`; crypto_alt avg `0.411` n `230`; crypto_major avg `0.2986` n `8`; equity avg `-1.3331` n `120`; fx avg `-0.2016` n `6`; index avg `-0.164` n `25`; metal avg `-0.4327` n `20`; unknown avg `-0.2179` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
