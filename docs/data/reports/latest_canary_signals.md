# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T00:52:38.233051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `13`; crypto_alt avg `-0.013` n `239`; crypto_major avg `0.146` n `8`; equity avg `0.2534` n `166`; fx avg `0.027` n `6`; index avg `0.0274` n `27`; metal avg `0.0467` n `20`; unknown avg `158.1145` n `1266`
- 1h: commodity avg `0.0287` n `13`; crypto_alt avg `0.113` n `239`; crypto_major avg `0.2459` n `8`; equity avg `0.4884` n `166`; fx avg `0.0575` n `6`; index avg `0.1754` n `27`; metal avg `0.2855` n `20`; unknown avg `357.6965` n `1258`
- 4h: commodity avg `0.127` n `13`; crypto_alt avg `-0.0233` n `239`; crypto_major avg `-0.1021` n `8`; equity avg `0.6466` n `166`; fx avg `0.0567` n `6`; index avg `0.1167` n `27`; metal avg `0.2264` n `20`; unknown avg `-0.642` n `1216`
- 24h: commodity avg `-1.0281` n `13`; crypto_alt avg `1.0684` n `239`; crypto_major avg `0.9864` n `8`; equity avg `5.615` n `166`; fx avg `-0.1246` n `6`; index avg `0.5358` n `27`; metal avg `0.5572` n `20`; unknown avg `241.3769` n `1045`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
