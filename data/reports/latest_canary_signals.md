# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T21:37:31.522912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0932` n `12`; crypto_alt avg `0.1309` n `230`; crypto_major avg `0.0713` n `8`; equity avg `0.0848` n `102`; fx avg `0.0124` n `6`; index avg `0.0225` n `25`; metal avg `0.0337` n `20`; unknown avg `0.0683` n `782`
- 1h: commodity avg `-0.1175` n `12`; crypto_alt avg `0.3912` n `230`; crypto_major avg `0.3125` n `8`; equity avg `0.1925` n `102`; fx avg `0.0439` n `6`; index avg `0.0269` n `25`; metal avg `0.0683` n `20`; unknown avg `0.1952` n `782`
- 4h: commodity avg `-0.1245` n `12`; crypto_alt avg `-0.2222` n `230`; crypto_major avg `-0.1878` n `8`; equity avg `-0.0549` n `102`; fx avg `0.0211` n `6`; index avg `-0.0093` n `25`; metal avg `0.0734` n `20`; unknown avg `0.0053` n `782`
- 24h: commodity avg `-0.2081` n `12`; crypto_alt avg `-0.31` n `230`; crypto_major avg `-0.8971` n `8`; equity avg `-0.3406` n `102`; fx avg `-0.0387` n `6`; index avg `-0.008` n `25`; metal avg `0.0771` n `20`; unknown avg `4.4505` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
