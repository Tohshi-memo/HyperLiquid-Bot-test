# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T19:52:30.751872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.073` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0144` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0678` n `12`; crypto_alt avg `-0.3313` n `228`; crypto_major avg `-0.4077` n `8`; equity avg `-0.0409` n `73`; fx avg `-0.0117` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0949` n `18`; unknown avg `-0.126` n `419`
- 1h: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.6409` n `228`; crypto_major avg `-0.9745` n `8`; equity avg `-0.1423` n `73`; fx avg `0.0635` n `6`; index avg `0.0399` n `23`; metal avg `-0.038` n `18`; unknown avg `-0.2843` n `419`
- 4h: commodity avg `0.0559` n `12`; crypto_alt avg `-1.0054` n `228`; crypto_major avg `-1.0272` n `8`; equity avg `-0.1724` n `73`; fx avg `0.007` n `6`; index avg `0.0458` n `23`; metal avg `-0.31` n `18`; unknown avg `-0.627` n `419`
- 24h: commodity avg `0.7961` n `12`; crypto_alt avg `0.6371` n `228`; crypto_major avg `-2.5155` n `8`; equity avg `-2.0274` n `72`; fx avg `0.0487` n `6`; index avg `-0.3257` n `23`; metal avg `-2.0338` n `18`; unknown avg `0.1813` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
