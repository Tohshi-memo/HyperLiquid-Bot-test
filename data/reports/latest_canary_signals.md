# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T13:22:27.522371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0515` n `12`; crypto_alt avg `-0.0538` n `230`; crypto_major avg `-0.0354` n `8`; equity avg `-0.1978` n `108`; fx avg `0.004` n `6`; index avg `-0.0297` n `25`; metal avg `0.04` n `20`; unknown avg `-0.0335` n `782`
- 1h: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.2575` n `230`; crypto_major avg `-0.3025` n `8`; equity avg `-0.1863` n `108`; fx avg `0.0093` n `6`; index avg `0.0008` n `25`; metal avg `-0.2229` n `20`; unknown avg `-0.0317` n `782`
- 4h: commodity avg `-0.1078` n `12`; crypto_alt avg `-0.1524` n `230`; crypto_major avg `-0.238` n `8`; equity avg `-0.0733` n `108`; fx avg `0.0081` n `6`; index avg `0.0611` n `25`; metal avg `0.0714` n `20`; unknown avg `-0.0767` n `781`
- 24h: commodity avg `-0.14` n `12`; crypto_alt avg `0.6909` n `230`; crypto_major avg `0.3336` n `8`; equity avg `1.5298` n `108`; fx avg `0.0671` n `6`; index avg `0.4759` n `25`; metal avg `0.6714` n `20`; unknown avg `0.0056` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
