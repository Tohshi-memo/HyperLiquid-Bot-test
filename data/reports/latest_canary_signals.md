# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T01:52:27.477761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `0.2377` n `234`; crypto_major avg `0.1963` n `8`; equity avg `0.0807` n `141`; fx avg `-0.0031` n `6`; index avg `0.0119` n `26`; metal avg `0.0351` n `20`; unknown avg `1.0928` n `963`
- 1h: commodity avg `0.0699` n `12`; crypto_alt avg `-1.3707` n `234`; crypto_major avg `-0.7118` n `8`; equity avg `0.0231` n `141`; fx avg `-0.0135` n `6`; index avg `0.0317` n `26`; metal avg `0.0294` n `20`; unknown avg `1.3335` n `961`
- 4h: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.7084` n `234`; crypto_major avg `-0.6612` n `8`; equity avg `-0.2104` n `141`; fx avg `-0.0092` n `6`; index avg `-0.0291` n `26`; metal avg `0.0108` n `20`; unknown avg `1.0081` n `931`
- 24h: commodity avg `0.2061` n `12`; crypto_alt avg `-3.9332` n `234`; crypto_major avg `-1.8988` n `8`; equity avg `-2.2376` n `141`; fx avg `-0.0704` n `6`; index avg `-0.2005` n `26`; metal avg `-0.5881` n `20`; unknown avg `174.0393` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
