# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T15:53:11.935967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.81` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.2087` n `12`; crypto_alt avg `-0.1154` n `230`; crypto_major avg `-0.1137` n `8`; equity avg `-0.116` n `102`; fx avg `-0.0052` n `6`; index avg `0.0177` n `25`; metal avg `0.0164` n `20`; unknown avg `-0.1089` n `780`
- 1h: commodity avg `-0.3511` n `12`; crypto_alt avg `-0.0936` n `230`; crypto_major avg `-0.2726` n `8`; equity avg `-0.6842` n `102`; fx avg `0.0018` n `6`; index avg `-0.0659` n `25`; metal avg `0.0178` n `20`; unknown avg `0.0127` n `780`
- 4h: commodity avg `-0.4125` n `12`; crypto_alt avg `-0.0051` n `230`; crypto_major avg `-0.8789` n `8`; equity avg `-2.6889` n `102`; fx avg `-0.0621` n `6`; index avg `-0.3095` n `25`; metal avg `0.0032` n `20`; unknown avg `0.8376` n `780`
- 24h: commodity avg `-0.1221` n `12`; crypto_alt avg `-0.6572` n `230`; crypto_major avg `-1.7318` n `8`; equity avg `0.2489` n `102`; fx avg `0.1108` n `6`; index avg `0.2565` n `25`; metal avg `-0.2963` n `20`; unknown avg `1.1909` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
