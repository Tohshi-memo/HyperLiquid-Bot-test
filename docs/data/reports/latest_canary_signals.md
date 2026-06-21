# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T23:37:27.135369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4349` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `-0.5604` n `228`; crypto_major avg `-0.5301` n `8`; equity avg `-0.2259` n `78`; fx avg `-0.0045` n `6`; index avg `-0.048` n `23`; metal avg `-0.1643` n `18`; unknown avg `0.9685` n `702`
- 1h: commodity avg `0.0817` n `12`; crypto_alt avg `-0.4315` n `228`; crypto_major avg `-0.3519` n `8`; equity avg `-0.4113` n `78`; fx avg `-0.009` n `6`; index avg `-0.0728` n `23`; metal avg `-0.0731` n `18`; unknown avg `0.7157` n `702`
- 4h: commodity avg `-0.1624` n `12`; crypto_alt avg `-1.8955` n `228`; crypto_major avg `-1.6029` n `8`; equity avg `-0.7478` n `78`; fx avg `-0.0571` n `6`; index avg `-0.168` n `23`; metal avg `-0.1506` n `18`; unknown avg `0.6974` n `702`
- 24h: commodity avg `0.1559` n `12`; crypto_alt avg `-1.0907` n `228`; crypto_major avg `-1.9492` n `8`; equity avg `-0.6129` n `78`; fx avg `-0.1309` n `6`; index avg `-0.1668` n `23`; metal avg `-0.2507` n `18`; unknown avg `0.6817` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
