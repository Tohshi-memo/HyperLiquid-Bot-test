# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T01:37:24.193621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0545` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `0.0932` n `8`; equity avg `-0.0015` n `102`; fx avg `0.0053` n `6`; index avg `0.0203` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0329` n `782`
- 1h: commodity avg `-0.1542` n `12`; crypto_alt avg `0.5007` n `230`; crypto_major avg `0.4873` n `8`; equity avg `-0.0109` n `102`; fx avg `0.0136` n `6`; index avg `0.013` n `25`; metal avg `0.0332` n `20`; unknown avg `3.2661` n `782`
- 4h: commodity avg `-0.341` n `12`; crypto_alt avg `0.5283` n `230`; crypto_major avg `0.6068` n `8`; equity avg `0.3963` n `102`; fx avg `-0.0193` n `6`; index avg `0.0719` n `25`; metal avg `0.0159` n `20`; unknown avg `0.6388` n `782`
- 24h: commodity avg `-0.3154` n `12`; crypto_alt avg `-0.4675` n `230`; crypto_major avg `-0.4495` n `8`; equity avg `0.1783` n `102`; fx avg `-0.0356` n `6`; index avg `0.0555` n `25`; metal avg `0.0994` n `20`; unknown avg `-0.0229` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
