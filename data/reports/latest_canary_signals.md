# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T16:22:26.291975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0897` n `12`; crypto_alt avg `0.0029` n `230`; crypto_major avg `0.0465` n `8`; equity avg `-0.0337` n `102`; fx avg `0.0032` n `6`; index avg `-0.0028` n `25`; metal avg `0.0074` n `20`; unknown avg `0.0123` n `782`
- 1h: commodity avg `-0.047` n `12`; crypto_alt avg `-0.0929` n `230`; crypto_major avg `-0.0572` n `8`; equity avg `-0.0315` n `102`; fx avg `-0.0039` n `6`; index avg `0.0089` n `25`; metal avg `0.0106` n `20`; unknown avg `-0.1047` n `782`
- 4h: commodity avg `-0.0967` n `12`; crypto_alt avg `-0.1106` n `230`; crypto_major avg `0.0633` n `8`; equity avg `0.0485` n `102`; fx avg `-0.0546` n `6`; index avg `0.0261` n `25`; metal avg `0.0494` n `20`; unknown avg `1.0751` n `782`
- 24h: commodity avg `-1.2449` n `12`; crypto_alt avg `0.0726` n `230`; crypto_major avg `0.1292` n `8`; equity avg `0.959` n `102`; fx avg `-0.1511` n `6`; index avg `0.2428` n `25`; metal avg `0.2707` n `20`; unknown avg `1.4446` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
