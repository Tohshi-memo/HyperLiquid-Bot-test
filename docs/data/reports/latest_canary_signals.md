# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T15:52:28.335007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0832` n `13`; crypto_alt avg `-0.0612` n `238`; crypto_major avg `0.0525` n `8`; equity avg `-0.0425` n `156`; fx avg `-0.0045` n `6`; index avg `0.0002` n `27`; metal avg `-0.029` n `20`; unknown avg `-0.2388` n `1261`
- 1h: commodity avg `0.0409` n `13`; crypto_alt avg `0.0728` n `238`; crypto_major avg `0.1329` n `8`; equity avg `-0.6566` n `156`; fx avg `-0.0035` n `6`; index avg `-0.0758` n `27`; metal avg `-0.154` n `20`; unknown avg `159.6999` n `1255`
- 4h: commodity avg `0.0111` n `13`; crypto_alt avg `0.0351` n `238`; crypto_major avg `-0.2181` n `8`; equity avg `-1.1758` n `156`; fx avg `-0.0709` n `6`; index avg `-0.045` n `27`; metal avg `-0.2154` n `20`; unknown avg `4.8695` n `1147`
- 24h: commodity avg `0.5761` n `13`; crypto_alt avg `-5.8706` n `238`; crypto_major avg `-4.7165` n `8`; equity avg `-5.9899` n `156`; fx avg `-0.1243` n `6`; index avg `-0.4943` n `27`; metal avg `-0.9568` n `20`; unknown avg `39.9986` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
