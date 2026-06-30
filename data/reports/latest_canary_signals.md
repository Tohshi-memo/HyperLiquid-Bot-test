# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T01:52:25.900816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3773` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0962` n `228`; crypto_major avg `-0.1811` n `8`; equity avg `0.0986` n `88`; fx avg `-0.0017` n `6`; index avg `0.0038` n `23`; metal avg `-0.1193` n `20`; unknown avg `-0.0036` n `765`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `-0.1726` n `228`; crypto_major avg `-0.1495` n `8`; equity avg `0.193` n `88`; fx avg `-0.0009` n `6`; index avg `0.0744` n `23`; metal avg `-0.2449` n `20`; unknown avg `0.1654` n `765`
- 4h: commodity avg `-0.0405` n `12`; crypto_alt avg `-1.1367` n `228`; crypto_major avg `-1.4338` n `8`; equity avg `-0.2222` n `88`; fx avg `0.053` n `6`; index avg `-0.0565` n `23`; metal avg `-0.52` n `20`; unknown avg `0.8013` n `763`
- 24h: commodity avg `-0.2389` n `12`; crypto_alt avg `0.37` n `228`; crypto_major avg `1.5576` n `8`; equity avg `1.8744` n `88`; fx avg `0.1962` n `6`; index avg `0.2027` n `23`; metal avg `-0.6845` n `20`; unknown avg `2.2577` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
