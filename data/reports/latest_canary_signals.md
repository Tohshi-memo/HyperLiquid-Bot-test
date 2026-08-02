# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T23:07:25.096977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0367` n `12`; crypto_alt avg `-0.0901` n `230`; crypto_major avg `-0.1379` n `8`; equity avg `0.1172` n `102`; fx avg `0.0067` n `6`; index avg `0.0648` n `25`; metal avg `-0.0245` n `20`; unknown avg `0.0076` n `783`
- 1h: commodity avg `0.3387` n `12`; crypto_alt avg `-0.4788` n `230`; crypto_major avg `-0.5479` n `8`; equity avg `0.1118` n `102`; fx avg `-0.0233` n `6`; index avg `0.0452` n `25`; metal avg `-0.0795` n `20`; unknown avg `0.1993` n `783`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `-0.228` n `230`; crypto_major avg `-0.0044` n `8`; equity avg `0.312` n `102`; fx avg `0.0946` n `6`; index avg `0.073` n `25`; metal avg `-0.1019` n `20`; unknown avg `1.1585` n `782`
- 24h: commodity avg `-1.1443` n `12`; crypto_alt avg `1.0133` n `230`; crypto_major avg `1.5105` n `8`; equity avg `1.6869` n `102`; fx avg `-0.0317` n `6`; index avg `0.3717` n `25`; metal avg `0.1766` n `20`; unknown avg `1.6016` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
