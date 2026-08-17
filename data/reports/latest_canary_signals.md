# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T22:07:29.039815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0559` n `12`; crypto_alt avg `-0.068` n `230`; crypto_major avg `-0.051` n `8`; equity avg `0.1114` n `114`; fx avg `0.0266` n `6`; index avg `0.0072` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0094` n `792`
- 1h: commodity avg `0.063` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `-0.0101` n `8`; equity avg `0.1603` n `114`; fx avg `0.019` n `6`; index avg `0.0262` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.0433` n `792`
- 4h: commodity avg `0.1769` n `12`; crypto_alt avg `-0.0428` n `230`; crypto_major avg `-0.0569` n `8`; equity avg `-0.0976` n `114`; fx avg `0.0092` n `6`; index avg `-0.0318` n `25`; metal avg `-0.0382` n `20`; unknown avg `-0.0987` n `792`
- 24h: commodity avg `0.5366` n `12`; crypto_alt avg `0.847` n `230`; crypto_major avg `1.3855` n `8`; equity avg `1.2488` n `114`; fx avg `0.0584` n `6`; index avg `0.0678` n `25`; metal avg `0.2657` n `20`; unknown avg `0.3041` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
