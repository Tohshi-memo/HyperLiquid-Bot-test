# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T05:22:26.478983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.0838` n `230`; crypto_major avg `0.2753` n `8`; equity avg `0.2983` n `94`; fx avg `0.0071` n `6`; index avg `0.089` n `25`; metal avg `0.0086` n `20`; unknown avg `1.1466` n `768`
- 1h: commodity avg `-0.0359` n `12`; crypto_alt avg `0.2139` n `230`; crypto_major avg `0.3473` n `8`; equity avg `0.3254` n `94`; fx avg `-0.0189` n `6`; index avg `0.0817` n `25`; metal avg `-0.0132` n `20`; unknown avg `1.0377` n `768`
- 4h: commodity avg `-0.1207` n `12`; crypto_alt avg `0.5443` n `230`; crypto_major avg `0.6381` n `8`; equity avg `0.6155` n `94`; fx avg `-0.0507` n `6`; index avg `0.1586` n `25`; metal avg `0.0451` n `20`; unknown avg `-0.2782` n `768`
- 24h: commodity avg `-0.0869` n `12`; crypto_alt avg `0.5835` n `230`; crypto_major avg `0.6215` n `8`; equity avg `-1.8812` n `93`; fx avg `0.1097` n `6`; index avg `-0.3641` n `25`; metal avg `0.0832` n `20`; unknown avg `-0.186` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
