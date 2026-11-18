# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T12:37:28.822772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0858` n `13`; crypto_alt avg `-0.2042` n `239`; crypto_major avg `-0.3736` n `8`; equity avg `-0.4096` n `163`; fx avg `0.0023` n `6`; index avg `-0.0555` n `27`; metal avg `-0.1663` n `20`; unknown avg `0.0925` n `1266`
- 1h: commodity avg `0.1775` n `13`; crypto_alt avg `-0.1708` n `239`; crypto_major avg `-0.2327` n `8`; equity avg `-0.4511` n `163`; fx avg `-0.0045` n `6`; index avg `-0.065` n `27`; metal avg `-0.1108` n `20`; unknown avg `-0.0025` n `1258`
- 4h: commodity avg `0.3377` n `13`; crypto_alt avg `-0.1152` n `239`; crypto_major avg `-0.734` n `8`; equity avg `-0.4998` n `163`; fx avg `0.022` n `6`; index avg `-0.0603` n `27`; metal avg `-0.0931` n `20`; unknown avg `135.2326` n `1218`
- 24h: commodity avg `-0.0073` n `13`; crypto_alt avg `-0.3596` n `239`; crypto_major avg `-0.2968` n `8`; equity avg `-0.7475` n `163`; fx avg `-0.1167` n `6`; index avg `-0.0697` n `27`; metal avg `-1.172` n `20`; unknown avg `7.0409` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
