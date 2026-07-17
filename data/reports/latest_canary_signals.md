# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T12:18:55.574409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0614` n `12`; crypto_alt avg `-0.0853` n `230`; crypto_major avg `-0.1264` n `8`; equity avg `-0.0793` n `96`; fx avg `-0.0029` n `6`; index avg `-0.0066` n `25`; metal avg `0.046` n `20`; unknown avg `-0.003` n `769`
- 1h: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.0915` n `230`; crypto_major avg `-0.1066` n `8`; equity avg `-0.3153` n `96`; fx avg `-0.013` n `6`; index avg `-0.0337` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.1186` n `769`
- 4h: commodity avg `0.2616` n `12`; crypto_alt avg `0.3417` n `230`; crypto_major avg `0.3533` n `8`; equity avg `0.811` n `96`; fx avg `-0.017` n `6`; index avg `0.1052` n `25`; metal avg `0.0224` n `20`; unknown avg `0.1759` n `768`
- 24h: commodity avg `-0.196` n `12`; crypto_alt avg `-1.5304` n `230`; crypto_major avg `-2.6636` n `8`; equity avg `-4.5603` n `94`; fx avg `-0.0569` n `6`; index avg `-0.5603` n `25`; metal avg `-0.6389` n `20`; unknown avg `-0.403` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
