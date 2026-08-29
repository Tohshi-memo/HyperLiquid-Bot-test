# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T14:22:28.968172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.1657` n `231`; crypto_major avg `0.1378` n `8`; equity avg `0.0113` n `127`; fx avg `-0.0007` n `6`; index avg `0.0041` n `26`; metal avg `0.0044` n `20`; unknown avg `0.0888` n `793`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.4038` n `231`; crypto_major avg `0.2395` n `8`; equity avg `0.0176` n `127`; fx avg `-0.0047` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.1186` n `793`
- 4h: commodity avg `0.0085` n `12`; crypto_alt avg `0.5835` n `231`; crypto_major avg `0.3054` n `8`; equity avg `-0.0216` n `127`; fx avg `-0.0103` n `6`; index avg `-0.0001` n `26`; metal avg `0.0079` n `20`; unknown avg `0.1098` n `761`
- 24h: commodity avg `0.1098` n `12`; crypto_alt avg `-0.9244` n `231`; crypto_major avg `-1.2332` n `8`; equity avg `-1.1651` n `127`; fx avg `-0.0465` n `6`; index avg `-0.1725` n `26`; metal avg `-0.5529` n `20`; unknown avg `-0.3159` n `743`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2038`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
