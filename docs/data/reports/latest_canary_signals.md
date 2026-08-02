# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T02:07:28.243614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3745` n `12`; crypto_alt avg `0.459` n `230`; crypto_major avg `0.61` n `8`; equity avg `0.2759` n `102`; fx avg `-0.0016` n `6`; index avg `0.0263` n `25`; metal avg `0.0066` n `20`; unknown avg `1.0358` n `782`
- 1h: commodity avg `-0.4534` n `12`; crypto_alt avg `0.5839` n `230`; crypto_major avg `0.7341` n `8`; equity avg `0.2152` n `102`; fx avg `-0.0135` n `6`; index avg `0.0361` n `25`; metal avg `0.0014` n `20`; unknown avg `1.5807` n `782`
- 4h: commodity avg `-0.5564` n `12`; crypto_alt avg `0.922` n `230`; crypto_major avg `1.0519` n `8`; equity avg `0.3966` n `102`; fx avg `-0.0351` n `6`; index avg `0.076` n `25`; metal avg `0.0313` n `20`; unknown avg `1.5248` n `782`
- 24h: commodity avg `-0.6651` n `12`; crypto_alt avg `-0.0025` n `230`; crypto_major avg `0.0929` n `8`; equity avg `0.2907` n `102`; fx avg `-0.0337` n `6`; index avg `0.0523` n `25`; metal avg `0.1012` n `20`; unknown avg `-0.0312` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
