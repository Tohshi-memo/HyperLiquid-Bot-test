# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T07:52:31.701715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `13`; crypto_alt avg `-0.1364` n `234`; crypto_major avg `-0.1279` n `8`; equity avg `0.0509` n `142`; fx avg `-0.0154` n `6`; index avg `-0.0086` n `26`; metal avg `0.015` n `20`; unknown avg `8.1814` n `975`
- 1h: commodity avg `0.2624` n `13`; crypto_alt avg `-1.093` n `234`; crypto_major avg `-1.0256` n `8`; equity avg `-0.5862` n `142`; fx avg `0.0003` n `6`; index avg `-0.1574` n `26`; metal avg `-0.1952` n `20`; unknown avg `6.1714` n `973`
- 4h: commodity avg `0.8079` n `13`; crypto_alt avg `-0.9852` n `234`; crypto_major avg `-0.5594` n `8`; equity avg `-0.0838` n `142`; fx avg `-0.0169` n `6`; index avg `-0.077` n `26`; metal avg `-0.1726` n `20`; unknown avg `2.245` n `940`
- 24h: commodity avg `0.2509` n `13`; crypto_alt avg `0.185` n `234`; crypto_major avg `0.2921` n `8`; equity avg `0.1982` n `142`; fx avg `0.1805` n `6`; index avg `0.0309` n `26`; metal avg `-0.3965` n `20`; unknown avg `773.5126` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
