# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T07:20:19.643380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `-0.1347` n `230`; crypto_major avg `-0.1433` n `8`; equity avg `0.0126` n `107`; fx avg `0.0027` n `6`; index avg `0.0019` n `25`; metal avg `0.0338` n `20`; unknown avg `0.3615` n `781`
- 1h: commodity avg `-0.1302` n `12`; crypto_alt avg `-0.5729` n `230`; crypto_major avg `-0.3747` n `8`; equity avg `0.1019` n `107`; fx avg `0.0124` n `6`; index avg `-0.0073` n `25`; metal avg `0.0591` n `20`; unknown avg `0.3866` n `781`
- 4h: commodity avg `-0.0936` n `12`; crypto_alt avg `-0.3855` n `230`; crypto_major avg `-0.1851` n `8`; equity avg `1.0195` n `107`; fx avg `0.0523` n `6`; index avg `0.1681` n `25`; metal avg `0.1212` n `20`; unknown avg `0.3799` n `765`
- 24h: commodity avg `0.1923` n `12`; crypto_alt avg `0.874` n `230`; crypto_major avg `1.165` n `8`; equity avg `2.7275` n `107`; fx avg `0.0606` n `6`; index avg `0.2905` n `25`; metal avg `0.2151` n `20`; unknown avg `0.5898` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
