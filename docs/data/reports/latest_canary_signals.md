# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T11:07:24.664104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.0392` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `0.0081` n `102`; fx avg `0.0006` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.0108` n `781`
- 1h: commodity avg `-0.0281` n `12`; crypto_alt avg `0.0873` n `230`; crypto_major avg `0.0143` n `8`; equity avg `0.0183` n `102`; fx avg `-0.0416` n `6`; index avg `0.0111` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.007` n `781`
- 4h: commodity avg `0.0321` n `12`; crypto_alt avg `-0.368` n `230`; crypto_major avg `-0.3312` n `8`; equity avg `-0.0167` n `102`; fx avg `-0.0219` n `6`; index avg `0.0359` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0335` n `781`
- 24h: commodity avg `0.492` n `12`; crypto_alt avg `0.0665` n `230`; crypto_major avg `-1.4448` n `8`; equity avg `-2.9391` n `102`; fx avg `-0.1182` n `6`; index avg `-0.3032` n `25`; metal avg `-0.0465` n `20`; unknown avg `4.6104` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
