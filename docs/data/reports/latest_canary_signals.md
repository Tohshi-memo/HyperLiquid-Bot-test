# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T13:07:30.686679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0918` n `13`; crypto_alt avg `0.1097` n `234`; crypto_major avg `0.0694` n `8`; equity avg `0.1355` n `142`; fx avg `-0.0236` n `6`; index avg `0.0368` n `26`; metal avg `0.0285` n `20`; unknown avg `-0.1924` n `984`
- 1h: commodity avg `-0.0453` n `13`; crypto_alt avg `0.7161` n `234`; crypto_major avg `0.3395` n `8`; equity avg `0.7909` n `142`; fx avg `-0.0342` n `6`; index avg `0.2172` n `26`; metal avg `0.2155` n `20`; unknown avg `4.7278` n `983`
- 4h: commodity avg `0.0265` n `13`; crypto_alt avg `0.7047` n `234`; crypto_major avg `0.4742` n `8`; equity avg `0.4633` n `142`; fx avg `-0.0553` n `6`; index avg `0.1961` n `26`; metal avg `0.1574` n `20`; unknown avg `-0.2299` n `975`
- 24h: commodity avg `-0.5189` n `13`; crypto_alt avg `3.3306` n `234`; crypto_major avg `2.8308` n `8`; equity avg `1.839` n `142`; fx avg `-0.3543` n `6`; index avg `0.3992` n `26`; metal avg `0.1706` n `20`; unknown avg `0.5985` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
