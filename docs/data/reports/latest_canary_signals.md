# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T03:52:32.163062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.0614` n `233`; crypto_major avg `0.005` n `8`; equity avg `-0.1892` n `134`; fx avg `-0.0069` n `6`; index avg `-0.0388` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.1249` n `797`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.4423` n `233`; crypto_major avg `-0.4257` n `8`; equity avg `-0.4327` n `134`; fx avg `-0.0301` n `6`; index avg `-0.0614` n `26`; metal avg `-0.0645` n `20`; unknown avg `0.6294` n `795`
- 4h: commodity avg `-0.102` n `12`; crypto_alt avg `-0.642` n `233`; crypto_major avg `-0.1342` n `8`; equity avg `0.3196` n `134`; fx avg `-0.0177` n `6`; index avg `0.0927` n `26`; metal avg `0.1409` n `20`; unknown avg `-0.0011` n `785`
- 24h: commodity avg `0.0349` n `12`; crypto_alt avg `-1.0202` n `232`; crypto_major avg `0.3111` n `8`; equity avg `-0.0382` n `134`; fx avg `0.0339` n `6`; index avg `-0.2348` n `26`; metal avg `-0.3986` n `20`; unknown avg `0.8196` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
