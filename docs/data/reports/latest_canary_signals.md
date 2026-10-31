# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T18:52:26.221349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `13`; crypto_alt avg `0.0038` n `238`; crypto_major avg `-0.0035` n `8`; equity avg `0.0129` n `156`; fx avg `-0.0082` n `6`; index avg `-0.0119` n `27`; metal avg `0.0024` n `20`; unknown avg `-0.2403` n `1260`
- 1h: commodity avg `0.0285` n `13`; crypto_alt avg `0.0605` n `238`; crypto_major avg `0.0223` n `8`; equity avg `0.0316` n `156`; fx avg `-0.0011` n `6`; index avg `0.0026` n `27`; metal avg `-0.0007` n `20`; unknown avg `-0.8011` n `1216`
- 4h: commodity avg `-0.0001` n `13`; crypto_alt avg `0.3694` n `238`; crypto_major avg `0.4281` n `8`; equity avg `0.0592` n `156`; fx avg `-0.016` n `6`; index avg `-0.0042` n `27`; metal avg `0.0055` n `20`; unknown avg `0.3301` n `1194`
- 24h: commodity avg `-0.4045` n `13`; crypto_alt avg `2.0554` n `238`; crypto_major avg `1.2371` n `8`; equity avg `1.8294` n `156`; fx avg `-0.0159` n `6`; index avg `0.1396` n `27`; metal avg `0.186` n `20`; unknown avg `0.7833` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
