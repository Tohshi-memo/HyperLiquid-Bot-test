# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T00:07:31.770519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1534` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.3464` n `228`; crypto_major avg `0.2608` n `8`; equity avg `-0.0167` n `78`; fx avg `0.0075` n `6`; index avg `0.0425` n `23`; metal avg `0.136` n `18`; unknown avg `0.4729` n `702`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0152` n `228`; crypto_major avg `-0.0919` n `8`; equity avg `-0.4946` n `78`; fx avg `0.0258` n `6`; index avg `-0.0233` n `23`; metal avg `-0.1368` n `18`; unknown avg `1.9967` n `702`
- 4h: commodity avg `-0.1265` n `12`; crypto_alt avg `-1.4159` n `228`; crypto_major avg `-1.311` n `8`; equity avg `-0.9159` n `78`; fx avg `0.0223` n `6`; index avg `-0.1576` n `23`; metal avg `-0.0793` n `18`; unknown avg `0.6585` n `702`
- 24h: commodity avg `0.1291` n `12`; crypto_alt avg `-0.5391` n `228`; crypto_major avg `-1.4667` n `8`; equity avg `-0.76` n `78`; fx avg `0.0278` n `6`; index avg `-0.1355` n `23`; metal avg `-0.1802` n `18`; unknown avg `1.0305` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
