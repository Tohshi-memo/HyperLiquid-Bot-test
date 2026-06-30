# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T21:07:29.513266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0438` n `228`; crypto_major avg `0.0041` n `8`; equity avg `0.05` n `88`; fx avg `-0.0023` n `6`; index avg `0.0104` n `23`; metal avg `-0.0228` n `20`; unknown avg `-0.0735` n `765`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.4186` n `228`; crypto_major avg `-0.3624` n `8`; equity avg `0.0343` n `88`; fx avg `-0.0203` n `6`; index avg `-0.0403` n `23`; metal avg `-0.1924` n `20`; unknown avg `-0.2066` n `765`
- 4h: commodity avg `-0.0752` n `12`; crypto_alt avg `-0.5326` n `228`; crypto_major avg `0.0006` n `8`; equity avg `0.3195` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0543` n `23`; metal avg `-0.1813` n `20`; unknown avg `1.045` n `763`
- 24h: commodity avg `0.1355` n `12`; crypto_alt avg `-2.229` n `228`; crypto_major avg `-2.0867` n `8`; equity avg `1.2157` n `88`; fx avg `0.1333` n `6`; index avg `0.2145` n `23`; metal avg `-0.0616` n `20`; unknown avg `8.179` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
