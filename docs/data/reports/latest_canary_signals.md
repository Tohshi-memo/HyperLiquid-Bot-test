# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T11:07:27.512504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1106` n `13`; crypto_alt avg `-0.1527` n `239`; crypto_major avg `-0.247` n `8`; equity avg `-0.1311` n `165`; fx avg `-0.0048` n `6`; index avg `-0.037` n `27`; metal avg `-0.0064` n `20`; unknown avg `223.8736` n `1252`
- 1h: commodity avg `0.2437` n `13`; crypto_alt avg `-0.2001` n `239`; crypto_major avg `-0.1558` n `8`; equity avg `0.2387` n `165`; fx avg `0.0051` n `6`; index avg `0.0031` n `27`; metal avg `0.1643` n `20`; unknown avg `702.4166` n `1256`
- 4h: commodity avg `-0.2429` n `13`; crypto_alt avg `-0.2138` n `239`; crypto_major avg `-0.4712` n `8`; equity avg `-0.2366` n `165`; fx avg `-0.0482` n `6`; index avg `-0.0187` n `27`; metal avg `0.3605` n `20`; unknown avg `22.8415` n `1194`
- 24h: commodity avg `-0.424` n `13`; crypto_alt avg `-3.3858` n `239`; crypto_major avg `-2.8655` n `8`; equity avg `-7.7506` n `165`; fx avg `-0.1273` n `6`; index avg `-0.8012` n `27`; metal avg `-1.2146` n `20`; unknown avg `30.0822` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
