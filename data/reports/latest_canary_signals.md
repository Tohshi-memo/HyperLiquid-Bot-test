# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T05:07:28.227264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `0.1425` n `235`; crypto_major avg `-0.0013` n `8`; equity avg `0.018` n `150`; fx avg `0.0001` n `6`; index avg `0.0005` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0948` n `1115`
- 1h: commodity avg `0.0256` n `13`; crypto_alt avg `0.8511` n `235`; crypto_major avg `0.382` n `8`; equity avg `0.068` n `150`; fx avg `0.0053` n `6`; index avg `0.0065` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.4194` n `1115`
- 4h: commodity avg `0.1263` n `13`; crypto_alt avg `0.0029` n `235`; crypto_major avg `-0.0244` n `8`; equity avg `-0.0532` n `150`; fx avg `0.0087` n `6`; index avg `-0.0145` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.1051` n `1109`
- 24h: commodity avg `0.1783` n `13`; crypto_alt avg `0.5684` n `235`; crypto_major avg `0.0788` n `8`; equity avg `-0.0306` n `150`; fx avg `-0.0072` n `6`; index avg `-0.0402` n `26`; metal avg `-0.004` n `20`; unknown avg `0.4989` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
