# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T11:01:05.270886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0111` n `230`; crypto_major avg `0.0076` n `8`; equity avg `-0.0495` n `96`; fx avg `0.0039` n `6`; index avg `0.0039` n `25`; metal avg `0.0138` n `20`; unknown avg `-0.0339` n `769`
- 1h: commodity avg `0.0182` n `12`; crypto_alt avg `-0.0912` n `230`; crypto_major avg `-0.027` n `8`; equity avg `0.3636` n `96`; fx avg `-0.0146` n `6`; index avg `0.0956` n `25`; metal avg `-0.0783` n `20`; unknown avg `-0.0614` n `769`
- 4h: commodity avg `0.2354` n `12`; crypto_alt avg `0.1057` n `230`; crypto_major avg `0.2624` n `8`; equity avg `0.801` n `96`; fx avg `0.0091` n `6`; index avg `0.1161` n `25`; metal avg `0.0142` n `20`; unknown avg `0.0493` n `768`
- 24h: commodity avg `0.0712` n `12`; crypto_alt avg `-1.3642` n `230`; crypto_major avg `-2.4434` n `8`; equity avg `-4.1659` n `94`; fx avg `-0.0203` n `6`; index avg `-0.5484` n `25`; metal avg `-0.6788` n `20`; unknown avg `-0.4106` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
