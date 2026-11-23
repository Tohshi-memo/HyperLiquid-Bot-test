# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T12:22:29.738276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.072` n `13`; crypto_alt avg `-0.1111` n `239`; crypto_major avg `-0.1713` n `8`; equity avg `-0.4253` n `166`; fx avg `-0.0081` n `6`; index avg `-0.0523` n `27`; metal avg `-0.0828` n `20`; unknown avg `0.7171` n `1260`
- 1h: commodity avg `0.0662` n `13`; crypto_alt avg `0.0229` n `239`; crypto_major avg `-0.1215` n `8`; equity avg `-0.5776` n `166`; fx avg `-0.0174` n `6`; index avg `-0.0696` n `27`; metal avg `-0.107` n `20`; unknown avg `0.4221` n `1256`
- 4h: commodity avg `-0.1797` n `13`; crypto_alt avg `0.1847` n `239`; crypto_major avg `0.3267` n `8`; equity avg `-0.2156` n `166`; fx avg `-0.0706` n `6`; index avg `-0.0206` n `27`; metal avg `0.0404` n `20`; unknown avg `219.2514` n `1138`
- 24h: commodity avg `-0.8978` n `13`; crypto_alt avg `0.8181` n `239`; crypto_major avg `0.9556` n `8`; equity avg `1.3225` n `166`; fx avg `0.1683` n `6`; index avg `0.0658` n `27`; metal avg `0.2794` n `20`; unknown avg `0.0005` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
