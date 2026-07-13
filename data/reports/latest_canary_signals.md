# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T15:22:27.608077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0546` n `12`; crypto_alt avg `-0.0348` n `230`; crypto_major avg `0.0955` n `8`; equity avg `0.0572` n `92`; fx avg `-0.0018` n `6`; index avg `-0.007` n `25`; metal avg `0.0332` n `20`; unknown avg `-0.0268` n `766`
- 1h: commodity avg `0.0267` n `12`; crypto_alt avg `0.4281` n `230`; crypto_major avg `0.5586` n `8`; equity avg `0.7093` n `92`; fx avg `-0.0132` n `6`; index avg `0.0901` n `25`; metal avg `0.0759` n `20`; unknown avg `0.0497` n `766`
- 4h: commodity avg `0.2129` n `12`; crypto_alt avg `-0.0168` n `230`; crypto_major avg `-0.2083` n `8`; equity avg `-0.0488` n `92`; fx avg `-0.0235` n `6`; index avg `0.0358` n `25`; metal avg `-0.0967` n `20`; unknown avg `-0.0588` n `766`
- 24h: commodity avg `0.1152` n `12`; crypto_alt avg `-1.1991` n `230`; crypto_major avg `-1.9662` n `8`; equity avg `-2.0086` n `92`; fx avg `-0.088` n `6`; index avg `-0.4115` n `25`; metal avg `-0.3504` n `20`; unknown avg `-0.1285` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
