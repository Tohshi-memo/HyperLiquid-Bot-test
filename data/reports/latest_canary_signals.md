# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T04:22:22.284070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.3637` n `239`; crypto_major avg `0.2622` n `8`; equity avg `0.2102` n `162`; fx avg `0.0007` n `6`; index avg `0.0327` n `27`; metal avg `0.0003` n `20`; unknown avg `0.1573` n `1263`
- 1h: commodity avg `0.1556` n `13`; crypto_alt avg `-0.1852` n `239`; crypto_major avg `-0.2776` n `8`; equity avg `-0.2882` n `162`; fx avg `-0.0267` n `6`; index avg `-0.0289` n `27`; metal avg `-0.0344` n `20`; unknown avg `-0.3048` n `1255`
- 4h: commodity avg `-0.0565` n `13`; crypto_alt avg `-0.0825` n `239`; crypto_major avg `-0.3912` n `8`; equity avg `-1.2964` n `162`; fx avg `-0.0333` n `6`; index avg `-0.1958` n `27`; metal avg `-0.382` n `20`; unknown avg `0.5436` n `1239`
- 24h: commodity avg `-0.3258` n `13`; crypto_alt avg `0.0863` n `239`; crypto_major avg `0.1047` n `8`; equity avg `0.1469` n `162`; fx avg `-0.0442` n `6`; index avg `0.0256` n `27`; metal avg `0.108` n `20`; unknown avg `0.5782` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
