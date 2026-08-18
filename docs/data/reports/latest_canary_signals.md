# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T12:22:27.376327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `-0.0124` n `230`; crypto_major avg `-0.0708` n `8`; equity avg `-0.139` n `114`; fx avg `-0.0` n `6`; index avg `-0.0027` n `25`; metal avg `0.0558` n `20`; unknown avg `0.0064` n `795`
- 1h: commodity avg `0.1057` n `12`; crypto_alt avg `-0.048` n `230`; crypto_major avg `-0.12` n `8`; equity avg `-0.1138` n `114`; fx avg `0.0067` n `6`; index avg `0.0021` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.0628` n `795`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `0.2894` n `230`; crypto_major avg `0.2711` n `8`; equity avg `0.0035` n `114`; fx avg `-0.0398` n `6`; index avg `0.0225` n `25`; metal avg `0.0986` n `20`; unknown avg `-0.0689` n `795`
- 24h: commodity avg `0.6724` n `12`; crypto_alt avg `-0.694` n `230`; crypto_major avg `0.2052` n `8`; equity avg `-2.3548` n `114`; fx avg `-0.044` n `6`; index avg `-0.4878` n `25`; metal avg `-0.1162` n `20`; unknown avg `-0.0877` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
