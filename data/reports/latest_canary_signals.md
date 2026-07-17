# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T08:07:28.199899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0225` n `12`; crypto_alt avg `-0.0456` n `230`; crypto_major avg `-0.0069` n `8`; equity avg `0.1015` n `96`; fx avg `0.0158` n `6`; index avg `0.0178` n `25`; metal avg `0.0249` n `20`; unknown avg `0.0088` n `768`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `-0.3138` n `230`; crypto_major avg `-0.1937` n `8`; equity avg `-0.054` n `96`; fx avg `0.0268` n `6`; index avg `0.0096` n `25`; metal avg `0.0546` n `20`; unknown avg `0.0848` n `768`
- 4h: commodity avg `-0.0973` n `12`; crypto_alt avg `-0.7933` n `230`; crypto_major avg `-0.8677` n `8`; equity avg `-0.6626` n `96`; fx avg `0.0156` n `6`; index avg `-0.0845` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.1395` n `736`
- 24h: commodity avg `-0.1496` n `12`; crypto_alt avg `-1.9327` n `230`; crypto_major avg `-3.1669` n `8`; equity avg `-5.2161` n `94`; fx avg `-0.038` n `6`; index avg `-0.6753` n `25`; metal avg `-0.6887` n `20`; unknown avg `-0.5503` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
