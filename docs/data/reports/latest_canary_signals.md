# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T16:52:34.491248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6812` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1004` n `12`; crypto_alt avg `0.2014` n `230`; crypto_major avg `0.4201` n `8`; equity avg `0.4852` n `102`; fx avg `0.0171` n `6`; index avg `0.0344` n `25`; metal avg `-0.0595` n `20`; unknown avg `-0.016` n `774`
- 1h: commodity avg `-0.0371` n `12`; crypto_alt avg `0.1359` n `230`; crypto_major avg `0.4096` n `8`; equity avg `0.3106` n `102`; fx avg `0.0169` n `6`; index avg `0.0278` n `25`; metal avg `-0.0606` n `20`; unknown avg `-0.1299` n `774`
- 4h: commodity avg `-0.6568` n `12`; crypto_alt avg `0.5706` n `230`; crypto_major avg `1.3295` n `8`; equity avg `-0.3517` n `102`; fx avg `0.0056` n `6`; index avg `0.121` n `25`; metal avg `0.066` n `20`; unknown avg `-0.1721` n `774`
- 24h: commodity avg `-1.2306` n `12`; crypto_alt avg `-1.5905` n `230`; crypto_major avg `-1.2872` n `8`; equity avg `-2.3189` n `102`; fx avg `-0.0783` n `6`; index avg `-0.1259` n `25`; metal avg `-0.3628` n `20`; unknown avg `1225.442` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
