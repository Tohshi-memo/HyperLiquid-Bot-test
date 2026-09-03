# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T05:52:34.365694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.2124` n `232`; crypto_major avg `0.212` n `8`; equity avg `0.2056` n `133`; fx avg `-0.0069` n `6`; index avg `0.0624` n `26`; metal avg `0.0645` n `20`; unknown avg `15.7335` n `792`
- 1h: commodity avg `-0.14` n `12`; crypto_alt avg `-0.1117` n `232`; crypto_major avg `-0.0996` n `8`; equity avg `-0.3996` n `133`; fx avg `0.0004` n `6`; index avg `-0.0793` n `26`; metal avg `-0.0469` n `20`; unknown avg `3.6348` n `790`
- 4h: commodity avg `-0.2498` n `12`; crypto_alt avg `0.629` n `232`; crypto_major avg `0.51` n `8`; equity avg `-0.1402` n `133`; fx avg `-0.0577` n `6`; index avg `-0.0464` n `26`; metal avg `0.0955` n `20`; unknown avg `1.5292` n `790`
- 24h: commodity avg `0.0018` n `12`; crypto_alt avg `0.1118` n `232`; crypto_major avg `0.0458` n `8`; equity avg `0.9686` n `133`; fx avg `-0.3307` n `6`; index avg `0.0913` n `26`; metal avg `0.7179` n `20`; unknown avg `-0.5147` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
