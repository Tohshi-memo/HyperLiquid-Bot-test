# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T08:22:27.847115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `0.206` n `231`; crypto_major avg `0.0739` n `8`; equity avg `0.0793` n `127`; fx avg `-0.0098` n `6`; index avg `0.0055` n `26`; metal avg `-0.018` n `20`; unknown avg `0.0066` n `792`
- 1h: commodity avg `0.1227` n `12`; crypto_alt avg `0.9317` n `231`; crypto_major avg `0.9855` n `8`; equity avg `0.4358` n `127`; fx avg `-0.022` n `6`; index avg `0.0393` n `26`; metal avg `0.0044` n `20`; unknown avg `0.1064` n `791`
- 4h: commodity avg `-0.1201` n `12`; crypto_alt avg `1.0269` n `231`; crypto_major avg `1.1885` n `8`; equity avg `0.5185` n `127`; fx avg `-0.0206` n `6`; index avg `0.0169` n `26`; metal avg `-0.201` n `20`; unknown avg `0.2462` n `775`
- 24h: commodity avg `0.2997` n `12`; crypto_alt avg `1.2662` n `231`; crypto_major avg `1.5613` n `8`; equity avg `2.1069` n `127`; fx avg `-0.1041` n `6`; index avg `0.3221` n `26`; metal avg `-0.3289` n `20`; unknown avg `0.4704` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
