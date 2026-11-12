# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T21:22:27.513268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `13`; crypto_alt avg `0.1646` n `239`; crypto_major avg `0.1902` n `8`; equity avg `-0.0546` n `162`; fx avg `-0.0039` n `6`; index avg `-0.0138` n `27`; metal avg `-0.0033` n `20`; unknown avg `1.2314` n `1255`
- 1h: commodity avg `0.1072` n `13`; crypto_alt avg `0.3145` n `239`; crypto_major avg `0.1016` n `8`; equity avg `0.1053` n `162`; fx avg `0.0077` n `6`; index avg `0.0044` n `27`; metal avg `-0.0894` n `20`; unknown avg `186.5008` n `1235`
- 4h: commodity avg `0.519` n `13`; crypto_alt avg `0.9502` n `239`; crypto_major avg `0.3987` n `8`; equity avg `-0.0901` n `162`; fx avg `0.0113` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0323` n `20`; unknown avg `1.301` n `1223`
- 24h: commodity avg `0.9461` n `13`; crypto_alt avg `-2.2697` n `239`; crypto_major avg `-3.0564` n `8`; equity avg `-2.4255` n `162`; fx avg `-0.127` n `6`; index avg `-0.1109` n `27`; metal avg `-0.7498` n `20`; unknown avg `30.902` n `1149`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
