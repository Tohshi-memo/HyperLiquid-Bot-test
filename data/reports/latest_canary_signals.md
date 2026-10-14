# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T23:22:26.869370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.0507` n `236`; crypto_major avg `0.0399` n `8`; equity avg `-0.2873` n `151`; fx avg `0.0078` n `6`; index avg `-0.0171` n `26`; metal avg `0.0256` n `20`; unknown avg `0.002` n `1136`
- 1h: commodity avg `-0.0607` n `13`; crypto_alt avg `0.139` n `236`; crypto_major avg `0.092` n `8`; equity avg `-0.4478` n `151`; fx avg `0.0615` n `6`; index avg `-0.0372` n `26`; metal avg `-0.0207` n `20`; unknown avg `-0.3728` n `1134`
- 4h: commodity avg `0.0419` n `13`; crypto_alt avg `0.3322` n `236`; crypto_major avg `-0.13` n `8`; equity avg `-1.5928` n `151`; fx avg `0.0414` n `6`; index avg `-0.1838` n `26`; metal avg `-0.0352` n `20`; unknown avg `0.7487` n `998`
- 24h: commodity avg `-0.1647` n `13`; crypto_alt avg `-2.0288` n `236`; crypto_major avg `-1.8871` n `8`; equity avg `-5.4173` n `151`; fx avg `-0.1075` n `6`; index avg `-0.6893` n `26`; metal avg `-0.7823` n `20`; unknown avg `1392.2742` n `890`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0891`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0876`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0572`, n `666`, weak_sample_signal
