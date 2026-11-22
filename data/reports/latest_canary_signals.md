# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T15:07:29.632813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `0.0208` n `239`; crypto_major avg `0.0769` n `8`; equity avg `0.049` n `166`; fx avg `0.0005` n `6`; index avg `0.022` n `27`; metal avg `0.0014` n `20`; unknown avg `1.9439` n `1253`
- 1h: commodity avg `-0.0254` n `13`; crypto_alt avg `-0.2637` n `239`; crypto_major avg `0.1352` n `8`; equity avg `0.023` n `166`; fx avg `0.0037` n `6`; index avg `0.0122` n `27`; metal avg `0.0337` n `20`; unknown avg `2.063` n `1249`
- 4h: commodity avg `-0.0423` n `13`; crypto_alt avg `-0.2205` n `239`; crypto_major avg `-0.1641` n `8`; equity avg `0.0398` n `166`; fx avg `0.0129` n `6`; index avg `0.0481` n `27`; metal avg `0.0054` n `20`; unknown avg `143.3507` n `1245`
- 24h: commodity avg `-0.0416` n `13`; crypto_alt avg `0.2063` n `239`; crypto_major avg `0.5013` n `8`; equity avg `0.8872` n `166`; fx avg `-0.0062` n `6`; index avg `0.177` n `27`; metal avg `0.0209` n `20`; unknown avg `187.1803` n `1080`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
