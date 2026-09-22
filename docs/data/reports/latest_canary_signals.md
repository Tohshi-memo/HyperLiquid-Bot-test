# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T20:37:28.885001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.3271` n `234`; crypto_major avg `0.1376` n `8`; equity avg `0.0706` n `140`; fx avg `-0.0074` n `6`; index avg `0.0011` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.7298` n `944`
- 1h: commodity avg `0.1952` n `12`; crypto_alt avg `0.4173` n `234`; crypto_major avg `0.0546` n `8`; equity avg `-0.0339` n `140`; fx avg `-0.0367` n `6`; index avg `-0.0456` n `26`; metal avg `-0.1068` n `20`; unknown avg `2.579` n `906`
- 4h: commodity avg `-0.034` n `12`; crypto_alt avg `1.5025` n `234`; crypto_major avg `0.8188` n `8`; equity avg `0.5704` n `140`; fx avg `-0.0377` n `6`; index avg `0.083` n `26`; metal avg `0.3422` n `20`; unknown avg `2.1091` n `874`
- 24h: commodity avg `0.1846` n `12`; crypto_alt avg `2.1231` n `234`; crypto_major avg `0.3006` n `8`; equity avg `0.9551` n `140`; fx avg `-0.3012` n `6`; index avg `0.1286` n `26`; metal avg `0.2988` n `20`; unknown avg `0.9284` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
