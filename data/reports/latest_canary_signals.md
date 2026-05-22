# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T07:37:16.599757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2341` n `12`; crypto_alt avg `0.0329` n `228`; crypto_major avg `0.1074` n `8`; equity avg `-0.0456` n `67`; fx avg `-0.0105` n `6`; index avg `-0.0428` n `23`; metal avg `-0.2133` n `18`; unknown avg `-0.0265` n `386`
- 1h: commodity avg `0.2396` n `12`; crypto_alt avg `0.3078` n `228`; crypto_major avg `0.1116` n `8`; equity avg `-0.1071` n `67`; fx avg `-0.0247` n `6`; index avg `-0.0187` n `23`; metal avg `-0.3132` n `18`; unknown avg `-0.1225` n `386`
- 4h: commodity avg `0.5315` n `12`; crypto_alt avg `0.1203` n `228`; crypto_major avg `-0.1346` n `8`; equity avg `0.0555` n `67`; fx avg `-0.0037` n `6`; index avg `0.0882` n `23`; metal avg `-0.2878` n `18`; unknown avg `-0.4029` n `376`
- 24h: commodity avg `-0.4483` n `12`; crypto_alt avg `1.7304` n `228`; crypto_major avg `0.1462` n `8`; equity avg `1.6913` n `66`; fx avg `0.1188` n `6`; index avg `0.8545` n `23`; metal avg `0.6727` n `18`; unknown avg `1.8009` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0405`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0369`, n `668`, weak_sample_signal
