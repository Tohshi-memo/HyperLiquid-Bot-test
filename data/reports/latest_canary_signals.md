# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T14:52:27.546876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `-0.318` n `231`; crypto_major avg `-0.3467` n `8`; equity avg `-0.2287` n `127`; fx avg `0.0132` n `6`; index avg `0.0153` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.0091` n `793`
- 1h: commodity avg `0.0627` n `12`; crypto_alt avg `0.4493` n `231`; crypto_major avg `0.3349` n `8`; equity avg `-0.0185` n `127`; fx avg `0.0005` n `6`; index avg `0.074` n `26`; metal avg `-0.2294` n `20`; unknown avg `0.0476` n `793`
- 4h: commodity avg `-0.162` n `12`; crypto_alt avg `0.2009` n `231`; crypto_major avg `0.3795` n `8`; equity avg `-0.2443` n `127`; fx avg `-0.0384` n `6`; index avg `0.1065` n `26`; metal avg `0.0388` n `20`; unknown avg `-0.1018` n `792`
- 24h: commodity avg `-0.0303` n `12`; crypto_alt avg `-1.0818` n `231`; crypto_major avg `-0.8867` n `8`; equity avg `-0.7387` n `127`; fx avg `-0.0761` n `6`; index avg `0.1086` n `26`; metal avg `0.6474` n `20`; unknown avg `0.2929` n `759`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
