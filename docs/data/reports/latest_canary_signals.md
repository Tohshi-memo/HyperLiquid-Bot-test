# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T05:22:35.600649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0143` n `230`; crypto_major avg `0.03` n `8`; equity avg `0.0018` n `96`; fx avg `-0.0006` n `6`; index avg `0.0186` n `25`; metal avg `0.003` n `20`; unknown avg `-0.4252` n `769`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `-0.0943` n `230`; crypto_major avg `-0.0194` n `8`; equity avg `-0.0266` n `96`; fx avg `0.0005` n `6`; index avg `0.024` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.4009` n `769`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.3347` n `230`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0348` n `96`; fx avg `-0.0248` n `6`; index avg `0.0876` n `25`; metal avg `-0.0077` n `20`; unknown avg `-0.229` n `769`
- 24h: commodity avg `0.6885` n `12`; crypto_alt avg `-0.5478` n `230`; crypto_major avg `0.1344` n `8`; equity avg `1.1917` n `96`; fx avg `0.0563` n `6`; index avg `0.1976` n `25`; metal avg `0.2917` n `20`; unknown avg `0.2525` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
