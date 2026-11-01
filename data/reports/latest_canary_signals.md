# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T07:52:27.212974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `0.0145` n `238`; crypto_major avg `0.0487` n `8`; equity avg `-0.0166` n `156`; fx avg `0.0013` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.0107` n `1263`
- 1h: commodity avg `0.016` n `13`; crypto_alt avg `0.0687` n `238`; crypto_major avg `-0.1164` n `8`; equity avg `-0.022` n `156`; fx avg `0.0077` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0074` n `20`; unknown avg `0.6014` n `1257`
- 4h: commodity avg `-0.0147` n `13`; crypto_alt avg `0.2315` n `238`; crypto_major avg `0.1342` n `8`; equity avg `0.1527` n `156`; fx avg `0.0014` n `6`; index avg `0.0276` n `27`; metal avg `0.0153` n `20`; unknown avg `0.6419` n `1232`
- 24h: commodity avg `-0.0057` n `13`; crypto_alt avg `0.971` n `238`; crypto_major avg `0.4728` n `8`; equity avg `0.3549` n `156`; fx avg `-0.0072` n `6`; index avg `0.0107` n `27`; metal avg `0.0861` n `20`; unknown avg `2.8093` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
