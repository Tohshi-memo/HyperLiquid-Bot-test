# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T22:22:29.886867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0259` n `13`; crypto_alt avg `-0.1459` n `239`; crypto_major avg `0.073` n `8`; equity avg `0.1132` n `166`; fx avg `0.0106` n `6`; index avg `0.0087` n `27`; metal avg `0.0192` n `20`; unknown avg `0.0179` n `1264`
- 1h: commodity avg `0.0167` n `13`; crypto_alt avg `-0.303` n `239`; crypto_major avg `0.0076` n `8`; equity avg `0.3785` n `166`; fx avg `0.0001` n `6`; index avg `0.0487` n `27`; metal avg `0.0131` n `20`; unknown avg `365.1915` n `1258`
- 4h: commodity avg `-0.1202` n `13`; crypto_alt avg `-1.7795` n `239`; crypto_major avg `-0.9725` n `8`; equity avg `0.0008` n `166`; fx avg `-0.0043` n `6`; index avg `0.0241` n `27`; metal avg `-0.1348` n `20`; unknown avg `1.4825` n `1224`
- 24h: commodity avg `-1.409` n `13`; crypto_alt avg `0.8126` n `239`; crypto_major avg `1.4192` n `8`; equity avg `6.4306` n `166`; fx avg `-0.1868` n `6`; index avg `0.6388` n `27`; metal avg `0.6225` n `20`; unknown avg `289.8516` n `1050`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
