# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T03:27:54.525123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0697` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0411` n `13`; crypto_alt avg `0.0643` n `239`; crypto_major avg `-0.0394` n `8`; equity avg `-0.0157` n `166`; fx avg `-0.0056` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0269` n `20`; unknown avg `0.0209` n `1259`
- 1h: commodity avg `-0.0634` n `13`; crypto_alt avg `-0.5854` n `239`; crypto_major avg `-0.7457` n `8`; equity avg `-0.1989` n `166`; fx avg `0.0033` n `6`; index avg `-0.0625` n `27`; metal avg `-0.085` n `20`; unknown avg `0.3747` n `1259`
- 4h: commodity avg `-0.0914` n `13`; crypto_alt avg `-1.0035` n `239`; crypto_major avg `-1.1436` n `8`; equity avg `-0.3171` n `166`; fx avg `-0.0144` n `6`; index avg `-0.0739` n `27`; metal avg `-0.0981` n `20`; unknown avg `177.7363` n `1252`
- 24h: commodity avg `-0.067` n `13`; crypto_alt avg `0.4792` n `239`; crypto_major avg `2.0471` n `8`; equity avg `0.6048` n `166`; fx avg `-0.0462` n `6`; index avg `0.1169` n `27`; metal avg `0.0314` n `20`; unknown avg `418.3433` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
