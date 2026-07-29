# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T18:07:40.413378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `0.5003` n `230`; crypto_major avg `0.4075` n `8`; equity avg `0.7988` n `102`; fx avg `0.0048` n `6`; index avg `0.1629` n `25`; metal avg `0.3136` n `18`; unknown avg `-0.1671` n `763`
- 1h: commodity avg `0.0162` n `12`; crypto_alt avg `1.0407` n `230`; crypto_major avg `0.8531` n `8`; equity avg `1.0802` n `102`; fx avg `0.0116` n `6`; index avg `0.2014` n `25`; metal avg `0.3009` n `20`; unknown avg `-0.0424` n `778`
- 4h: commodity avg `0.1793` n `12`; crypto_alt avg `0.4675` n `230`; crypto_major avg `0.3729` n `8`; equity avg `-0.0033` n `102`; fx avg `-0.0189` n `6`; index avg `0.0416` n `25`; metal avg `0.5784` n `20`; unknown avg `-0.2436` n `777`
- 24h: commodity avg `1.2675` n `12`; crypto_alt avg `-1.2314` n `230`; crypto_major avg `0.6651` n `8`; equity avg `-0.4466` n `102`; fx avg `-0.0337` n `6`; index avg `-0.1662` n `25`; metal avg `0.328` n `20`; unknown avg `-0.4584` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
