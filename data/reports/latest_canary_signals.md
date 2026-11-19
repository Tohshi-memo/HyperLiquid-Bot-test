# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T14:22:29.771939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `-0.0714` n `239`; crypto_major avg `-0.0441` n `8`; equity avg `0.0597` n `165`; fx avg `0.0026` n `6`; index avg `0.0012` n `27`; metal avg `-0.0593` n `20`; unknown avg `0.1128` n `1263`
- 1h: commodity avg `0.1307` n `13`; crypto_alt avg `-0.0489` n `239`; crypto_major avg `0.122` n `8`; equity avg `-0.0945` n `165`; fx avg `0.0304` n `6`; index avg `-0.0301` n `27`; metal avg `-0.044` n `20`; unknown avg `158.3007` n `1263`
- 4h: commodity avg `0.1885` n `13`; crypto_alt avg `0.0798` n `239`; crypto_major avg `0.2968` n `8`; equity avg `-0.1208` n `165`; fx avg `0.0117` n `6`; index avg `-0.0679` n `27`; metal avg `-0.2315` n `20`; unknown avg `0.5101` n `1257`
- 24h: commodity avg `0.1505` n `13`; crypto_alt avg `0.5317` n `239`; crypto_major avg `0.5215` n `8`; equity avg `1.3009` n `165`; fx avg `0.0537` n `6`; index avg `0.3169` n `27`; metal avg `-0.3742` n `20`; unknown avg `5.7259` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
