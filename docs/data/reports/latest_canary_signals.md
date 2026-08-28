# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T15:37:28.373520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.1687` n `231`; crypto_major avg `-0.2957` n `8`; equity avg `-0.133` n `127`; fx avg `0.0101` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0299` n `20`; unknown avg `0.0035` n `793`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `-0.4281` n `231`; crypto_major avg `-0.6239` n `8`; equity avg `-0.391` n `127`; fx avg `0.025` n `6`; index avg `-0.009` n `26`; metal avg `-0.0447` n `20`; unknown avg `-0.0177` n `793`
- 4h: commodity avg `0.0133` n `12`; crypto_alt avg `-0.1597` n `231`; crypto_major avg `-0.0899` n `8`; equity avg `-0.3968` n `127`; fx avg `-0.0238` n `6`; index avg `0.0724` n `26`; metal avg `-0.0593` n `20`; unknown avg `-0.0882` n `792`
- 24h: commodity avg `0.0051` n `12`; crypto_alt avg `-1.4567` n `231`; crypto_major avg `-1.5414` n `8`; equity avg `-0.7232` n `127`; fx avg `-0.0637` n `6`; index avg `0.1122` n `26`; metal avg `0.5453` n `20`; unknown avg `0.2024` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
