# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T21:07:34.260556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3769` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2902` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1014` n `12`; crypto_alt avg `-0.9384` n `228`; crypto_major avg `-0.7679` n `8`; equity avg `-0.1301` n `78`; fx avg `-0.047` n `6`; index avg `0.0055` n `23`; metal avg `-0.0241` n `18`; unknown avg `-0.3805` n `702`
- 1h: commodity avg `-0.1142` n `12`; crypto_alt avg `-1.5528` n `228`; crypto_major avg `-1.4` n `8`; equity avg `-0.264` n `78`; fx avg `-0.0632` n `6`; index avg `-0.0231` n `23`; metal avg `-0.053` n `18`; unknown avg `0.4211` n `702`
- 4h: commodity avg `-0.0295` n `12`; crypto_alt avg `-1.7554` n `228`; crypto_major avg `-1.3058` n `8`; equity avg `-0.3088` n `78`; fx avg `-0.1146` n `6`; index avg `-0.0156` n `23`; metal avg `-0.1274` n `18`; unknown avg `0.8059` n `694`
- 24h: commodity avg `0.1651` n `12`; crypto_alt avg `0.0285` n `228`; crypto_major avg `-1.0145` n `8`; equity avg `-0.0128` n `78`; fx avg `-0.1793` n `6`; index avg `0.0197` n `23`; metal avg `-0.1619` n `18`; unknown avg `0.7993` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
