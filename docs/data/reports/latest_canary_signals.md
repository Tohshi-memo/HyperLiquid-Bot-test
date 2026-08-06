# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T03:22:32.377614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `0.1057` n `230`; crypto_major avg `0.0482` n `8`; equity avg `-0.0882` n `108`; fx avg `0.0035` n `6`; index avg `-0.0146` n `25`; metal avg `-0.1007` n `20`; unknown avg `0.0021` n `782`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.1577` n `230`; crypto_major avg `0.0094` n `8`; equity avg `-0.0268` n `108`; fx avg `0.0192` n `6`; index avg `-0.0018` n `25`; metal avg `-0.21` n `20`; unknown avg `-0.1305` n `782`
- 4h: commodity avg `0.1246` n `12`; crypto_alt avg `-0.2298` n `230`; crypto_major avg `-0.633` n `8`; equity avg `-0.3063` n `108`; fx avg `-0.0464` n `6`; index avg `-0.1648` n `25`; metal avg `0.0466` n `20`; unknown avg `-0.0685` n `782`
- 24h: commodity avg `0.1785` n `12`; crypto_alt avg `0.2086` n `230`; crypto_major avg `-0.0673` n `8`; equity avg `-1.7699` n `108`; fx avg `0.025` n `6`; index avg `-0.3265` n `25`; metal avg `0.5002` n `20`; unknown avg `0.9047` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
