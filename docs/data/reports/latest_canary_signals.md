# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T14:07:21.866920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0923` n `12`; crypto_alt avg `0.0031` n `228`; crypto_major avg `0.0154` n `8`; equity avg `0.1612` n `66`; fx avg `0.0049` n `6`; index avg `0.0355` n `23`; metal avg `-0.2285` n `18`; unknown avg `0.1033` n `386`
- 1h: commodity avg `-0.1513` n `12`; crypto_alt avg `-0.0564` n `228`; crypto_major avg `0.072` n `8`; equity avg `0.4018` n `66`; fx avg `-0.0395` n `6`; index avg `0.2784` n `23`; metal avg `-0.0252` n `18`; unknown avg `0.4977` n `386`
- 4h: commodity avg `1.147` n `12`; crypto_alt avg `-0.2871` n `228`; crypto_major avg `-0.269` n `8`; equity avg `0.0109` n `66`; fx avg `-0.0566` n `6`; index avg `-0.0625` n `23`; metal avg `-0.4715` n `18`; unknown avg `1.2635` n `386`
- 24h: commodity avg `-1.1069` n `12`; crypto_alt avg `2.0356` n `228`; crypto_major avg `2.3054` n `8`; equity avg `1.8648` n `66`; fx avg `0.0089` n `6`; index avg `0.9454` n `23`; metal avg `0.2173` n `18`; unknown avg `6.5154` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
