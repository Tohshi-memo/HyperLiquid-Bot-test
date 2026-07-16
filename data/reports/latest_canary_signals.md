# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T06:52:33.143586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.157` n `230`; crypto_major avg `0.2368` n `8`; equity avg `0.0347` n `94`; fx avg `-0.029` n `6`; index avg `0.013` n `25`; metal avg `0.0683` n `20`; unknown avg `0.0449` n `768`
- 1h: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.1091` n `230`; crypto_major avg `-0.0928` n `8`; equity avg `-0.149` n `94`; fx avg `-0.0515` n `6`; index avg `0.0049` n `25`; metal avg `-0.0393` n `20`; unknown avg `0.0101` n `752`
- 4h: commodity avg `-0.126` n `12`; crypto_alt avg `-0.1625` n `230`; crypto_major avg `0.226` n `8`; equity avg `-0.2716` n `94`; fx avg `-0.0646` n `6`; index avg `-0.043` n `25`; metal avg `0.0194` n `20`; unknown avg `-0.1444` n `752`
- 24h: commodity avg `-0.1071` n `12`; crypto_alt avg `-0.0411` n `230`; crypto_major avg `0.0537` n `8`; equity avg `-2.4311` n `93`; fx avg `0.0724` n `6`; index avg `-0.4597` n `25`; metal avg `-0.011` n `20`; unknown avg `-0.148` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
