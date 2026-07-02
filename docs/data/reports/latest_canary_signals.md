# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T20:52:28.531047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.79` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0881` n `229`; crypto_major avg `0.1178` n `8`; equity avg `-0.0111` n `88`; fx avg `0.0016` n `6`; index avg `-0.0092` n `25`; metal avg `-0.027` n `20`; unknown avg `-0.2289` n `765`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `-0.0054` n `229`; crypto_major avg `-0.1131` n `8`; equity avg `0.0959` n `88`; fx avg `0.0317` n `6`; index avg `-0.0288` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.4556` n `765`
- 4h: commodity avg `0.0899` n `12`; crypto_alt avg `-0.0701` n `229`; crypto_major avg `-0.1822` n `8`; equity avg `0.1157` n `88`; fx avg `0.0102` n `6`; index avg `0.0593` n `25`; metal avg `-0.0254` n `20`; unknown avg `1.1942` n `763`
- 24h: commodity avg `0.1005` n `12`; crypto_alt avg `2.1016` n `228`; crypto_major avg `2.9922` n `8`; equity avg `-2.2067` n `88`; fx avg `-0.086` n `6`; index avg `-0.4501` n `25`; metal avg `0.9604` n `20`; unknown avg `1.9923` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
