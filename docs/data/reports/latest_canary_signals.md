# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T08:58:16.254473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0725` n `12`; crypto_alt avg `0.0213` n `230`; crypto_major avg `0.1513` n `8`; equity avg `0.1363` n `93`; fx avg `-0.0173` n `6`; index avg `0.0229` n `25`; metal avg `0.0503` n `20`; unknown avg `-0.019` n `767`
- 1h: commodity avg `-0.1716` n `12`; crypto_alt avg `0.0974` n `230`; crypto_major avg `0.2563` n `8`; equity avg `-0.1266` n `93`; fx avg `-0.0041` n `6`; index avg `-0.0245` n `25`; metal avg `0.1134` n `20`; unknown avg `0.0136` n `767`
- 4h: commodity avg `-0.0983` n `12`; crypto_alt avg `-0.1791` n `230`; crypto_major avg `-0.0369` n `8`; equity avg `-0.2697` n `93`; fx avg `-0.0203` n `6`; index avg `-0.0948` n `25`; metal avg `0.0521` n `20`; unknown avg `-0.0902` n `747`
- 24h: commodity avg `-0.2157` n `12`; crypto_alt avg `1.4856` n `230`; crypto_major avg `3.1337` n `8`; equity avg `1.202` n `92`; fx avg `0.0222` n `6`; index avg `0.4172` n `25`; metal avg `0.3711` n `20`; unknown avg `0.27` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
