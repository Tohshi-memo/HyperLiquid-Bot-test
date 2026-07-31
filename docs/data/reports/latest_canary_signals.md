# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T16:22:26.300785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.0765` n `230`; crypto_major avg `0.0818` n `8`; equity avg `0.153` n `102`; fx avg `-0.0087` n `6`; index avg `0.0567` n `25`; metal avg `0.0217` n `20`; unknown avg `0.0092` n `780`
- 1h: commodity avg `-0.1809` n `12`; crypto_alt avg `0.3139` n `230`; crypto_major avg `0.2512` n `8`; equity avg `-0.0106` n `102`; fx avg `0.0274` n `6`; index avg `0.0554` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.2966` n `780`
- 4h: commodity avg `-0.317` n `12`; crypto_alt avg `0.1954` n `230`; crypto_major avg `-0.7228` n `8`; equity avg `-2.0954` n `102`; fx avg `-0.0738` n `6`; index avg `-0.2214` n `25`; metal avg `-0.0399` n `20`; unknown avg `0.5757` n `780`
- 24h: commodity avg `0.083` n `12`; crypto_alt avg `-0.4565` n `230`; crypto_major avg `-1.6699` n `8`; equity avg `-0.0735` n `102`; fx avg `0.1307` n `6`; index avg `0.2006` n `25`; metal avg `-0.3939` n `20`; unknown avg `0.7532` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
