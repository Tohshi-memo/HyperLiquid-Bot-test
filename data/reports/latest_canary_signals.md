# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T12:07:23.319109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.74` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `-0.0468` n `228`; crypto_major avg `-0.0812` n `8`; equity avg `-0.0423` n `66`; fx avg `-0.0172` n `6`; index avg `-0.0519` n `23`; metal avg `0.0718` n `18`; unknown avg `0.0013` n `386`
- 1h: commodity avg `-0.1364` n `12`; crypto_alt avg `-0.0154` n `228`; crypto_major avg `-0.1198` n `8`; equity avg `0.2781` n `66`; fx avg `-0.0269` n `6`; index avg `0.1262` n `23`; metal avg `0.1008` n `18`; unknown avg `-0.0332` n `386`
- 4h: commodity avg `0.5091` n `12`; crypto_alt avg `-1.1665` n `228`; crypto_major avg `-1.2187` n `8`; equity avg `-0.2875` n `66`; fx avg `0.0231` n `6`; index avg `-0.2536` n `23`; metal avg `-0.0417` n `18`; unknown avg `0.752` n `386`
- 24h: commodity avg `-1.188` n `12`; crypto_alt avg `1.6228` n `228`; crypto_major avg `1.9459` n `8`; equity avg `1.0872` n `66`; fx avg `0.0405` n `6`; index avg `0.8991` n `23`; metal avg `-0.1669` n `18`; unknown avg `6.5665` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
