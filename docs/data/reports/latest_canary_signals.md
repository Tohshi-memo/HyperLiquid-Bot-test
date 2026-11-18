# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T04:22:43.328969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.02` n `239`; crypto_major avg `0.088` n `8`; equity avg `0.313` n `163`; fx avg `-0.0008` n `6`; index avg `0.043` n `27`; metal avg `0.0475` n `20`; unknown avg `2.9173` n `1264`
- 1h: commodity avg `-0.0629` n `13`; crypto_alt avg `0.1201` n `239`; crypto_major avg `0.2206` n `8`; equity avg `0.5799` n `163`; fx avg `-0.0139` n `6`; index avg `0.0975` n `27`; metal avg `0.0564` n `20`; unknown avg `4.8727` n `1256`
- 4h: commodity avg `-0.201` n `13`; crypto_alt avg `-0.7213` n `239`; crypto_major avg `-0.6714` n `8`; equity avg `-0.9925` n `163`; fx avg `-0.0438` n `6`; index avg `-0.0764` n `27`; metal avg `-0.5066` n `20`; unknown avg `6.0974` n `1256`
- 24h: commodity avg `0.2879` n `13`; crypto_alt avg `-0.3132` n `239`; crypto_major avg `0.0058` n `8`; equity avg `0.0851` n `163`; fx avg `-0.0836` n `6`; index avg `0.0214` n `27`; metal avg `-0.7723` n `20`; unknown avg `240.0762` n `1073`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
