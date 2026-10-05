# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T04:52:27.862066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `13`; crypto_alt avg `0.1474` n `235`; crypto_major avg `0.0483` n `8`; equity avg `0.003` n `144`; fx avg `0.01` n `6`; index avg `-0.0051` n `26`; metal avg `0.0057` n `20`; unknown avg `0.9544` n `1077`
- 1h: commodity avg `0.0528` n `13`; crypto_alt avg `-0.5555` n `235`; crypto_major avg `-0.3887` n `8`; equity avg `-0.1679` n `144`; fx avg `0.0508` n `6`; index avg `-0.0373` n `26`; metal avg `-0.0888` n `20`; unknown avg `2.1869` n `1049`
- 4h: commodity avg `-0.0527` n `13`; crypto_alt avg `-0.8447` n `235`; crypto_major avg `-0.7224` n `8`; equity avg `-0.298` n `144`; fx avg `-0.0918` n `6`; index avg `-0.0897` n `26`; metal avg `-0.1581` n `20`; unknown avg `1.8249` n `980`
- 24h: commodity avg `-0.2687` n `13`; crypto_alt avg `0.0297` n `235`; crypto_major avg `0.7829` n `8`; equity avg `0.1969` n `144`; fx avg `-0.0724` n `6`; index avg `-0.0561` n `26`; metal avg `0.022` n `20`; unknown avg `0.2139` n `904`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
