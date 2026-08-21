# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T10:37:30.661604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6361` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0781` n `12`; crypto_alt avg `-0.2015` n `230`; crypto_major avg `-0.3803` n `8`; equity avg `-0.0127` n `121`; fx avg `0.0086` n `6`; index avg `0.0027` n `25`; metal avg `0.0391` n `20`; unknown avg `-0.0067` n `793`
- 1h: commodity avg `0.0374` n `12`; crypto_alt avg `0.2672` n `230`; crypto_major avg `-0.3331` n `8`; equity avg `0.0632` n `121`; fx avg `0.0231` n `6`; index avg `0.0023` n `25`; metal avg `-0.0425` n `20`; unknown avg `0.0993` n `793`
- 4h: commodity avg `0.1045` n `12`; crypto_alt avg `2.3795` n `230`; crypto_major avg `1.7451` n `8`; equity avg `0.5049` n `121`; fx avg `-0.0192` n `6`; index avg `0.0007` n `25`; metal avg `0.109` n `20`; unknown avg `0.3946` n `793`
- 24h: commodity avg `0.1352` n `12`; crypto_alt avg `6.711` n `230`; crypto_major avg `6.5566` n `8`; equity avg `0.5496` n `121`; fx avg `-0.072` n `6`; index avg `-0.0126` n `25`; metal avg `0.7308` n `20`; unknown avg `2.4006` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
