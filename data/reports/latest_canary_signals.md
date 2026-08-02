# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T13:52:30.600337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `0.0565` n `230`; crypto_major avg `0.091` n `8`; equity avg `-0.0283` n `102`; fx avg `-0.0102` n `6`; index avg `0.0125` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.1035` n `782`
- 1h: commodity avg `0.0281` n `12`; crypto_alt avg `-0.0973` n `230`; crypto_major avg `0.1072` n `8`; equity avg `-0.0387` n `102`; fx avg `-0.0479` n `6`; index avg `0.0199` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0587` n `782`
- 4h: commodity avg `0.1429` n `12`; crypto_alt avg `-0.371` n `230`; crypto_major avg `-0.3102` n `8`; equity avg `-0.2644` n `102`; fx avg `-0.0317` n `6`; index avg `-0.0295` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.1492` n `782`
- 24h: commodity avg `-1.0743` n `12`; crypto_alt avg `0.1402` n `230`; crypto_major avg `0.068` n `8`; equity avg `0.8174` n `102`; fx avg `-0.1425` n `6`; index avg `0.2309` n `25`; metal avg `0.2472` n `20`; unknown avg `0.2049` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
