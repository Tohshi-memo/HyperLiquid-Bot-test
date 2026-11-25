# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T21:52:33.051785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `13`; crypto_alt avg `0.0803` n `239`; crypto_major avg `-0.1746` n `8`; equity avg `-0.2517` n `168`; fx avg `-0.011` n `6`; index avg `-0.0254` n `27`; metal avg `0.0359` n `20`; unknown avg `1.5437` n `1265`
- 1h: commodity avg `0.0328` n `13`; crypto_alt avg `0.3586` n `239`; crypto_major avg `0.2114` n `8`; equity avg `0.1508` n `168`; fx avg `-0.015` n `6`; index avg `0.0181` n `27`; metal avg `0.0226` n `20`; unknown avg `84.1321` n `1229`
- 4h: commodity avg `0.0029` n `13`; crypto_alt avg `1.501` n `239`; crypto_major avg `1.6877` n `8`; equity avg `2.1432` n `168`; fx avg `-0.0007` n `6`; index avg `0.1852` n `27`; metal avg `0.6653` n `20`; unknown avg `1.8372` n `1213`
- 24h: commodity avg `0.4002` n `13`; crypto_alt avg `2.621` n `239`; crypto_major avg `1.3119` n `8`; equity avg `-0.6409` n `168`; fx avg `0.0411` n `6`; index avg `-0.0711` n `27`; metal avg `0.1896` n `20`; unknown avg `-0.1127` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
