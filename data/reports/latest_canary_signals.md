# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T07:52:26.773750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `-0.0065` n `230`; crypto_major avg `0.0391` n `8`; equity avg `-0.1332` n `102`; fx avg `0.0073` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0327` n `20`; unknown avg `0.1507` n `777`
- 1h: commodity avg `0.0165` n `12`; crypto_alt avg `-0.0273` n `230`; crypto_major avg `-0.0255` n `8`; equity avg `0.1226` n `102`; fx avg `0.0221` n `6`; index avg `0.0145` n `25`; metal avg `0.0031` n `20`; unknown avg `0.2932` n `777`
- 4h: commodity avg `-0.1137` n `12`; crypto_alt avg `0.4875` n `230`; crypto_major avg `1.0882` n `8`; equity avg `1.5859` n `102`; fx avg `-0.0388` n `6`; index avg `0.3419` n `25`; metal avg `0.1993` n `20`; unknown avg `0.338` n `761`
- 24h: commodity avg `0.0197` n `12`; crypto_alt avg `-1.1526` n `230`; crypto_major avg `1.1666` n `8`; equity avg `-1.2105` n `102`; fx avg `-0.1011` n `6`; index avg `-0.1256` n `25`; metal avg `0.0114` n `20`; unknown avg `-0.001` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
