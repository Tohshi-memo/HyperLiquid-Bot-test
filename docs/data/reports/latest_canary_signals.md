# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T07:52:27.950800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `13`; crypto_alt avg `0.2772` n `239`; crypto_major avg `0.2583` n `8`; equity avg `0.6068` n `158`; fx avg `0.0257` n `6`; index avg `0.0999` n `27`; metal avg `0.1268` n `20`; unknown avg `1.0094` n `1256`
- 1h: commodity avg `0.043` n `13`; crypto_alt avg `-0.1674` n `239`; crypto_major avg `-0.1678` n `8`; equity avg `0.1122` n `158`; fx avg `-0.0551` n `6`; index avg `0.0047` n `27`; metal avg `0.0366` n `20`; unknown avg `0.5018` n `1248`
- 4h: commodity avg `-0.0452` n `13`; crypto_alt avg `0.0116` n `239`; crypto_major avg `-0.4884` n `8`; equity avg `-0.0035` n `158`; fx avg `-0.1079` n `6`; index avg `-0.0183` n `27`; metal avg `0.0532` n `20`; unknown avg `-0.0543` n `1218`
- 24h: commodity avg `1.1877` n `13`; crypto_alt avg `-4.0588` n `239`; crypto_major avg `-5.9086` n `8`; equity avg `-5.987` n `158`; fx avg `-0.0376` n `6`; index avg `-0.8063` n `27`; metal avg `-0.4244` n `20`; unknown avg `232.23` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
