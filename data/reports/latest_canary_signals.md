# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T11:37:28.099016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0548` n `13`; crypto_alt avg `-0.06` n `239`; crypto_major avg `-0.0178` n `8`; equity avg `0.0632` n `165`; fx avg `0.0135` n `6`; index avg `0.0153` n `27`; metal avg `-0.0076` n `20`; unknown avg `0.6198` n `1262`
- 1h: commodity avg `0.2835` n `13`; crypto_alt avg `-0.5559` n `239`; crypto_major avg `-0.7707` n `8`; equity avg `-0.6323` n `165`; fx avg `0.0092` n `6`; index avg `-0.0945` n `27`; metal avg `-0.079` n `20`; unknown avg `378.8499` n `1258`
- 4h: commodity avg `-0.0745` n `13`; crypto_alt avg `-0.3826` n `239`; crypto_major avg `-0.2911` n `8`; equity avg `-0.3898` n `165`; fx avg `0.0058` n `6`; index avg `-0.0337` n `27`; metal avg `0.3513` n `20`; unknown avg `42.1827` n `1194`
- 24h: commodity avg `-0.1355` n `13`; crypto_alt avg `-3.9946` n `239`; crypto_major avg `-3.6029` n `8`; equity avg `-8.2297` n `165`; fx avg `-0.076` n `6`; index avg `-0.8376` n `27`; metal avg `-1.2721` n `20`; unknown avg `55.1381` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
