# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T01:52:26.362795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.3879` n `231`; crypto_major avg `-0.2896` n `8`; equity avg `-0.031` n `127`; fx avg `0.0034` n `6`; index avg `-0.003` n `26`; metal avg `-0.0672` n `20`; unknown avg `0.1578` n `792`
- 1h: commodity avg `-0.0597` n `12`; crypto_alt avg `0.0767` n `231`; crypto_major avg `0.0785` n `8`; equity avg `0.0015` n `127`; fx avg `-0.0252` n `6`; index avg `-0.0262` n `26`; metal avg `-0.0789` n `20`; unknown avg `-0.0521` n `792`
- 4h: commodity avg `-0.0696` n `12`; crypto_alt avg `0.6098` n `231`; crypto_major avg `0.3426` n `8`; equity avg `0.1659` n `127`; fx avg `-0.0408` n `6`; index avg `0.0266` n `26`; metal avg `-0.1599` n `20`; unknown avg `-0.0996` n `792`
- 24h: commodity avg `0.2874` n `12`; crypto_alt avg `1.597` n `231`; crypto_major avg `2.1849` n `8`; equity avg `0.234` n `127`; fx avg `-0.004` n `6`; index avg `0.0434` n `26`; metal avg `-0.2403` n `20`; unknown avg `0.8635` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
