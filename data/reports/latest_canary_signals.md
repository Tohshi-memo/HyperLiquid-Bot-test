# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T23:39:55.275938+00:00`
- Correlation status: `ready`
- Asset price records: `594`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.132` n `12`; crypto_alt avg `0.1793` n `228`; crypto_major avg `0.0546` n `8`; equity avg `0.0257` n `65`; fx avg `-0.0106` n `5`; index avg `-0.0105` n `23`; metal avg `0.0102` n `18`; unknown avg `-0.1301` n `365`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `0.5424` n `228`; crypto_major avg `0.2393` n `8`; equity avg `0.4951` n `65`; fx avg `-0.0215` n `5`; index avg `0.1315` n `23`; metal avg `0.2202` n `18`; unknown avg `-0.0631` n `365`
- 4h: commodity avg `0.5091` n `12`; crypto_alt avg `0.1625` n `228`; crypto_major avg `-0.1848` n `8`; equity avg `-0.068` n `65`; fx avg `-0.0477` n `5`; index avg `0.0007` n `23`; metal avg `-0.3119` n `18`; unknown avg `-0.1686` n `365`
- 24h: commodity avg `0.8567` n `12`; crypto_alt avg `1.5284` n `228`; crypto_major avg `-1.7871` n `8`; equity avg `-1.4758` n `65`; fx avg `0.1308` n `5`; index avg `-0.8085` n `23`; metal avg `-0.1034` n `18`; unknown avg `-0.4382` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.139`, n `590`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `590`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `590`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `590`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `586`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `586`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0862`, n `586`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0836`, n `586`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `586`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0751`, n `586`, weak_sample_signal
