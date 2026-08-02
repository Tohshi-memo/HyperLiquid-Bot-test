# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T16:37:30.165893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0987` n `230`; crypto_major avg `0.2797` n `8`; equity avg `0.0749` n `102`; fx avg `-0.0002` n `6`; index avg `0.0118` n `25`; metal avg `0.0138` n `20`; unknown avg `0.145` n `782`
- 1h: commodity avg `-0.1093` n `12`; crypto_alt avg `-0.0352` n `230`; crypto_major avg `0.1479` n `8`; equity avg `0.0662` n `102`; fx avg `-0.007` n `6`; index avg `0.0256` n `25`; metal avg `0.0207` n `20`; unknown avg `0.0548` n `782`
- 4h: commodity avg `-0.1885` n `12`; crypto_alt avg `0.0202` n `230`; crypto_major avg `0.3523` n `8`; equity avg `0.1154` n `102`; fx avg `-0.0612` n `6`; index avg `0.0387` n `25`; metal avg `0.044` n `20`; unknown avg `1.1864` n `782`
- 24h: commodity avg `-1.2712` n `12`; crypto_alt avg `0.1033` n `230`; crypto_major avg `0.2938` n `8`; equity avg `1.0417` n `102`; fx avg `-0.1506` n `6`; index avg `0.2494` n `25`; metal avg `0.2795` n `20`; unknown avg `1.4531` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
